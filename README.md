# Python Data Processing with Express.js API

This project processes employee data using Python and sends the processed results to an Express.js REST API for temporary storage. Below are the steps to run the Python data processing script and the Express.js server.

## Requirements

- Node.js (for Express server)
- Python 3.x (for data processing)
- pandas, requests libraries (for Python)

## 1. Set Up Express.js Server

### Install Dependencies:
npm install


### Start the Express.js Server:
npm start


## 2. Set Up Python Data Processing
### Install Python Dependencies:
pip install pandas requests

### Run the Python Script:
Make sure the data.csv file is placed in the ./data/ folder, then run the Python script:
python process_data.py

This will process the data, clean it, normalize it, perform analysis, and send the processed data to the Express API.



## API Endpoints
- POST /api/data: Receives processed data and stores it temporarily.
Request Body: Array of employee data (JSON format)
Response: { "message": "Data received successfully" }

- GET /api/data: Retrieves the stored processed data.
Response: JSON array of processed data.



