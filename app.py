const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.listen(process.env.PORT || 3000, () => {
    console.log('Server is running...');
});

// Keep the app alive
setInterval(() => {
    require('http').get(`http://${process.env.PROJECT_DOMAIN}.glitch.me`);
}, 3 * 60 * 1000); // every 3 minutes
