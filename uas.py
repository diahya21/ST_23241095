# Program untuk mensimulasikan sistem keranjang belanja

# Inisialisasi keranjang belanja
keranjang = []

# Inisialisasi total biaya
total_biaya = 0

# Loop sampai pengguna memutuskan untuk checkout
while True:
    # Tampilkan menu
    print("===Sistem Keranjang Belanja===")
    print("1. Tambahkan item ke keranjang")
    print("2. Hapus item dari keranjang")
    print("3. Lihat keranjang")
    print("4. Checkout")

    # Dapatkan pilihan pengguna
    pilihan = input("Masukkan pilihan Anda: ")

    # Tambahkan item ke keranjang
    if pilihan == "1":
        nama_item = input("Masukkan nama item: ")
        harga_item = int(input("Masukkan harga item: "))
        keranjang.append({"nama": nama_item, "harga": harga_item})
        print(f"Menambahkan {nama_item} ke keranjang")

    # Hapus item dari keranjang
    elif pilihan == "2":
        if len(keranjang) == 0:
            print("Keranjang kosong")
        else:
            nama_item = input("Masukkan nama item untuk dihapus: ")
            for item in keranjang:
                if item["nama"] == nama_item:
                    keranjang.remove(item)
                    print(f"Item {nama_item} dihapus dari keranjang")
                    break
            else:
                print(f"{nama_item} tidak ditemukan di keranjang")

    # Lihat keranjang
    elif pilihan == "3":
        if len(keranjang) == 0:
            print("Keranjang kosong")
        else:
            print("Isi keranjang:")
            for item in keranjang:
                print(f"{item['nama']}: {item['harga']}")

    # Checkout
    elif pilihan == "4":
        if len(keranjang) == 0:
            print("Keranjang kosong")
        else:
            print("Checkout:")
            for item in keranjang:
                total_biaya += item["harga"]
            print(f"Total biaya: {total_biaya:.2f}")
            print("Terima kasih telah berbelanja!")
            break

    # Pilihan tidak valid
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")