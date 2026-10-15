const $ = (id) => document.getElementById(id);
const body = document.body;
const cari = $('cari');
const awan = $('awan');
const grid = $('grid');
const pesan = $('pesan');

const FAV_KEY = 'faros:favorit';
const URUTAN_POS = ['noun', 'verb', 'adjective', 'adverb'];

let kataAktif = '';
let artiAktif = [];
let filterAktif = 'all';

function el(tag, kelas, teks){
    const e = document.createElement(tag);
    if(kelas) e.className = kelas;
    if(teks) e.textContent = teks;
    return e;
}

function setState(s) {
    body.dataset.state = s;
}

function bacaFavorit(){
    try{return JSON.parse(localStorage.getItem(FAV_KEY)) || [];}
    catch{return [];}
}

function simpanFavorit(daftar){
    try{localStorage.setItem(FAV_KEY, JSON.stringify(daftar));} 
    catch{/*Cannot save to browser storage*/}
}

function tampilkanAwan(daftar, pesanKosong){
    awan.replaceChildren();
    if(!daftar.length){
        awan.append(el('p', 'kosong', pesanKosong));
        return;
    }
    for(const kata of daftar){
        const b = el('button', 'kata-awan', kata);
        b.type = 'button';
        b.style.fontSize = (1.1 + Math.random() * 2.6).toFixed(2) + 'rem';
        b.style.fontWeight = Math.random() < 0.25 ? '700' : '400';
        b.style.fontStyle = Math.random() < 0.25 ? 'italic' : 'normal';
        if(Math.random() < 0.2) b.style.writingMode = 'vertical-r1';
        b.addEventListener('click', ()=> cariKata(kata));
        awan.append(b);
    }
}

async function muatAcak(){
    try {
        const r = await fetch('/api/acak?n=40');
        tampilkanAwan(await r.json(), '');
    } catch {
        tampilkanAwan([], 'Tidak bisa terhubung ke server, jalankan server, lalu buka http://localhost:3000');
    }
}

function beranda(){
    cari.value = '';
    cari.blur();
    setState('landing');
    muatAcak();
}

function tampilkanFavorit(){
    cari.value = '';
    setState('landing');
    tampilkanAwan(bacaFavorit(), 'No favorite words yet')
}

async function cariKata(input) {
    const kata = input.trim().toLowerCase();
    if(!kata) return;

    cari.value = kata;
    cari.blur();
    kataAktif = kata;
    filterAktif = 'all';
    $('judul').textContent = kata;
    setState('hasil');

    let error = '';
    try {
        const r = await fetch('/api/kata/' + encodeURIComponent(kata));
        if(r.ok){
            artiAktif = (await r.json()).sort(
                (a, b) => URUTAN_POS.indexOf(a.pos) - URUTAN_POS.indexOf(b.pos)
            );
        } else {
            artiAktif = [];
            error = `${kata} is not found. Try to check or search for the root of the word.`
        }
    } catch {
        artiAktif = [];
        error = 'Cannot connected to the server. Make sure the server is running';
    }

    gambarHasil(error);
    gambarBintang();

}

function gambarHasil(galat = '') {
    const filter = $('filter');
    filter.replaceChildren();
    grid.replaceChildren();
    pesan.textContent = galat;
    if (!artiAktif.length) return;
    
    const hitung = {};
    for (const a of artiAktif) hitung[a.pos] = (hitung[a.pos] || 0) + 1;
    
    const opsi = ['all', ...URUTAN_POS.filter((p) => hitung[p])];
    for (const p of opsi) {
        const nama = p === 'all' ? 'all' : p[0].toUpperCase() + p.slice(1);
        const jumlah = p === 'all' ? artiAktif.length : hitung[p];
        const b = el('button', 'chip', `${nama} ${jumlah}`);
        b.type = 'button';
        b.setAttribute('aria-pressed', String(p === filterAktif));
        b.addEventListener('click', () => { filterAktif = p; gambarHasil(); });
        filter.append(b);
    }

    for (const a of artiAktif) {
        if (filterAktif !== 'all' && a.pos !== filterAktif) continue;
        const kartu = el('article', 'kartu');
        kartu.append(el('span', 'pos', a.pos));
        kartu.append(el('p', 'def', a.definisi_en));
        kartu.append(a.terjemahan
        ? el('p', 'id', a.terjemahan)
        : el('p', 'id kosong', 'Belum ada terjemahan Indonesia'));
        if (a.contoh) kartu.append(el('p', 'contoh', '“' + a.contoh.split(' | ')[0] + '”'));
        grid.append(kartu);
    }
}

/* ---------- Favorit ---------- */

function gambarBintang() {
    const aktif = bacaFavorit().includes(kataAktif);
    const b = $('bintang');
    b.textContent = aktif ? '★' : '☆';
    b.setAttribute('aria-pressed', String(aktif));
    b.setAttribute('aria-label', aktif ? 'Hapus dari favorit' : 'Tambah ke favorit');
}

$('bintang').addEventListener('click', () => {
    const f = bacaFavorit();
    simpanFavorit(f.includes(kataAktif) ? f.filter((x) => x !== kataAktif) : [...f, kataAktif]);
    gambarBintang();
    });
    
/* ---------- Peristiwa ---------- */

cari.addEventListener('focus', () => {
    if (body.dataset.state === 'landing') setState('fokus');
});
cari.addEventListener('blur', () => {
    if (body.dataset.state === 'fokus' && !cari.value.trim()) setState('landing');
});
$('form').addEventListener('submit', (e) => { e.preventDefault(); cariKata(cari.value); });
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') beranda(); });
$('tombol-beranda').addEventListener('click', beranda);
$('tombol-favorit').addEventListener('click', tampilkanFavorit);

muatAcak();