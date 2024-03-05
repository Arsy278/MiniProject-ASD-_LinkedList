from datetime import datetime
import os
from prettytable import PrettyTable

os.system('cls' if os.name == 'nt' else 'clear')

class Node:
    def __init__(self, nama_karyawan, waktu):
        self.nama_karyawan = nama_karyawan
        self.waktu = waktu
        self.next = None

class PendataanKehadiran:
    def __init__(self):
        self.head = None

    def lihatSemuaKehadiran(self):
        current = self.head
        if not current:
            print("Belum ada data kehadiran yang dicatat.")
            input("Tekan Enter untuk melanjutkan...")
            return
        nomor_awal = 1
        tabel = PrettyTable()
        tabel.field_names= ["No", "Nama Karyawan", "Tanggal"]
        while current:
            tabel.add_row([nomor_awal, current.nama_karyawan, current.waktu])
            nomor_awal += 1
            current = current.next
        print("\nDaftar Semua Kehadiran:")
        print(tabel)
        input("Tekan Enter untuk melanjutkan...")

    def perbaruiKehadiran(self, nama_karyawan, tanggal):
        current = self.head
        found = False
        while current:
            if current.nama_karyawan == nama_karyawan:
                current.waktu = tanggal
                print("\nAbsensi berhasil diperbarui!, berikut deskripsi absensi :")
                print("Nama Karyawan: ", current.nama_karyawan)
                print("Tanggal & Jam: ", current.waktu)
                found = True
                break
            current = current.next
        if not found:
            print("Karyawan tidak ditemukan dalam data kehadiran.")
        input("Tekan Enter untuk melanjutkan...")

    def tambahNodeDiAwal(self, nama_karyawan, tanggal):
        new_node = Node(nama_karyawan, tanggal)
        new_node.next = self.head
        self.head = new_node
        print(f"Data ditambahkan di awal.")

    def tambahNodeDiTengah(self, nama_karyawan, tanggal, posisi):
        if posisi <= 0:
            print("Index harus lebih besar dari 0.")
            return
        new_node = Node(nama_karyawan, tanggal)
        current = self.head
        count = 1
        while current and count < posisi:
            current = current.next
            count += 1
        if not current:
            print("Index melebihi panjang list.")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"Data ditambahkan di tengah.")

    def tambahNodeDiAkhir(self, nama_karyawan, tanggal):
        new_node = Node(nama_karyawan, tanggal)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def hapusNodeDiAwal(self):
        if not self.head:
            print("List sudah kosong.")
            return
        self.head = self.head.next
        print("Data dihapus di awal list.")
    def hapusNodeDiTengah(self, posisi):
        if not self.head:
            print("List sudah kosong.")
            return
        if posisi <= 0:
            print("Index harus lebih besar dari 0.")
            return
        current = self.head
        if posisi == 1:
            self.head = current.next
            return
        count = 1
        prev = None
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Index melebihi panjang list.")
            return
        prev.next = current.next

    def hapusNodeDiAkhir(self):
        if not self.head:
            print("List sudah kosong.")
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
        else:
            self.head = None
        print("Data terakhir pada list berhasil dihapus.")

pendataan = PendataanKehadiran()

def ambil_input():
    while True:
        nama_karyawan = input("Masukkan Nama: ")
        if nama_karyawan.isdigit():
            print("Data hanya boleh diisi oleh abjad, silahkan coba lagi.")
        else: 
            break
    tanggal = datetime.now().strftime("%d-%m-%Y")
    waktu = datetime.now().strftime("%H:%M:%S")
    print("\nAbsensi berhasil!, berikut deskripsi waktu absensi :")
    
    tabelAbsensi = PrettyTable()
    tabelAbsensi.field_names = ["Nama Karyawan", "Tanggal", "Waktu"]
    tabelAbsensi.add_row([nama_karyawan, tanggal, waktu])
    print(tabelAbsensi)
    return nama_karyawan, tanggal

def perbaruiAbsen():
    nama_karyawan = input("Masukkan nama karyawan yang ingin diubah: ")
    tanggal = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    return nama_karyawan, tanggal

while True:
    print(f"{'-'*40:^40}")
    print(f"{'Program Pendataan Kehadiran Karyawan':^40}")
    print(f"{'-'*40:^40}")
    print("Pilihan Menu:")
    print("1. Isi Absensi")
    print("2. Lihat Data Absensi")
    print("3. Perbarui Data Absensi")
    print("4. Hapus Absensi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == '1':
        opsi = input("Dimana data ingin ditaruh ? (Awal(a), Tengah(b), Akhir(c): ")
        if opsi in ['a', 'b', 'c']:
            if opsi == 'a':
                nama_karyawan, tanggal = ambil_input()
                pendataan.tambahNodeDiAwal(nama_karyawan, tanggal)
            elif opsi == 'b':
                posisi= int(input("Masukkan posisi(index) data: "))
                nama_karyawan, tanggal = ambil_input()
                pendataan.tambahNodeDiTengah(nama_karyawan, tanggal, posisi)
            elif opsi == 'c':
                nama_karyawan, tanggal = ambil_input()
                pendataan.tambahNodeDiAkhir(nama_karyawan, tanggal)
                print(f"Data ditambahkan di akhir.")
        else:
            print("Input tidak benar. Data tidak berhasil ditambahkan.")

    elif pilihan == '2':
        pendataan.lihatSemuaKehadiran()
    elif pilihan == '3':
        nama_karyawan, tanggal = perbaruiAbsen()
        pendataan.perbaruiKehadiran(nama_karyawan, tanggal)
    elif pilihan == '4':
        opsi = input("Data bagian mana yang ingin dihapus ? (Awal(a), Tengah(b), Akhir(c): ").lower()
        if opsi in ['a', 'b', 'c']:
            if opsi == 'a':
                pendataan.hapusNodeDiAwal()
            elif opsi == 'b':
                posisi = int(input("Masukkan posisi data yang akan dihapus: "))
                pendataan.hapusNodeDiTengah(posisi)
                print(f"Data dihapus pada posisi ke-{posisi}.")
            elif opsi == 'c':
                pendataan.hapusNodeDiAkhir()
        else:
            print("Input tidak valid. Node tidak dihapus.")
    elif pilihan == '5':
        print("┌───────────────────────────────────────────────┐")
        print("│                                               │")
        print("│        Terima kasih telah menggunakan         │")
        print("│                Program saya!                  │")
        print("│                                               │")
        print("│         Semoga harimu menyenangkan.           │")
        print("│                                               │")
        print("│                                      -arsy    │")
        print("└───────────────────────────────────────────────┘")

        break
    else:
        print("Input tidak valid. Silakan pilih menu yang sesuai.")