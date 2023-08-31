from flask import Flask, request, send_file, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from validate import handler
import asyncio
from concurrent.futures import ThreadPoolExecutor
from git import Repo, Remote

_APP_DATA_REPORTS = '/source/tools/.app_data/reports'
_APP_DATA_UPLOADS = '/source/tools/.app_data/uploads'
_ONTOLOGY_PATH = '/source/ontology/yaml/resources'
_INSTANCE_VALIDATION_REPORT_FILENAME = 'instance_validation_report_filename'
_GIT_REPO_URL = 'https://github.com/google/digitalbuildings'
_GIT_REPO_DIR = '/main'

app = Flask(__name__)
repo = Repo.clone_from(_GIT_REPO_URL, _GIT_REPO_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_building_config():
   if request.args.get(_INSTANCE_VALIDATION_REPORT_FILENAME):
    iv_report = open(os.path.join(_APP_DATA_REPORTS, request.args.get(_INSTANCE_VALIDATION_REPORT_FILENAME)))
    iv_output = iv_report.read()
    return render_template('upload.html', iv_output=iv_output, iv_filename=request.args.get(_INSTANCE_VALIDATION_REPORT_FILENAME))
   else:
       return render_template('upload.html')
    
@app.route('/validate', methods=['POST', 'GET'])
async def validate_building_config():
    if request.method == 'POST':
        try:
            f = request.files['file']
            filename= secure_filename(f.filename)
            save_location = os.path.join(_APP_DATA_UPLOADS, filename)
            f.save(save_location)
            print(save_location)

            # Get remote repo branch ontology if passed in
            pull_request_id = request.form.get('dbo_commit_hash')
            remote_name = 'digitalbuildings'
            if pull_request_id:
                if not Remote(repo=repo, name=remote_name).exists():
                    Remote.create(repo=repo, name=remote_name, url='https://github.com/google/digitalbuildings')
                fetched_branch = repo.remote(name=remote_name).fetch(f'pull/{pull_request_id}/head')
                repo.git.checkout(fetched_branch)

            # validate file
            loop = asyncio.get_running_loop()
            _executor = ThreadPoolExecutor(1)
            instance_validation_report_filename = await loop.run_in_executor(_executor, lambda: handler.RunValidation(
                filenames=[save_location],
                default_types_filepath=_ONTOLOGY_PATH,
                report_directory=_APP_DATA_REPORTS,

            ))
            repo.git.checkout(repo.remote().fetch()[0])

            instance_base_filename = os.path.basename(instance_validation_report_filename)

            return redirect(
                url_for('upload_building_config', instance_validation_report_filename=instance_base_filename))
        except Exception as e:
            return str(e), 500
        
@app.route('/download/<filename>')
def download_file(filename):
    return send_file(
                path_or_file=os.path.join(_APP_DATA_REPORTS, filename),
                download_name=filename,
                as_attachment=True
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
