import sqlite3
import nltk
from nltk.corpus import wordnet

print("Memeriksa data WordNet multibahasa (OMW)...")
nltk.download('omw-2.0', quiet=True)
nltk.download('omw')

def build_massive_database():
    conn = sqlite3.connect("src/kamus.db")
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS bank_kata_inggris')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank_kata_inggris (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kata TEXT,
            definisi_en TEXT,
            terjemahan TEXT,
            UNIQUE(kata, definisi_en)
    )
''') #UNIQUE(kata, definisi_en) berguna untuk membuat kombinasi unik 1 kosakata inggris dengan definisi miliknya sendiri

    print("Mengekstrak kata. definisi, terjemahan..")
    print("Memulai pengambilan kata dari wordnet...")
    semua_kata = list(wordnet.words())
    
    data_kata_siap_masuk = []

    for kata in semua_kata:
        synsets = wordnet.synsets(kata)
        kata_terformat = kata.replace('_', ' ') #wordnet pakai underscore buat frasa

        for synset in synsets:
            definisi = synset.definition()

            daftar_indo = synset.lemma_names('ind')
            #list comprehension python
            terjemahan_bersih = ", ".join([indo.replace('_', ' ') for indo in daftar_indo])

            data_kata_siap_masuk.append((kata_terformat, definisi, terjemahan_bersih))
    print(f"Memasukkan {len(data_kata_siap_masuk)} kata ke database.")     

    cursor.executemany('''
        INSERT OR IGNORE INTO bank_kata_inggris (kata, definisi_en, terjemahan)
        VALUES (?, ?, ?)
    ''', data_kata_siap_masuk)

    conn.commit()
    conn.close()

    print("SELESAI!, bank kosakata bahasa inggris dan terjemahan indonesia telah terisi")

if __name__ == "__main__":
    build_massive_database()