const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
const dataRoutes = require('./routes/dataRoutes');

dotenv.config();

const app = express();
app.use(cors());
app.use(bodyParser.json());

// API Routes
app.use('/api/data', dataRoutes);

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
