from flask import Flask, request, jsonify, send_file, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
import os
from validate import handler
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
    
@app.route('/upload')
def upload_file_landing():
   if request.args.get('filename'):
    f = open('.app_data/reports/' + request.args.get('filename'))
    output = f.read()
    return render_template('upload.html', output=output, filename=request.args.get('filename'))
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
            subscription_name = request.args.get('subscription_name')
            filename= secure_filename(f.filename)
            save_location = os.path.join('.app_data/uploads', filename)
            f.save(save_location)

            # validate file
            report_directory = '.app_data/reports'
            ontology_path = '../ontology/yaml/resources'
            loop = asyncio.get_running_loop()
            _executor = ThreadPoolExecutor(1)
            report_filename = await loop.run_in_executor(_executor, lambda: handler.RunValidation(
                filenames=[save_location],
                default_types_filepath=ontology_path,
                report_directory=report_directory,
                subscription=subscription_name,
                
            ))

            base_filename = os.path.basename(report_filename)

            return redirect(
                url_for('upload_file_landing', filename=base_filename))
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
