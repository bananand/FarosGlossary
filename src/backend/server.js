//di sini server berperan mengambil data dari database kamus untuk diserahkan ke browser(express)
const express = require('express');

//cross origin resource sharing memberikan alamat dari generator localhost dengan port berbeda seperti liveserver
const cors = require('cors');
const sqlite3 = require('sqlite3');
const path = require('path');

const app = express();
app.use(cors());

const db = new sqlite3.Database(
    path.join(__dirname, '..', 'kamus.db'), //keluar 2 level ke directory kamus.db untuk berperan sebagai db sqlite
    sqlite3.OPEN_READONLY
);

app.get('/api/kata/:kata', (req, res) => {
    const kata = req.params.kata.toLowerCase();

    db.all(
        'SELECT definisi_en, terjemahan FROM bank_kata_inggris WHERE kata = ?',
        [kata], 
        (err, rows) => {
            if(err) return res.status(500).json({error: err.message});
            if(rows.length === 0) return res.status(404).json({error: 'Kata tidak ditemukan'});
            res.json(rows);
        }
    );
});
app.listen(3000, () => console.log('Server is running on http://localhost:3000'));