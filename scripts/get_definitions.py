import sqlite3

def cari_kata_kamus(kata):
    conn = sqlite3.connect("src/kamus.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT definisi_en, terjemahan
        FROM bank_kata_inggris
        WHERE kata = ?
''', [kata.lower()]) #sqlite hanya nerima data dalam bentuk tuple/list, makanya harus dibungkus pake list di sini

    hasil = cursor.fetchall()
    conn.close()
    return hasil

if __name__ == "__main__":
    kata_yang_dicari = input("Let's find the meaning of: ")
    print(f"Searching for '{kata_yang_dicari.upper()}'")

    daftar_makna = cari_kata_kamus(kata_yang_dicari)

    if daftar_makna:
        for indeks, (definisi, terjemahan) in enumerate(daftar_makna, 1):
            teks_terjemahan = terjemahan if terjemahan else "No Indonesian translation found in database library."

            print(f" [EN]  {indeks}. {definisi}")
            print(f" [ID]  {indeks}. {teks_terjemahan}\n")
    else:
        print(f"Sorry, the word '{kata_yang_dicari.upper()}' is not found in the database library.")      

