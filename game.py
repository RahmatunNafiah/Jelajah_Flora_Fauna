import random
import sys

# =======================================
# DATA 38 PROVINSI
# =======================================
data_provinsi = {
    "Aceh": [
        {"nama": "Badak Sumatera", "jenis": "Fauna", "ciri": "Memiliki dua cula pendek dan tubuh coklat kemerahan.",
         "fakta": "Badak Sumatera adalah badak paling kecil di dunia."},
        {"nama": "Bunga Jeumpa", "jenis": "Flora", "ciri": "Bunga kuning harum, simbol Aceh.",
         "fakta": "Dipakai dalam upacara adat Aceh."}
    ],

    "Sumatera Utara": [
        {"nama": "Orangutan Tapanuli", "jenis": "Fauna", "ciri": "Rambut coklat dengan wajah unik.",
         "fakta": "Spesies orangutan terbaru yang ditemukan pada 2017."},
        {"nama": "Amorphophallus Titanum", "jenis": "Flora", "ciri": "Bunga raksasa berbau busuk.",
         "fakta": "Termasuk bunga dengan bau busuk paling kuat di dunia."}
    ],

    "Sumatera Barat": [
        {"nama": "Kucing Emas", "jenis": "Fauna", "ciri": "Tubuh keemasan, sulit ditemui.",
         "fakta": "Termasuk kucing liar paling langka."},
        {"nama": "Pohon Surian", "jenis": "Flora", "ciri": "Pohon besar berkualitas tinggi.",
         "fakta": "Dijuluki mahoni Indonesia."}
    ],

    "Riau": [
        {"nama": "Gajah Sumatera", "jenis": "Fauna", "ciri": "Lebih kecil dari gajah Asia.",
         "fakta": "Sangat terancam akibat penyusutan habitat."},
        {"nama": "Sagu", "jenis": "Flora", "ciri": "Menghasilkan pati dari batang.",
         "fakta": "Makanan pokok masyarakat Riau."}
    ],

    "Kepulauan Riau": [
        {"nama": "Dugong (Duyung)", "jenis": "Fauna", "ciri": "Mamalia laut pemakan lamun.",
         "fakta": "Menginspirasi legenda putri duyung."},
        {"nama": "Bakau", "jenis": "Flora", "ciri": "Tumbuh di air payau.",
         "fakta": "Akar bakau menahan abrasi pantai."}
    ],

    "Jambi": [
        {"nama": "Harimau Sumatera", "jenis": "Fauna", "ciri": "Loreng rapat, tubuh kecil.",
         "fakta": "Sangat kritis populasinya."},
        {"nama": "Temulawak", "jenis": "Flora", "ciri": "Rimpang besar berkhasiat.",
         "fakta": "Obat tradisional masyarakat Jambi."}
    ],

    "Sumatera Selatan": [
        {"nama": "Buaya Muara", "jenis": "Fauna", "ciri": "Reptil besar dengan rahang kuat.",
         "fakta": "Buaya terbesar di dunia."},
        {"nama": "Duku Palembang", "jenis": "Flora", "ciri": "Buah manis kulit tipis.",
         "fakta": "Varietas duku paling terkenal di Indonesia."}
    ],

    "Bangka Belitung": [
        {"nama": "Burung Pelatuk", "jenis": "Fauna", "ciri": "Paruh kuat untuk mematuk kayu.",
         "fakta": "Sering di hutan pulau timah."},
        {"nama": "Ketapang", "jenis": "Flora", "ciri": "Daun lebar bertingkat.",
         "fakta": "Daunnya dipakai untuk aquascape."}
    ],

    "Bengkulu": [
        {"nama": "Beruang Madu", "jenis": "Fauna", "ciri": "Tanda bulan sabit di dada.",
         "fakta": "Beruang terkecil di dunia."},
        {"nama": "Rafflesia Arnoldii", "jenis": "Flora", "ciri": "Bunga terbesar di dunia.",
         "fakta": "Bengkulu adalah pusat habitatnya."}
    ],

    "Lampung": [
        {"nama": "Gajah Lampung", "jenis": "Fauna", "ciri": "Hidup di Way Kambas.",
         "fakta": "Terancam akibat konflik manusia–satwa."},
        {"nama": "Kopi Lampung", "jenis": "Flora", "ciri": "Aromatik dan pekat.",
         "fakta": "Termasuk kopi robusta terbaik Indonesia."}
    ],

    # =====================
    # JAWA
    # =====================
    "DKI Jakarta": [
        {"nama": "Lutung", "jenis": "Fauna", "ciri": "Primata hitam pekat.",
         "fakta": "Habitat tersisa di hutan kota Jakarta."},
        {"nama": "Angsana", "jenis": "Flora", "ciri": "Peneduh dengan bunga kuning.",
         "fakta": "Banyak ditanam sebagai penghijauan."}
    ],

    "Banten": [
        {"nama": "Badak Jawa", "jenis": "Fauna", "ciri": "Satu cula, sangat langka.",
         "fakta": "Hanya tersisa di Ujung Kulon."},
        {"nama": "Kemenyan", "jenis": "Flora", "ciri": "Penghasil getah aromatik.",
         "fakta": "Dipakai untuk parfum dan ritual."}
    ],

    "Jawa Barat": [
        {"nama": "Macan Tutul Jawa", "jenis": "Fauna", "ciri": "Titik hitam rapat.",
         "fakta": "Kucing besar endemik Jawa."},
        {"nama": "Patrakomala", "jenis": "Flora", "ciri": "Bunga ungu lembut.",
         "fakta": "Puspa resmi Jawa Barat."}
    ],

    "Jawa Tengah": [
        {"nama": "Kukang Jawa", "jenis": "Fauna", "ciri": "Primata bermata besar.",
         "fakta": "Sering diperdagangkan ilegal."},
        {"nama": "Jambu Mete", "jenis": "Flora", "ciri": "Memiliki kacang mete.",
         "fakta": "Masuk Indonesia pada abad ke-16."}
    ],

    "DI Yogyakarta": [
        {"nama": "Ayam Ketawa", "jenis": "Fauna", "ciri": "Suara seperti tertawa.",
         "fakta": "Sering dilombakan."},
        {"nama": "Pohon Gayam", "jenis": "Flora", "ciri": "Daun lebar, buah keras.",
         "fakta": "Melambangkan keteduhan kraton."}
    ],

    "Jawa Timur": [
        {"nama": "Lumba-Lumba", "jenis": "Fauna", "ciri": "Mamalia laut cerdas.",
         "fakta": "Banyak di Teluk Kiluan."},
        {"nama": "Tebu", "jenis": "Flora", "ciri": "Batang manis penghasil gula.",
         "fakta": "Jatim adalah produsen gula terbesar Indonesia."}
    ],

    # =====================
    # BALI – NTT – NTB
    # =====================
    "Bali": [
        {"nama": "Rusa Bali", "jenis": "Fauna", "ciri": "Tubuh ramping coklat.",
         "fakta": "Maskot provinsi Bali."},
        {"nama": "Jepun", "jenis": "Flora", "ciri": "Bunga harum putih/kuning.",
         "fakta": "Dipakai dalam upacara adat Bali."}
    ],

    "Nusa Tenggara Barat (NTB)": [
        {"nama": "Sapi Bali", "jenis": "Fauna", "ciri": "Tubuh merah kecoklatan.",
         "fakta": "Ras sapi lokal unggulan."},
        {"nama": "Bunga Gosang", "jenis": "Flora", "ciri": "Merah cerah.",
         "fakta": "Banyak tumbuh di Lombok."}
    ],

    "Nusa Tenggara Timur (NTT)": [
        {"nama": "Komodo", "jenis": "Fauna", "ciri": "Kadal terbesar di dunia.",
         "fakta": "Hanya ada di NTT."},
        {"nama": "Lontar", "jenis": "Flora", "ciri": "Palem yang tahan kering.",
         "fakta": "Daunnya dipakai untuk tenun tradisional."}
    ],

    # =====================
    # KALIMANTAN
    # =====================
    "Kalimantan Barat": [
        {"nama": "Bekantan", "jenis": "Fauna", "ciri": "Hidung panjang.",
         "fakta": "Maskot Kalimantan Barat."},
        {"nama": "Belian (Ulin)", "jenis": "Flora", "ciri": "Kayu sangat keras.",
         "fakta": "Disebut kayu besi."}
    ],

    "Kalimantan Tengah": [
        {"nama": "Enggang", "jenis": "Fauna", "ciri": "Paruh panjang bertanduk.",
         "fakta": "Simbol budaya Dayak."},
        {"nama": "Rotan", "jenis": "Flora", "ciri": "Merambat panjang kuat.",
         "fakta": "Bahan kerajinan Dayak."}
    ],

    "Kalimantan Selatan": [
        {"nama": "Pesut Mahakam", "jenis": "Fauna", "ciri": "Lumba-lumba air tawar.",
         "fakta": "Hanya ada di Sungai Mahakam."},
        {"nama": "Kasturi", "jenis": "Flora", "ciri": "Buah ungu kecil.",
         "fakta": "Endemik Kalimantan Selatan."}
    ],

    "Kalimantan Timur": [
        {"nama": "Beruang Madu", "jenis": "Fauna", "ciri": "Bulu hitam dengan dada terang.",
         "fakta": "Sangat terancam."},
        {"nama": "Meranti", "jenis": "Flora", "ciri": "Pohon kayu bangunan utama.",
         "fakta": "Banyak di hutan Kalimantan Timur."}
    ],

    "Kalimantan Utara": [
        {"nama": "Kucing Merah Borneo", "jenis": "Fauna", "ciri": "Tubuh kemerahan kecil.",
         "fakta": "Sangat langka."},
        {"nama": "Keruing", "jenis": "Flora", "ciri": "Kayu besar penghasil resin.",
         "fakta": "Untuk kapal dan konstruksi berat."}
    ],

    # =====================
    # SULAWESI
    # =====================
    "Sulawesi Utara": [
        {"nama": "Tarsius", "jenis": "Fauna", "ciri": "Mata besar, aktif malam.",
         "fakta": "Primata terkecil di dunia."},
        {"nama": "Cempaka", "jenis": "Flora", "ciri": "Bunga harum.",
         "fakta": "Dipakai dalam ritual Minahasa."}
    ],

    "Sulawesi Tengah": [
        {"nama": "Anoa", "jenis": "Fauna", "ciri": "Kerbau kecil hitam.",
         "fakta": "Endemik Sulawesi."},
        {"nama": "Gofasa", "jenis": "Flora", "ciri": "Kayu keras.",
         "fakta": "Dipakai membuat perahu tradisional."}
    ],

    "Sulawesi Selatan": [
        {"nama": "Maleo", "jenis": "Fauna", "ciri": "Bertelur besar.",
         "fakta": "Telurnya menetas oleh panas bumi."},
        {"nama": "Lontara", "jenis": "Flora", "ciri": "Daun kuat.",
         "fakta": "Dipakai menulis aksara Lontara."}
    ],

    "Sulawesi Tenggara": [
        {"nama": "Kuskus Beruang", "jenis": "Fauna", "ciri": "Bulu lebat.",
         "fakta": "Hidup di hutan tropis Sulawesi."},
        {"nama": "Jati", "jenis": "Flora", "ciri": "Kayu berkualitas tinggi.",
         "fakta": "Banyak ditanam masyarakat."}
    ],

    "Gorontalo": [
        {"nama": "Hiu Paus", "jenis": "Fauna", "ciri": "Ikan terbesar dunia.",
         "fakta": "Ada di Teluk Tomini."},
        {"nama": "Cempedak", "jenis": "Flora", "ciri": "Mirip nangka.",
         "fakta": "Buah favorit masyarakat."}
    ],

    "Sulawesi Barat": [
        {"nama": "Kupu-Kupu Morpho", "jenis": "Fauna", "ciri": "Sayap biru metalik.",
         "fakta": "Sangat indah."},
        {"nama": "Bitti", "jenis": "Flora", "ciri": "Kayu kuat.",
         "fakta": "Bahan kapal Pinisi."}
    ],

    # =====================
    # MALUKU
    # =====================
    "Maluku": [
        {"nama": "Kakatua Putih", "jenis": "Fauna", "ciri": "Bulu putih jambul besar.",
         "fakta": "Endemik Maluku."},
        {"nama": "Pala", "jenis": "Flora", "ciri": "Rempah harum kuat.",
         "fakta": "Membuat Maluku terkenal sebagai pulau rempah."}
    ],

    "Maluku Utara": [
        {"nama": "Kakatua Seram", "jenis": "Fauna", "ciri": "Bergaya lincah.",
         "fakta": "Maskot Maluku Utara."},
        {"nama": "Cengkeh", "jenis": "Flora", "ciri": "Rempah kecil.",
         "fakta": "Sempat jadi rebutan kolonial."}
    ],

    # =====================
    # PAPUA (6 PROVINSI)
    # =====================
    "Papua": [
        {"nama": "Cenderawasih", "jenis": "Fauna", "ciri": "Bulu cerah menawan.",
         "fakta": "Disebut burung surga."},
        {"nama": "Buah Merah", "jenis": "Flora", "ciri": "Merah panjang.",
         "fakta": "Obat tradisional kuat."}
    ],

    "Papua Barat": [
        {"nama": "Kura-kura Leher Ular", "jenis": "Fauna", "ciri": "Leher panjang.",
         "fakta": "Langka dan unik."},
        {"nama": "Anggrek Hitam", "jenis": "Flora", "ciri": "Kelopak ungu kehitaman.",
         "fakta": "Anggrek sangat langka."}
    ],

    "Papua Barat Daya": [
        {"nama": "Mambruk", "jenis": "Fauna", "ciri": "Mahkota bulu indah.",
         "fakta": "Mirip merpati raksasa."},
        {"nama": "Sagu", "jenis": "Flora", "ciri": "Penghasil pati.",
         "fakta": "Makanan pokok masyarakat Papua."}
    ],

    "Papua Tengah": [
        {"nama": "Kanguru Pohon", "jenis": "Fauna", "ciri": "Kanguru arboreal.",
         "fakta": "Tidak hidup di tanah."},
        {"nama": "Matoa", "jenis": "Flora", "ciri": "Buah manis beraroma unik.",
         "fakta": "Berbuah setahun sekali."}
    ],

    "Papua Pegunungan": [
        {"nama": "Kasuari", "jenis": "Fauna", "ciri": "Burung besar agresif.",
         "fakta": "Sering menjaga wilayahnya."},
        {"nama": "Nothofagus", "jenis": "Flora", "ciri": "Flora dataran tinggi.",
         "fakta": "Termasuk tanaman purba."}
    ],

    "Papua Selatan": [
        {"nama": "Buaya Air Tawar", "jenis": "Fauna", "ciri": "Lebih kecil dari buaya muara.",
         "fakta": "Umum di rawa selatan Papua."},
        {"nama": "Sagu Rumbia", "jenis": "Flora", "ciri": "Penghasil sagu utama.",
         "fakta": "Makanan pokok masyarakat selatan."}
    ],
}

# =======================================
# GLOBAL SKOR
# =======================================
skor = 0

# =======================================
# FUNGSI GAME
# =======================================

def tampilkan_menu():
    print("\n==== GAME EDUKASI FLORA & FAUNA INDONESIA ====")
    print("1. Main Quiz")
    print("2. Jelajah Provinsi")
    print("3. Lihat Skor")
    print("4. Keluar")
    return input("Pilih menu: ")

def quiz():
    global skor
    semua = []

    # Gabungkan semua data flora + fauna menjadi 1 list
    for prov in data_provinsi.values():
        semua.extend(prov)

    soal = random.choice(semua)
    print("\n==== QUIZ ====")
    print("Jenis :", soal["jenis"])
    print("Ciri  :", soal["ciri"])
    jawab = input("Apa nama flora/fauna ini? : ")

    if jawab.lower() == soal["nama"].lower():
        print("Benar! +10 poin")
        skor += 10
    else:
        print(f"Salah! Jawaban benar: {soal['nama']}")
        skor -= 5
        print("Fakta tambahan:", soal["fakta"])

def jelajah():
    print("\n==== JELAJAH PROVINSI ====")
    for i, prov in enumerate(data_provinsi.keys(), start=1):
        print(f"{i}. {prov}")

    pilih = input("Pilih provinsi (nomor): ")
    
    if not pilih.isdigit() or int(pilih) not in range(1, len(data_provinsi)+1):
        print("Pilihan tidak valid.")
        return

    provinsi = list(data_provinsi.keys())[int(pilih)-1]
    print(f"\n=== {provinsi} ===")

    for item in data_provinsi[provinsi]:
        print(f"- {item['nama']} ({item['jenis']})")
        print(f"  Ciri : {item['ciri']}")
        print(f"  Fakta: {item['fakta']}\n")

def lihat_skor():
    print(f"\nSkor kamu saat ini: {skor}\n")

# =======================================
# MAIN LOOP
# =======================================
while True:
    pilih = tampilkan_menu()

    if pilih == "1":
        quiz()
    elif pilih == "2":
        jelajah()
    elif pilih == "3":
        lihat_skor()
    elif pilih == "4":
        print("Terima kasih sudah bermain!")
        sys.exit()
    else:
        print("Pilihan tidak dikenal.")
