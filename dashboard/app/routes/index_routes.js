const express = require('express');
const router = express.Router();

module.exports = function(db) {
    // get request for the main site
    router.get('/', (req, res) => {
      res.render('index');
    });

    return router;
};