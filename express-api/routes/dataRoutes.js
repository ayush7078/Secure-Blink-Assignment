const express = require('express');
const router = express.Router();
const { receiveData, getData } = require('../controllers/dataController');

// POST route for receiving data
router.post('/', receiveData);

// GET route to retrieve data
router.get('/', getData);

module.exports = router;
