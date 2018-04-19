const ObjectID = require('mongodb').ObjectID;
const {
  goodStatus,
  badStatus,
  errorObject
} = require('./constants');
const express = require('express');
const router = express.Router();

module.exports = function(db) {
  // Get the status
  router.get('/', (req, res) => {
    db.collection('status').findOne({}, (err, item) => {
      if (err) {
        res.send(errorObject);
      }
      else {
        res.send(item);
      }
    })
  });

  // Creates a new, default status
  router.post('/default', (req, res) => {
    const defaultStatus = goodStatus;
    db.collection('status').insert(defaultStatus, (err, result) => {
      if (err) {
        res.send(errorObject);
      } else {
        res.send(defaultStatus);
      }
    })
  });

  // updates the status to bad
  router.put('/bad', (req, res) => {
    db.collection('status').update({}, badStatus, (err, result) => {
      if (err) {
        res.send(errorObject);
      } else {
        res.send(badStatus);
      }
    }); 
  });

  // updates the status to good 
  router.put('/good', (req, res) => {
    db.collection('status').update({}, goodStatus, (err, result) => {
      if (err) {
        res.send(errorObject);
      } else {
        res.send(goodStatus);
      }
    }); 
  });

  return router;
};