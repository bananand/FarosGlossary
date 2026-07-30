import sqlite3 
import csv
import os

def buat_database():
    csv_path = os.path.join("data", "sampel.csv") #join bisa menerima banyak argumen
    db_path = os.path.join("src", "kamus.db")

    if not os.path.exists(csv_path):
        print(f"Error: File {csv_path} tidak ditemukan!")
        return

    print("Menyiapkan database FarosGlossary...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kata_klasik (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kata TEXT NOT NULL,
            definisi_inggris TEXT,
            terjemahan_indonesia TEXT
        )
    ''')#urutan tata bahasa sqlite: Type, Constraint, extra modifier

    #Kosongin tabel jika skrip reload/berjalan ulang
    cursor.execute('DELETE FROM kata_klasik')

    print("Membaca data dari sampel.csv...") #pastikan sampel.csv memuat kata x,x,x (jangan ada spasi)
    with open(csv_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file) #ubah csv ke bentuk dictionary python; key ada di baris pertama makanya jangan dispasiin stlh koma

        for baris in csv_reader: #parameterized query
            cursor.execute(''' 
                INSERT INTO kata_klasik (kata, definisi_inggris, terjemahan_indonesia)
                VALUES (?, ?, ?)
            ''', (baris['kata'], baris['definisi_inggris'], baris['terjemahan_indonesia']))

    #simpan perubahan dan menutup koneksi        
    conn.commit()
    conn.close()
    print(f"Database FarosGlossary berhasil dibuat di: {db_path}")

if __name__ == "__main__":
        buat_database()