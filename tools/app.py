from flask import Flask, request, jsonify, send_file
import os
from custom_logic import process_yaml

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'shared', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        yaml_content = data.get('content')

        # Save the uploaded YAML file to local memory
        with open(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_file.yaml'), 'w') as f:
            f.write(yaml_content)

        # Process the YAML using custom logic
        processed_content = process_yaml(yaml_content)

        # Save the processed content to a new text file
        with open(os.path.join(app.config['UPLOAD_FOLDER'], 'processed_file.txt'), 'w') as f:
            f.write(processed_content)

        # Prepare the download response
        download_url = '/download'
        response = {
            'downloadURL': download_url
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download', methods=['GET'])
def download():
    try:
        filename = 'processed_file.txt'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        return send_file(filepath, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
