const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const bodyParser = require('body-parser');
const path = require('path');
const db = require('./config/db');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './app/views'));

const port = 8000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './app/public')));

MongoClient.connect(db.url, (err, database) => {
  if (err) return console.err(err);
  
  const iridiumDB = database.db('iridium');
  const statusRouter = require('./app/routes/status_routes')(iridiumDB);
  const indexRouter = require('./app/routes/index_routes')(iridiumDB);
  app.use('/', indexRouter);
  app.use('/status', statusRouter);
  app.listen(port, () => {});
});
