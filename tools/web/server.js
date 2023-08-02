const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
//const fetch = require('node-fetch');
const fs = require('fs');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve the frontend
app.use(express.static(path.join(__dirname, 'web')));

// Handle the upload request and forward it to the Flask backend
app.post('/upload', (req, res) => {
  const fileContent = req.body.content;

  // Save the uploaded YAML file to local memory
  fs.writeFileSync('shared/uploads/uploaded_file.yaml', fileContent);

  // Execute custom logic using the Python script
  exec('python backend/custom_logic.py', (error, stdout, stderr) => {
    if (error) {
      console.error('Error executing custom logic:', error);
      res.status(500).json({ error: 'Error processing YAML' });
      return;
    }

    // Read the processed content from the output file
    const processedContent = fs.readFileSync('shared/uploads/processed_file.txt', 'utf8');

    // Prepare the download response
    const downloadURL = '/download';
    const response = {
      downloadURL,
      processedContent,
    };
    res.json(response);
  });
});

app.get('/download', (req, res) => {
  const filename = 'processed_file.txt';
  const filepath = path.join(__dirname, 'shared', 'uploads', filename);
  res.download(filepath);
});

app.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
});
