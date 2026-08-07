import nltk
from nltk.corpus import wordnet 

print("Memeriksa ketersediaan data WordNet...")
nltk.download('wordnet', quiet=True)

def cari_definisi_inggris(kata):
    kumpulan_makna = wordnet.synsets(kata)

    if not kumpulan_makna:
        return None

    semua_definisi = []
    for makna in kumpulan_makna:
        semua_definisi.append(makna.definition())
    return semua_definisi

if __name__ == "__main__":
    # daftar_kata = ["invisible", "griffin", "pharos", "serendipity"]
    # mengganti daftar kata yang terinput langsung dengan input teks

    kata_yang_dicari = input("Let's find the meaning of: ")
    print("\n=== CHECKING FROM WORDNET ===")

    daftar_definisi = cari_definisi_inggris(kata_yang_dicari)
    if daftar_definisi:
        print(f"Kata: {kata_yang_dicari.upper()}")
        # print(f"Definisi: {daftar_definisi}\n")

        for indeks, definisi in enumerate(daftar_definisi, 1):
            print(f"{indeks}. {definisi}")
        print()
    else:
        print(f"Kata: {kata_yang_dicari}")
        print("Definisi: Tidak ditemukan di WordNet.\n")