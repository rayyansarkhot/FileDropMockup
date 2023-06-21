const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

// Read the file
const filePath = 'doc.pdf'; // Replace with the actual file path
const fileStream = fs.createReadStream(filePath);

// Create a FormData object
const formData = new FormData();
formData.append('file', fileStream);

// API endpoint URL
const apiUrl = 'http://127.0.0.1:8000';

// Send the file using Axios
axios.post(apiUrl, formData, {
  headers: formData.getHeaders(),
})
  .then(response => {
    console.log('File uploaded successfully:', response.data);
  })
  .catch(error => {
    console.error('Error uploading file:', error);
  });
