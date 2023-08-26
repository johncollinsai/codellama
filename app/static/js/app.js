require('dotenv').config({ path: __dirname+'/.env' });

// console.log(process.env);  // print environment variables

const express = require('express');
const sendMail = require('./sendMail');
const cors = require('cors');   
const app = express();

app.use(cors()); 
app.use(express.json());

app.post('/send-email', (req, res) => {
    const { to, subject, text } = req.body;
    sendMail(to, subject, text)
        .then(() => res.status(200).send('Email sent successfully!'))
        .catch(error => {
            console.error("Error while sending email:", error);
            res.status(500).send('Failed to send email: ' + error.message)
        });
});


app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

app.listen(3000, () => console.log('Server started on port 3000'));

