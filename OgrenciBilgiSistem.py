import pandas as pd
try:
    ogrenci_sayisi=input("Kac adet ogrenci girecegini yaziniz:")
    ogrenci_sayisi=int(ogrenci_sayisi)
    if ogrenci_sayisi<=0:
        print("Hatali bir deger girdiniz.Tekrar deneyin.")
except ValueError:
        print('Only integers are allowed! Try again.')

ad_soyadlar=[]
okul_nos=[]
puanlar=[]
harf_not=[]
gecme_durumu=[]

def not_hesapla():
     try:
        global puan
        puan=input("Lutfen not degerini giriniz:") 
        puan=int(puan)
        if puan>100 or puan<0:
         print("Lutfen 0 ile 100 arasinda bir deger giriniz.")  
        elif puan>=90 and puan<=100:
            return "A"
        elif puan>=80 and puan<90:
            return "B"
        elif puan>=60 and puan<80:
            return "C"
        elif puan>=50 and puan<60:
            return "D"
        else:
            return "F"    
     except ValueError:
        return 'Only integers are allowed! Try again.'
        
def ogrenci_ekle(ad_soyad,okul_no,puan):
    ad_soyadlar.append(ad_soyad)
    okul_nos.append(okul_no)
    puanlar.append(puan)

def kaldi_gecti(puan):
        if puan>=50 and puan<=100:
            return "Gecti"
        else: 
            return "Kaldi"

def ogrenci(ogrenci_sayisi):
    for i in range(ogrenci_sayisi):
        try:
            ad_soyad=input("Ogrenci adi ve soyadini giriniz:")
            if ad_soyad.isdigit():
             raise TypeError("Sadece string ifadelere izin verilir.")

            okul_no=input("Ogrenci okul numarasini giriniz:")
            okul_no=int(okul_no)
            if okul_no in okul_nos:
                return "Ayni okul numarasına sahip iki ogrenci olamaz"
                break
            harf_not.append(not_hesapla())
            gecme_durumu.append(kaldi_gecti(puan))
            ogrenci_ekle(ad_soyad,okul_no,puan)
        except ValueError:
            return "Only integers are allowed! Try again."
         

print(ogrenci(ogrenci_sayisi))
yenilist=[ad_soyadlar,okul_nos,puanlar,harf_not,gecme_durumu]
df_students=pd.DataFrame(yenilist,index=["Ad-Soyad","Okul Numarası","Aldigi Puan","Harf Notu","Gecme Durumu"])
print(df_students)


df_students.to_excel('OgrenciBilgiSistemi.xlsx')
