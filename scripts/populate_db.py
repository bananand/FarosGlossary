import sqlite3
from nltk.corpus import wordnet

def build_massive_database():
    conn = sqlite3.connect("src/kamus.db")
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS bank_kata_inggris')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank_kata_inggris (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kata TEXT,
            definisi_en TEXT,
            terjemahan_id TEXT
    )
''')

    print("Memulai pengambilan kata dari wordnet...")
    semua_kata = list(wordnet.words())
    print(f"Berhasil mengambil {len(semua_kata)} kata dari WordNet.")

    data_kata_siap_masuk = []

    for kata in semua_kata:
        synsets = wordnet.synsets(kata)
        for synset in synsets:
            definisi = synset.definition()
            kata_terformat = kata.replace('_', ' ') #wordnet pakai underscore buat frasa
            data_kata_siap_masuk.append((kata_terformat, definisi, ""))
    print(f"Memasukkan {len(data_kata_siap_masuk)} kata ke database.")     

    cursor.executemany('''
        INSERT OR IGNORE INTO bank_kata_inggris (kata, definisi_en, terjemahan_id)
        VALUES (?, ?, ?)
    ''', data_kata_siap_masuk)

    conn.commit()
    conn.close()

    print("SELESAI!, bank kosakata bahasa inggris telah terisi")

if __name__ == "__main__":
    build_massive_database()