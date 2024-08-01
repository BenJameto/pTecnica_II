const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.get('/api/greet', (req, res) => {
    res.json({ message: 'Hello from the API!' });
});

app.listen(port, () => {
    console.log(`API listening at http://localhost:${port}`);
});
