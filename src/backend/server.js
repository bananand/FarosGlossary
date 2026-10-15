//di sini server berperan mengambil data dari database kamus untuk diserahkan ke browser(express)
const express = require('express');

//cross origin resource sharing memberikan alamat dari generator localhost dengan port berbeda seperti liveserver
const cors = require('cors');
const sqlite3 = require('sqlite3');
const path = require('path');

const app = express();
app.use(cors());
//membawa ke frontend dari bantuan express
app.use(express.static(path.join(__dirname, '..', 'frontend')));

const db = new sqlite3.Database(
    path.join(__dirname, '..', 'kamus.db'), //keluar 2 level ke directory kamus.db untuk berperan sebagai db sqlite
    sqlite3.OPEN_READONLY
);

app.get('/api/kata/:kata', (req, res) => {
    const kata = req.params.kata.toLowerCase();

    db.all(
        'SELECT pos, definisi_en, terjemahan, contoh FROM bank_kata_inggris WHERE kata = ? ORDER BY id',
        [kata], 
        (err, rows) => {
            if(err) return res.status(500).json({error: err.message});
            if(rows.length === 0) return res.status(404).json({error: 'Kata tidak ditemukan'});
            res.json(rows);
        }
    );
});

// landing page kata acak yang punya definisi asli bukan angka, satu kata dan panjangnya wajar
app.get('/api/acak', (req, res) => {
    const n = Math.min(parseInt(req.query.n, 10) || 30, 60);

    db.all(
        `SELECT DISTINCT kata FROM bank_kata_inggris
        WHERE TERJEMAHAN IS NOT null
            AND kata NOT GLOB '*[0-9]*'
            AND kata NOT LIKE '% %'
            AND length(kata) BETWEEN 4 AND 14
        ORDER BY RANDOM() LIMIT ?`, 
        [n],
        (err, rows) => {
            if(err) return res.status(500).json({error: err.message});
            res.json(rows.map((r) => r.kata));
        }
    );
});

app.listen(3000, () => console.log('Server is running on http://localhost:3000'));