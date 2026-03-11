import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

# Daftar barang aksesoris lari (brand & harga berbeda)
DAFTAR_BARANG = [   
    ("Sepatu Nike Air Zoom", 1500000),
    ("Sepatu Adidas Ultraboost", 1800000),
    ("Sepatu New Balance 1080", 1700000),
    ("Kaos Nike Dri-FIT", 350000),
    ("Kaos Adidas Aeroready", 320000),
    ("Kaos New Balance Run", 300000),
    ("Topi Nike Featherlight", 200000),
    ("Topi Adidas Running", 180000),
    ("Celana Nike Challenger", 400000),
    ("Celana Adidas Own The Run", 380000)
]

percobaan_login = 0

def show_kasir_window():
    login_window.destroy()

    def update_harga(event=None):
        idx = combo_barang.current()
        if idx >= 0:
            entry_harga.config(state="normal")
            entry_harga.delete(0, tk.END)
            entry_harga.insert(0, str(DAFTAR_BARANG[idx][1]))
            entry_harga.config(state="readonly")

    def hitung_total():
        nama = entry_nama.get()
        barang_idx = combo_barang.current()
        if barang_idx == -1:
            messagebox.showerror("Error", "Pilih barang terlebih dahulu!")
            return
        barang, harga = DAFTAR_BARANG[barang_idx]
        try:
            jumlah = int(entry_jumlah.get())
            bayar = int(entry_bayar.get())
        except ValueError:
            messagebox.showerror("Error", "Jumlah dan uang harus berupa angka!")
            return
        total = jumlah * harga
        kembali = bayar - total

        struk = (
            f"Nama Pembeli : {nama}\n"
            f"{'-'*35}\n"
            f"Nama Barang  : {barang}\n"
            f"Harga Satuan : Rp. {harga}\n"
            f"Jumlah Barang: {jumlah}\n"
            f"{'-'*35}\n"
            f"Total        : Rp. {total}\n"
            f"Tunai        : Rp. {bayar}\n"
            f"Kembali      : Rp. {kembali}\n"
            f"{'-'*35}\n"
            f"\nTerima Kasih Telah Berbelanja!!"
        )
        messagebox.showinfo("Invoice", struk)

    root = tk.Tk()
    root.title("Kasir Aksesoris Lari")
    root.geometry("440x540")
    root.configure(bg="#f0f4f8")

    # Frame utama
    frame = tk.Frame(root, bg="#f0f4f8")
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Nama Pembeli
    tk.Label(frame, text="Nama Pembeli:", bg="#f0f4f8").grid(row=0, column=0, sticky="w", pady=5)
    entry_nama = tk.Entry(frame, width=25)
    entry_nama.grid(row=0, column=1, pady=5, sticky="ew")

    # Pilih Barang
    tk.Label(frame, text="Nama Barang:", bg="#f0f4f8").grid(row=1, column=0, sticky="w", pady=5)
    combo_barang = ttk.Combobox(frame, values=[f"{b[0]} (Rp. {b[1]})" for b in DAFTAR_BARANG], state="readonly", width=30)
    combo_barang.grid(row=1, column=1, pady=5, sticky="ew")
    combo_barang.bind("<<ComboboxSelected>>", update_harga)

    # Harga (otomatis)
    tk.Label(frame, text="Harga Satuan:", bg="#f0f4f8").grid(row=2, column=0, sticky="w", pady=5)
    entry_harga = tk.Entry(frame, width=25, state="readonly")
    entry_harga.grid(row=2, column=1, pady=5, sticky="ew")

    # Jumlah Produk
    tk.Label(frame, text="Jumlah Produk:", bg="#f0f4f8").grid(row=3, column=0, sticky="w", pady=5)
    entry_jumlah = tk.Entry(frame, width=25)
    entry_jumlah.grid(row=3, column=1, pady=5, sticky="ew")

    # Uang Pembeli
    tk.Label(frame, text="Uang Pembeli:", bg="#f0f4f8").grid(row=4, column=0, sticky="w", pady=5)
    entry_bayar = tk.Entry(frame, width=25)
    entry_bayar.grid(row=4, column=1, pady=5, sticky="ew")

    # Tombol Total
    tk.Button(frame, text="Hitung Total", command=hitung_total, bg="#4caf50", fg="white", width=20).grid(row=5, column=0, columnspan=2, pady=15)

    # Daftar Barang (Tabel)
    tabel_frame = tk.LabelFrame(frame, text="Daftar Barang & Harga", bg="#f0f4f8")
    tabel_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")
    for i, (nama, harga) in enumerate(DAFTAR_BARANG):
        tk.Label(tabel_frame, text=f"{i+1}. {nama}", width=28, anchor="w", bg="#f0f4f8").grid(row=i, column=0, sticky="w")
        tk.Label(tabel_frame, text=f"Rp. {harga}", width=14, anchor="e", bg="#f0f4f8").grid(row=i, column=1, sticky="e")

    frame.columnconfigure(1, weight=1)
    root.mainloop()

# Fungsi untuk login dengan batas 3x percobaan
def login():
    global percobaan_login
    username = entry_user.get()
    password = entry_pass.get()
    if username == "1" and password == "1":
        show_kasir_window()
    else:
        percobaan_login += 1
        if percobaan_login >= 3:
            messagebox.showerror("Login Gagal", "Percobaan login melebihi 3 kali. Program akan keluar.")
            login_window.destroy()
        else:
            messagebox.showerror("Login Gagal", f"Username atau Password salah!\nPercobaan ke-{percobaan_login} dari 3.")

# Window login
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("340x200")
login_window.configure(bg="#f0f4f8")

tk.Label(login_window, text="Username", bg="#f0f4f8").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_user = tk.Entry(login_window)
entry_user.grid(row=1, column=1, padx=10, pady=10)

tk.Label(login_window, text="Password", bg="#f0f4f8").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_pass = tk.Entry(login_window, show="*")
entry_pass.grid(row=2, column=1, padx=10, pady=10)

tk.Button(login_window, text="Login", command=login, bg="#2196f3", fg="white", width=15).grid(row=3, column=0, columnspan=2, pady=15)

login_window.mainloop()
