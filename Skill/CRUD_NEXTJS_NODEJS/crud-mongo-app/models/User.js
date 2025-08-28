const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true, // <- Will reject if missing
  },
  email: {
    type: String,
    required: true,
    unique: true // <- Will reject duplicates
  }
});

module.exports = mongoose.model('User', userSchema);

