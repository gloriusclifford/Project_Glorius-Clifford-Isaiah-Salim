print ("=========================== Login dan Buat Daftar Jadwal Pelajaran ===========================")
print ("")

jadwal_pelajaran = {
    "Senin"     : ["Upacara","PJOK", "B.INDO", "PAI"],
    "Selasa"    : ["P5.2", "Sentra","PPKN", "K3LH",], 
    "Rabu"      : ["IPAS","P5.1", "Menpro", "BK"],
    "Kamis"     : ["Sejarah", "PBO","SENBUD", "PEMDAS",],
    "Jumat"     : ["Informatika","Matematika", "B.Ingrris"],
}

USERNAME = "PRAKTEK"
PASSWORD = "PEMDAS"


def login ():
    while True:
        max_attempts = 3
        attempts = 0
        
        while attempts < max_attempts:
            print ("=======================================")
            username = input ("Masukan Nama Anda        : ")
            password = input ("Masukan Password anda    : ")
            
            if username == USERNAME and password == PASSWORD:
                print ("SELAMAT LOGIN ANDA BERHASIL")
                return True
            else:
                print ("Username atau Password Salah, Silahkan Coba lagi")
                attempts += 1
        
        print ("ANDA TERLALU BANYAK MENCOBA")
        return False
    

if login():
    while True:
        print ("================================ Menu Utama ================================")
        print ("                       Jadwal Pelajaran SMK TELKOM JKT                      ")
        print ("1. Senin                                                                    ")
        print ("")
        print ("2. Selasa                                                                   ")
        print ("")
        print ("3. Rabu                                                                     ")
        print ("")
        print ("4. Kamis                                                                    ")
        print ("")
        print ("5. Jumat                                                                    ")
        print ("")
        print ("6. Keluar                                                                   ")
        pilihan = input ("Masukan Jadwal Hari (Senin/Selasa/Rabu/Kamis/Jumat/Keluar): ")

        if pilihan == "Senin":
            print("Jadwal Hari Senin: ")
            for jadwal in jadwal_pelajaran["Senin"]:
                print(f"-{jadwal}")
        
        elif pilihan == "Selasa":
            print("Jadwal Hari Selasa: ")
            for jadwal in jadwal_pelajaran["Selasa"]:
                print(f"-{jadwal}")
            
        elif pilihan == "Rabu":
            print("Jadwal Hari Rabu: ")
            for jadwal in jadwal_pelajaran["Rabu"]:
                print(f"-{jadwal}")
        
        elif pilihan == "Kamis":
            print("Jadwal Hari Kamis: ")
            for jadwal in jadwal_pelajaran["Kamis"]:
                print(f"-{jadwal}")
        
        elif pilihan == "Jumat":
            print("Jadwal Hari Jumat: ")
            for jadwal in jadwal_pelajaran["Jumat"]:
                print(f"-{jadwal}")
           
        
        elif pilihan == "Keluar":
            print ("Terima kasih Telah Menggunakan Jadwal ini")
            
        else:
            print ("Pilihan anda tidak ada dalam daftar")
              
 
    