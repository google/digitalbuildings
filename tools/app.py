from flask import Flask, request, jsonify, send_file, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
import os
from validate import handler
import asyncio
from concurrent.futures import ThreadPoolExecutor
from git import Repo, Remote
import subprocess

app = Flask(__name__)
    
@app.route('/upload')
def upload_file_landing():
   if request.args.get('instance_validation_report_filename'):
    iv_report = open('.app_data/reports/' + request.args.get('instance_validation_report_filename'))
    iv_output = iv_report.read()
   # if request.args.get('telemetry_validation_report_filename'):
   #     tv_report = open('.app_data/reports/' + request.args.get('telemetry_validation_report_filename'))
   #     tv_output = tv_report.read()
   #     return render_template('upload.html', iv_output=iv_output)
    return render_template('upload.html', iv_output=iv_output, iv_filename=request.args.get('instance_validation_report_filename'))
   else:
       return render_template('upload.html')
    
@app.route('/validate', methods=['POST', 'GET'])
async def validate_yaml_file():
    # A building config is posted to the validate endpoint
    # a sub process is created that runs the instance validator
    # Report log is just displayed on the screen...and downloadable?

    if request.method == 'POST':
        try:
            f = request.files['file']
            filename= secure_filename(f.filename)
            save_location = os.path.join('.app_data/uploads', filename)
            f.save(save_location)

            # Get remote repo branch ontology if passed in
            pull_request_id = request.form.get('dbo_commit_hash')
            repo = Repo('..')
            remote_name = 'digitalbuildings'
            if pull_request_id:
                print(pull_request_id)
                db_remote = Remote.create(repo=repo, name=remote_name, url='https://github.com/google/digitalbuildings')
                fetched_branch = repo.remote(name=remote_name).fetch(f'pull/{pull_request_id}/head')
                print('fetched branch')
                repo.git.checkout(fetched_branch)
                print('checkout branch')

            # validate file
            report_directory = '.app_data/reports'
            ontology_path = '../ontology/yaml/resources'
            loop = asyncio.get_running_loop()
            _executor = ThreadPoolExecutor(1)
            instance_validation_report_filename = await loop.run_in_executor(_executor, lambda: handler.RunValidation(
                filenames=[save_location],
                default_types_filepath=ontology_path,
                report_directory=report_directory,
                gcp_credential_path=os.path.expanduser('~/code/creds/oauth_client_credential.json')

            ))

            instance_base_filename = os.path.basename(instance_validation_report_filename)
            print(instance_base_filename)

            return redirect(
                url_for('upload_file_landing', instance_validation_report_filename=instance_base_filename))
        except Exception as e:
            return str(e), 500
        
@app.route('/download/<filename>')
def download_file(filename):
    return send_file(
                path_or_file='.app_data/reports/' + filename,
                download_name=filename,
                as_attachment=True
            )


if __name__ == '__main__':
    app.run(debug=True)
