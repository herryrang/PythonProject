books = {
    "B001": {"judul": "Doraemon", "pengarang": "Fujiko F. Fujio", "jumlah": 10},
    "B002": {"judul": "Crayon Shinchan", "pengarang": "Yoshito Usui", "jumlah": 5}
}

def add_book():
    isbn = input("Masukkan ISBN buku: ")
    judul = input("Masukkan judul buku: ")
    pengarang = input("Masukkan pengarang: ")
    jumlah = int(input("Masukkan jumlah buku: "))
    books[isbn] = {"judul": judul, "pengarang": pengarang, "jumlah": jumlah}
    print("Buku berhasil ditambahkan!")

def display_book():
    for isbn, book in books.items():
        print(f"ISBN: {isbn}, Judul: {book['judul']}, Pengarang: {book['pengarang']}, Jumlah: {book['jumlah']}")

def search_book():
    judul = input("Masukkan judul buku yang ingin dicari: ")
    for isbn, book in books.items():
        if judul.lower() in book["judul"].lower():
            print(f"ISBN: {isbn}, Judul: {book['judul']}, Pengarang: {book['pengarang']}, Jumlah: {book['jumlah']}")

def update_book():
    isbn = input("Masukkan ISBN buku yang ingin diperbarui: ")
    if isbn in books:
        print("Data buku saat ini:")
        print(books[isbn])

        judul_baru = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
        pengarang_baru = input("Masukkan pengarang baru (kosongkan jika tidak ingin mengubah): ")
        jumlah_baru = input("Masukkan jumlah buku baru (kosongkan jika tidak ingin mengubah): ")

        if judul_baru:
            books[isbn]["judul"] = judul_baru
        if pengarang_baru:
            books[isbn]["pengarang"] = pengarang_baru
        if jumlah_baru:
            books[isbn]["jumlah"] = int(jumlah_baru)            

def delete_book():
    isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
    if isbn in books:
        del books[isbn]
        print("Buku berhasil dihapus!")
    else:
        print("Buku dengan ISBN tersebut tidak ditemukan.")


while True:
    print("\nMenu Sistem Informasi Perpustakaan:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Tampilkan Buku")
    print("4. Update Buku")
    print("5. Hapus Buku")

    # ... (pilihan menu lainnya)
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        add_book()
    elif pilihan == "2":
        search_book()
    elif pilihan == "3":
        display_book()
    elif pilihan == "4":
        update_book()
    elif pilihan == "5":
        delete_book()

    









