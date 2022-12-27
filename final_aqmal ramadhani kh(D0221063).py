#nama   :   AQMAL RAMADHANI KH
#nim    :   D0221063

#RUMUS MENGHITUNG VOLUME DAN LUAS DENGAN METODE INHERITANCE!!!

class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi**2

class Segitiga(BangunDatar):
    def __init__(self,alas,tinggi) :
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return self.alas * self.tinggi / 2

class Lingkaran(BangunDatar):
    def __init__(self,jari2):
        self.phi = 22/7
        self.jari2 = jari2

    def luas(self):
        return self.phi * (self.jari2**2)

class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi**3

class Limas(BangunRuang):
    def __init__(self,panjang_alas,tinggi_alas,tinggi_limas):
        self.panjang_alas = panjang_alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_limas = tinggi_limas

    def volume(self):
        return (self.panjang_alas*self.tinggi_alas/2) * self.tinggi_limas / 3

class Tabung(BangunRuang):
    def __init__(self,jari2,tinggi):
        self.phi = 22/7
        self.jari2 = jari2
        self.tinggi = tinggi

    def volume(self):
        return self.phi * (self.jari2**2) * self.tinggi
    
class Balok(BangunRuang):
    def __init__(self, panjang,luas,tinggi):
        self.panjang = panjang
        self.luas = luas
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * (self.luas) * self.tinggi

def menu_bangundatar():
    while True : 
        print('''MENU PILIHAN
1. persegi
2. segitiga
3. lingkaran
4. kembali''')
        pilihan = int(input("pilih kode menu diatas : "))
        if pilihan == 1 : 
            print("menghitung luas persegi")
            sisi = int(input("masukkan panjang sisi : "))
            persegi = Persegi(sisi)
            print("luas persegi = ",persegi.luas()) 
        elif pilihan == 2 : 
            print("menghitung luas segitiga")
            alas = int(input("masukkan panjang alas segitiga : "))
            tinggi = int(input("masukkan panjang tinggi segitiga : "))
            segitiga = Segitiga(alas,tinggi)
            print("luas segitiga = ",segitiga.luas())
        elif pilihan == 3 : 
            print("menghitung luas lingkaran")
            jari2 = int(input("masukkan panjang jari-jari : "))
            lingkaran = Lingkaran(jari2)
            print("luas lingkaran = ",int(lingkaran.luas()))
        elif pilihan == 4 : 
            menu_utama()
        else : 
            print("masukkan kode menu dengan benar!")

            
            


def menu_bangunruang():
    while True : 
        print('''MENU PILIHAN
1. tabung
2. limas segitiga
3. kubus
4. balok
5. kembali''')
        menu = int(input("pilih kode menu diatas : "))
        if menu == 1 : 
            print("menghitung volume tabung")
            jari2 = int(input("masukkan panjang jari-jari : "))
            tinggi = int(input("masukkan tinggi tabung : "))
            tabung = Tabung(jari2,tinggi)
            print("volume tabung = ",int(tabung.volume()))
        elif menu == 2 : 
            print("menghitung volume limas segitiga")
            alas = int(input("masukkan panjang alas segitiga : "))
            tinggi_alas = int(input("masukkan panjang tinggi alas segitiga : "))
            tinggi_limas = int(input("masukkan panjang tinggi limas : "))
            limas = Limas(alas,tinggi_alas,tinggi_limas)
            print("volume limas segitiga = ",limas.volume())
        elif menu == 3 : 
            print("menghitung volume kubus")
            sisi = int(input("masukkan panjang sisi : "))
            kubus = Kubus(sisi)
            print("volume kubus = ",kubus.volume())
        elif menu == 4:
            print("menghitung volume balok")
            panjang = int(input("masukkan panjang balok: "))
            lebar = int(input("masukkan lebar balok: "))
            tinggi = int(input("masukkan tinggi balok: "))
            balok = Balok(panjang,lebar,tinggi)
            print("volume balok = ",int(balok.volume()))
            

        elif pilihan == 5 : 
            menu_utama()
        else : 
            print("masukkan kode yang benar!")
        

def menu_utama():
    while True : 
        print('''~~~SELAMAT DATANG~~~
MENU PILIHAN
1. menghitung luas bangun datar
2. menghitung volume bangun ruang
3. berhenti''')
        pilihan = int(input("pilih kode menu diatas : "))
        if pilihan == 1 : 
            menu_bangundatar()
        elif pilihan == 2 : 
            menu_bangunruang()
        elif pilihan == 3 :
            break
        else : 
            print("masukkan kode dengan benar")

menu_utama()
