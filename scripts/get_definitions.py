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
    daftar_kata = ["invisible", "griffin", "pharos", "serendipity"]

    print("\n=== MENGAMBIL DEFINISI DARI WORDNET ===")
    for k in daftar_kata:
        definisi = cari_definisi_inggris(k)
        if definisi:
            print(f"Kata: {k}")
            print(f"Definisi: {definisi}\n")
        else:
            print(f"Kata: {k}")
            print("Definisi: Tidak ditemukan di WordNet.\n")