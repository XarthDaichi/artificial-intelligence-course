const express = require('express');
const cors = require('cors');

const bodyParser = require('body-parser');

const fs = require('fs');
const path = require('path');


const app = express();
const port = 3001; // Change this port as needed

app.use(cors());

app.use(bodyParser.json());

// Serve static content (e.g., React build)
app.use(express.static('build'));

// Process endpoint
app.post('/echo', (req, res) => {
  // Just echo the input and echo it with a timestamp
  console.log(`req.body = ${req.body}`)
  const timestampedText = `Echo from server: at ${new Date().toISOString()}: ${req.body.text}`;
  console.log(timestampedText)
  res.json({ result: timestampedText });
});

// About endpoint (for future implementation)
app.get('/about', (req, res) => {
  res.send('About page (to be implemented)');
});


// Start the Express server
app.listen(port, () => {
  console.log(`Express server is running on port ${port}`);
});
