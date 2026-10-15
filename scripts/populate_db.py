import sqlite3
import nltk
from nltk.corpus import wordnet
from pathlib import Path

print("Memeriksa data WordNet multibahasa (OMW)...")
for paket in ("wordnet","omw","omw-2.0", "omw-1.4"):
    nltk.download(paket, quiet=True)

#.resolve() untuk menandai path lengkap program kita sepert C:/.. dari __file__ atau file yang sedang kita buka
DB_PATH = Path(__file__).resolve().parent.parent/"src"/"kamus.db"
#supaya wordnet terambil key dan value untuk kategori kata yang diambil, note untuk adjective s itu derived adjective berbeda dari a yang root adj.
POS_MAP = {"n": "noun", "v": "verb", "a": "adjective", "s": "adjective", "r": "adverb"}

#function lama sebelum memasukkan kategori kata
# def build_massive_database():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('DROP TABLE IF EXISTS bank_kata_inggris')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS bank_kata_inggris (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             kata TEXT NOT NULL,
#             pos TEXT NOT NULL,
#             definisi_en TEXT NOT NULL,
#             terjemahan TEXT,
#             contoh TEXT,
#             UNIQUE(kata, pos, definisi_en)
#     )
# ''') #UNIQUE(kata, pos, definisi_en) berguna untuk membuat kombinasi unik 1 kosakata inggris dengan definisi miliknya sendiri dan kategori kata tsb

#     print("Mengekstrak kata. definisi, terjemahan..")
#     print("Memulai pengambilan kata dari wordnet...")
#     semua_kata = list(wordnet.words())
    
#     data_kata_siap_masuk = []

#     for kata in semua_kata:
#         synsets = wordnet.synsets(kata)
#         kata_terformat = kata.replace('_', ' ') #wordnet pakai underscore buat frasa

#         for synset in synsets:
#             definisi = synset.definition()

#             daftar_indo = synset.lemma_names('ind')
#             #list comprehension python
#             #menghapus duplikat sambil pertahanin urutan dengan dict.keys
#             terjemahan_unik = list(dict.fromkeys(
#                 indo.replace('_', ' ') for indo in daftar_indo
#             ))
#             #pemisah  "; "supaya arti koma tidak tertukar dengan apa yang ada dalam lemma/jadikan null bila kosong
#             terjemahan_bersih = "; ".join(terjemahan_unik) or None

#             data_kata_siap_masuk.append((kata_terformat, definisi, terjemahan_bersih))
#     print(f"Memasukkan {len(data_kata_siap_masuk)} kata ke database.")     

#     cursor.executemany('''
#         INSERT OR IGNORE INTO bank_kata_inggris (kata, definisi_en, terjemahan)
#         VALUES (?, ?, ?)
#     ''', data_kata_siap_masuk)

#     conn.commit()
#     conn.close()

#     print("SELESAI!, bank kosakata bahasa inggris dan terjemahan indonesia telah terisi")

def build_massive_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS bank_kata_inggris')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank_kata_inggris (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kata TEXT NOT NULL,
            pos TEXT NOT NULL,
            definisi_en TEXT NOT NULL,
            terjemahan TEXT,
            contoh TEXT,
            UNIQUE(kata, pos, definisi_en)
    )
''') #UNIQUE(kata, pos, definisi_en) berguna untuk membuat kombinasi unik 1 kosakata inggris dengan definisi miliknya sendiri dan kategori kata tsb

    print("Mengekstrak kata, kategori kata, definisi, terjemahan..")
    print("Memulai pengambilan kata dari wordnet...")
    baris = []
    for synset in wordnet.all_synsets():
        pos = POS_MAP[synset.pos()]
        definisi = synset.definition()

        terjemahan = "; ".join(dict.fromkeys(
            l.replace("_", " ") for l in synset.lemma_names("ind")
        )) or None 
        contoh = " | ".join(synset.examples()) or None
        
        for lemma in synset.lemma_names():
            kata = lemma.replace("_", " ").lower()
            baris.append((kata, pos, definisi, terjemahan, contoh))
    print(f"Memasukkan {len(baris)} baris ke database...")
    cursor.executemany('''
        INSERT OR IGNORE INTO bank_kata_inggris (kata, pos, definisi_en, terjemahan, contoh)
        VALUES(?, ?, ?, ?, ?)
    ''', baris)

    conn.commit()
    conn.close()
    print("SELESAI! Bank kosakata sudah terisi.")    

if __name__ == "__main__":
    build_massive_database()