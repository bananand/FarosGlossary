import nltk
from nltk.corpus import wordnet 

print("Memeriksa ketersediaan data WordNet...")
nltk.download('wordnet', quiet=True)

def cari_definisi_inggris(kata):
    kumpulan_makna = wordnet.synsets(kata)

    if not kumpulan_makna:
        return None
    return kumpulan_makna[0].definition()

if __name__ == "__main__":
    # daftar_kata = ["invisible", "griffin", "pharos", "serendipity"]
    # mengganti daftar kata yang terinput langsung dengan input teks

    kata_yang_dicari = input("Let's find the meaning of: ")
    print("\n=== CHECKING FROM WORDNET ===")
    definisi = cari_definisi_inggris(kata_yang_dicari)
    if definisi:
        print(f"Kata: {kata_yang_dicari}")
        print(f"Definisi: {definisi}\n")
    else:
        print(f"Kata: {kata_yang_dicari}")
        print("Definisi: Tidak ditemukan di WordNet.\n")