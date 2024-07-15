const express = require('express');
const multer = require('multer');
const fs = require('fs');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const upload = multer();

app.use(express.json());
app.use(express.static('public'));

app.post('/update_model', upload.none(), (req, res) => {
    const data = req.body;

    fs.writeFileSync('user_measurements.json', JSON.stringify(data));

    exec('blender --background --python update_model.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).send('Error updating model');
        }

        res.sendFile(path.join(__dirname, 'updated_model.glb'));
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
