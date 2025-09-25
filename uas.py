# manajemen toko rahayu
data_barang={}
data_jual={}
admin="1"
pw="1"
import os as s

def clear_screen():
    s.system('cls' if s.name == 'nt' else 'clear')

def login():
    while True:
        clear_screen()
        print("="*30)
        username = input("Masukkan username: ")
        print("="*30)
        password = input("Masukkan password: ")
        print("="*30)
        if username == admin and password == pw:
            print("Login berhasil")
            main()
            break
        else:
            print("Login gagal")
            input("Tekan Enter untuk mencoba lagi...")

def main():
    while True:
        clear_screen()
        print("\nMenu Utama")
        print("1. Kelola Barang")
        print("2. Kasir")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == "1":
            kelola_barang()
        elif pilihan == "2":
            kasir()
        elif pilihan == "3":
            clear_screen()
            print("Terima kasih telah menggunakan aplikasi ini")
            break
        else:
            print("Pilihan tidak tersedia")
            input("Tekan Enter untuk melanjutkan...")

def kelola_barang():
    while True:
        clear_screen()
        print("\nMenu Kelola Barang")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Update Barang")
        print("4. Lihat Barang")
        print("5. Kembali")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            update_barang()
        elif pilihan == "4":
            tampilkan_barang()
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak tersedia")
            input("Tekan Enter untuk melanjutkan...")

def kasir():
    while True:
        clear_screen()
        print("\nMenu Kasir")
        print("1. Tambah Barang Belanjaan")
        print("2. Lihat Barang Belanjaan")
        print("3. Hitung Total Belanjaan")
        print("4. Kembali")
        pilihan = input("Pilih menu (1/2/3/4): ")  
        if pilihan == "1":
            tambah_barang_belanja()
        elif pilihan == "2":
            lihat_barang_belanja()
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "3":
            hitung_total_belanja()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak tersedia")
            input("Tekan Enter untuk melanjutkan...")

def tambah_barang_belanja():
    clear_screen()
    if not data_barang:
        print("Tidak ada barang tersedia!")
        input("Tekan Enter untuk melanjutkan...")
        return
    tampilkan_barang()
    while True:
        nama_barang = input("Masukkan nama barang yang ingin dibeli: ")
        
        if nama_barang not in data_barang:
            print("Barang tidak tersedia!")
            continue
        
        if data_barang[nama_barang]["stock"] <= 0:
            print("Stok barang habis!")
            continue
        
        try:
            jumlah = int(input("Masukkan jumlah: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            
            if jumlah > data_barang[nama_barang]["stock"]:
                print(f"Stok tidak mencukupi! Stok tersedia: {data_barang[nama_barang]['stock']}")
                continue
            
            # Tambah ke keranjang belanja
            if nama_barang in data_jual:
                data_jual[nama_barang]["jumlah"] += jumlah
            else:
                data_jual[nama_barang] = {
                    "harga": data_barang[nama_barang]["harga"],
                    "jumlah": jumlah
                }
            
            print(f"{jumlah} {nama_barang} berhasil ditambahkan ke keranjang")
            
            val = input("Apakah ingin menambah barang lain? (y/n): ")
            if val.lower() != 'y':
                break
                
        except ValueError:
            print("Jumlah harus berupa angka!")

def lihat_barang_belanja():   
    clear_screen()
    if not data_jual:
        print("Keranjang belanja kosong!")
        return
    
    print("=" * 70)
    print(f"{'Nama Barang':<25}{'Harga':>15}{'Jumlah':>10}{'Subtotal':>15}")
    print("=" * 70)
    
    total = 0
    for nama_barang, detail in data_jual.items():
        subtotal = detail["harga"] * detail["jumlah"]
        total += subtotal
        print(f"{nama_barang:<25}{detail['harga']:>15,}{detail['jumlah']:>10}{subtotal:>15,}")
    
    print("=" * 70)
    print(f"{'Total':<50}{total:>15,}")
    print("=" * 70)

def hitung_total_belanja():    
    clear_screen()
    if not data_jual:
        print("Keranjang belanja kosong!")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    # Tampilkan barang belanja
    lihat_barang_belanja()
    
    # Hitung total
    total = sum(detail["harga"] * detail["jumlah"] for detail in data_jual.values())
    
    print(f"\nTotal belanja: Rp. {total:,}")
    
    while True:
        try:
            uang_bayar = int(input("Masukkan uang yang dibayarkan: Rp. "))
            if uang_bayar < total:
                print("Uang tidak mencukupi!")
                continue
            
            kembalian = uang_bayar - total
            
            # Kurangi stok barang
            for nama_barang, detail in data_jual.items():
                data_barang[nama_barang]["stock"] -= detail["jumlah"]
            
            # Tampilkan struk
            cetak_struk(total, uang_bayar, kembalian)
            
            # Reset keranjang belanja setelah transaksi selesai
            data_jual.clear()
            input("Tekan Enter untuk melanjutkan...")
            break
            
        except ValueError:
            print("Uang harus berupa angka!")

def cetak_struk(total, uang_bayar, kembalian):
    from datetime import datetime
    print("\n" + "="*50)
    print("                  TOKO RAHAYU")
    print("                 STRUK BELANJA")
    print("="*50)
    print(f"Tanggal: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-"*50)
    
    print(f"{'Barang':<20}{'Qty':>5}{'Harga':>10}{'Total':>10}")
    print("-"*50)
    
    for nama_barang, detail in data_jual.items():
        subtotal = detail["harga"] * detail["jumlah"]
        print(f"{nama_barang:<20}{detail['jumlah']:>5}{detail['harga']:>10,}{subtotal:>10,}")
    
    print("-"*50)
    print(f"{'Total':<35}{total:>10,}")
    print(f"{'Bayar':<35}{uang_bayar:>10,}")
    print(f"{'Kembalian':<35}{kembalian:>10,}")
    print("="*50)
    print("         Terima kasih atas kunjungan Anda!")
    print("                 TOKO RAHAYU")
    print("="*50)

def tambah_barang():
    clear_screen()
    while True:
        nama_barang = input("Masukkan nama barang: ")
        if nama_barang in data_barang:
            print("Barang sudah ada")
            print()
            continue    
        else:
            harga_barang = input("Masukkan harga barang: Rp. ")
            try:
                harga_barang = int(harga_barang)
            except ValueError:
                print("Harga harus berupa angka!")
                continue

            stock_barang = input("Masukkan stok barang: ")
            try:
                stock_barang = int(stock_barang)
                if stock_barang < 0:
                    print("Stok tidak boleh minus")
                    continue
            except ValueError:
                print("Stok harus berupa angka")
                continue
            data_barang[nama_barang] = {"harga": harga_barang, "stock": stock_barang}
            print("Barang berhasil ditambahkan")
            print()
            val = input("Apakah anda ingin menambahkan barang lain? (y/n): ")
            if val.lower() != 'y':
                break

def hapus_barang():
    clear_screen()
    if not data_barang:
        print("Tidak ada barang untuk dihapus!")
        input("Tekan Enter untuk melanjutkan...")
        return
        
    tampilkan_barang()
    while True:
        nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
        if nama_barang in data_barang:
            del data_barang[nama_barang]
            print("Barang berhasil dihapus")
            val = input("Apakah anda ingin menghapus barang lain? (y/n): ")
            if val.lower() != 'y':
                break
        else:
            print("Barang tidak ada")
            input("Tekan Enter untuk melanjutkan...")
            break

def update_barang():    
    clear_screen()
    if not data_barang:
        print("Tidak ada barang untuk diupdate!")
        input("Tekan Enter untuk melanjutkan...")
        return
        
    tampilkan_barang()
    while True:
        nama_barang = input("Masukkan nama barang yang ingin diupdate: ")
        if nama_barang in data_barang:
            while True:
                print("1. Update harga")
                print("2. Update Stock")
                val = input("Apa yang ingin diupdate? : ")
                if val == "1":
                    try:
                        harga_barang = int(input("Masukkan harga baru: Rp. "))
                        data_barang[nama_barang]["harga"] = harga_barang
                        print("Harga berhasil diupdate")
                        tampilkan_barang()
                        break
                    except ValueError:
                        print("Harga harus berupa angka!")
                elif val == "2":
                    try:
                        stock_barang = int(input("Masukkan stok baru: "))
                        if stock_barang < 0:
                            print("Stok tidak boleh minus")
                            continue
                        data_barang[nama_barang]["stock"] = stock_barang
                        print("Stok berhasil diupdate")
                        tampilkan_barang()
                        break
                    except ValueError:
                        print("Stok harus berupa angka!")
                else:
                    print("Pilihan tidak tersedia")
            
            val1 = input("Apakah anda ingin mengupdate barang lain? (y/n): ")
            if val1.lower() != 'y':
                break
        else:
            print("Barang tidak ada")
            input("Tekan Enter untuk melanjutkan...")
            break

def tampilkan_barang():
    if not data_barang:
        print("Tidak ada barang tersedia!")
        return
        
    print("=" * 60)
    print(f"{'Nama Barang':<25}{'Harga':>15}{'Stock':>15}")
    print("=" * 60)
    for nama_barang, detail_barang in data_barang.items():
        print(f"{nama_barang:<25}{detail_barang['harga']:>15,}{detail_barang['stock']:>15}")
    print("=" * 60)

login()