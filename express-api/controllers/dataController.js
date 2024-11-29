// controllers/dataController.js

// Mock database for storing data
let processedData = [];

// Function to handle receiving processed data
const receiveData = (req, res) => {
  const data = req.body;
  if (!data || data.length === 0) {
    return res.status(400).json({ message: 'No data received' });
  }
  processedData = data;  // Store the processed data
  res.status(200).json({ message: 'Data received successfully' });
};

// Function to handle retrieving stored data
const getData = (req, res) => {
  if (processedData.length === 0) {
    return res.status(404).json({ message: 'No processed data available' });
  }
  res.status(200).json(processedData);
};

// Export the functions to be used in routes
module.exports = {
  receiveData,
  getData
};
