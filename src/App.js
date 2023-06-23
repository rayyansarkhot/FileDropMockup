import React, { useState } from 'react';
import axios from 'axios';

const styles = {
  formFileUpload: {
    height: '16rem',
    width: '28rem',
    maxWidth: '100%',
    textAlign: 'center',
    position: 'relative',
  },
  inputFileUpload: {
    display: 'none',
  },
  labelFileUpload: {
    height: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: '2px',
    borderRadius: '1rem',
    borderStyle: 'dashed',
    borderColor: '#cbd5e1',
    backgroundColor: '#f8fafc',
  },
  labelFileUploadDragActive: {
    backgroundColor: '#ffffff',
  },
  uploadButton: {
    cursor: 'pointer',
    padding: '0.25rem',
    fontSize: '1rem',
    border: 'none',
    fontFamily: 'Oswald, sans-serif',
    backgroundColor: 'transparent',
  },
  dragFileElement: {
    position: 'absolute',
    width: '100%',
    height: '100%',
    borderRadius: '1rem',
    top: '0px',
    right: '0px',
    bottom: '0px',
    left: '0px',
  },
};

function App() {
  const [dragActive, setDragActive] = useState(false);
  const [uploadSuccess, setUploadSuccess] = useState(false);
  const [uploadError, setUploadError] = useState(false);
  const [date, setDate] = useState('');
  const [contact, setContact] = useState('');
  const [delivery, setDelivery] = useState('');
  const [commodity, setCommodity] = useState('');

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const file = e.dataTransfer.files[0];
      try {
        const formData = new FormData();
        formData.append('file', file);

        setUploadError(false);
        setUploadSuccess(false);

        const response = await axios.post('http://127.0.0.2:8000', formData);
        const response2 = await axios.post('http://127.0.0.3:8000', formData);
        console.log(response2.data);

        // File uploaded successfully
        setUploadSuccess(true);
        console.log('Response:', response.data);
      } catch (error) {
        // Error occurred while uploading the file
        setUploadError(true);
        console.error('Error uploading file:', error);
      }
    }
  };

  const handleChange = async (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      try {
        const formData = new FormData();
        formData.append('file', file);

        setUploadError(false);
        setUploadSuccess(false);

        const response = await axios.post('http://127.0.0.2:8000', formData);
        const response2 = await axios.post('http://127.0.0.3:8000', formData);
        let date = response2.data[0].choices[0].text;
        let contact = response2.data[1].choices[0].text;
        let delivery = response2.data[2].choices[0].text;
        let commodity = response2.data[3].choices[0].text;
        console.log(`${date}\n${contact}\n${delivery}\n${commodity}`);
        if (response2.data && response2.data.length >= 4) {
          setDate(response2.data[0].choices[0].text);
          setContact(response2.data[1].choices[0].text);
          setDelivery(response2.data[2].choices[0].text);
          setCommodity(response2.data[3].choices[0].text);
        }
        
        // File uploaded successfully
        setUploadSuccess(true);
        console.log('File uploaded successfully');
        console.log('Response:', response.data);
      } catch (error) {
        // Error occurred while uploading the file
        setUploadError(true);
        console.error('Error uploading file:', error);
      }
    }

  };

  const onButtonClick = async (e) => {
    const inputElement = document.getElementById('input-file-upload');
    if (inputElement) {
      inputElement.value = null; // Reset the file input value
      inputElement.click();
    }
    
    handleChange(e);

  };
  

  return (
    <div className="App">
      <h1>Upload PDF for RFQ</h1>
      <form
        id="form-file-upload"
        onDragEnter={handleDrag}
        onDragOver={handleDrag}
        onDragLeave={handleDrag}
        onDrop={handleDrop}
        style={styles.formFileUpload}
      >
        <input
          type="file"
          id="input-file-upload"
          // multiple={false}
          onChange={handleChange}
          style={styles.inputFileUpload}
        />
        <label
          htmlFor="input-file-upload"
          className={dragActive ? 'drag-active' : ''}
          style={{ ...styles.labelFileUpload, ...(dragActive && styles.labelFileUploadDragActive) }}
        >
          <div>
            <p>Drag and drop your file here or</p>
            <button className="upload-button" onClick={onButtonClick} style={styles.uploadButton}>
              Upload a file
            </button>
          </div>
        </label>
        {dragActive && <div id="drag-file-element" style={styles.dragFileElement}></div>}
        {uploadSuccess && <p>File uploaded successfully!</p>}
        {uploadSuccess && (
        <div style={styles.uploadedVariables}>
          <p>Date: {date}</p>
          <p>Contact: {contact}</p>
          <p>Delivery: {delivery}</p>
          <p>Commodity: {commodity}</p>
        </div>
      )}
        {uploadError && <p>Error uploading file. Please try again.</p>}
      </form>
    </div>
  );
}

export default App;