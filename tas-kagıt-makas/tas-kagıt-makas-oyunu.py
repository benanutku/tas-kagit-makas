from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
from random import randint



#ana pencerimiz 
app=Tk()
app.title("Taş Kağıt Makas")
app.geometry("400x250")
app.configure(background="#9b59b6")

#resimler
tas_img= ImageTk.PhotoImage(Image.open("tas-user.png"))
kagit_img= ImageTk.PhotoImage(Image.open("kagıt-user.png"))
makas_img= ImageTk.PhotoImage(Image.open("makas-user.png"))
tas_img_bil= ImageTk.PhotoImage(Image.open("tas.png"))
kagıt_img_bil= ImageTk.PhotoImage(Image.open("kagıt.png"))
makas_img_bil= ImageTk.PhotoImage(Image.open("makas.png"))

#resim ekleme 

kul_label=Label(app,image=makas_img,bg="#9b59b6")
bil_label=Label(app,image=makas_img_bil,bg="#9b59b6")
bil_label.grid(row=1,column=0)
kul_label.grid(row=1,column=4)

#skor tutmak

kullanıcıSkor = Label(app,text=0,font=100,bg="#9b59b6",fg="white")
bilgisayarSkor=Label(app,text=0,font=100,bg="#9b59b6",fg="white")
bilgisayarSkor.grid(row=1,column=1)
kullanıcıSkor.grid(row=1,column=3)
#skor göstergesi
kullanıcı_indicator=Label(app,font=50,text="KULLANICI",bg="#9b59b6",fg="white")
bilgisayar_indicator=Label(app,font=50,text="BİLGİSAYAR",bg="#9b59b6",fg="white")
kullanıcı_indicator.grid(row=0,column=3)
bilgisayar_indicator.grid(row=0,column=1)

#tur skor tutmak
kullanıcıTurSkor=Label(app,text=0,font=100,bg="#9b59b6",fg="white")
bilgisayarTurSkor=Label(app,text=0,font=100,bg="#9b59b6",fg="white")
kullanıcıTurSkor.grid(row=0,column=10)
bilgisayarTurSkor.grid(row=10,column=10)

#tur skor göstergesi

kullanıcıTur_indicator=Label(app,font=50,text="KULLANICI",bg="#9b59b6",fg="white")
bilgisayarTur_indicator=Label(app,font=50,text="BİLGİSAYAR",bg="#9b59b6",fg="white")
kullanıcıTur_indicator.grid(row=0,column=5)
bilgisayarTur_indicator.grid(row=10,column=5)


#mesaj

msg=Label(app,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)
#güncelleme mesajı
def updateMesaj(x): 
 msg['text']= x

 #global değişkenler
kullanıcı_galibiyet=0
bilgisayar_galibiyet=0


 #kullanıcı skor güncellemesi
def updateKullanıcıSkor():
 score=int(kullanıcıSkor["text"])
 score += 1
 kullanıcıSkor["text"]=str(score)
 if score==3:
    updatekullanıcıTurSkor()
    resetSkor()
#bilgisayar skor güncellemesi
def updateBilgisayarSkor():
 score=int(bilgisayarSkor["text"])
 score += 1
 bilgisayarSkor["text"]=str(score)
 if score==3:
    updatebilgisayarTurskor()
    resetSkor()
 
 #kullanıcı tur skor güncellemesi
def updatekullanıcıTurSkor():
   score=int(kullanıcıTurSkor["text"])
   score +=1
   kullanıcıTurSkor["text"]=str(score)
   if score==1:
    global kullanıcı_galibiyet
    kullanıcı_galibiyet += 1
   
      

    #bilgisayar tur skor güncellemesi
 
def updatebilgisayarTurskor():
   score=int(bilgisayarTurSkor["text"])
   score +=1
   bilgisayarTurSkor["text"]=str(score)
   if score==1:
    global bilgisayar_galibiyet
    bilgisayar_galibiyet += 1
   
   
    
     
 
 
 #kazanan kontrolü 
def kontrolKazanan(oyuncu,bilgisayar):
 if oyuncu==bilgisayar:
  updateMesaj("Berabere")
 elif oyuncu== "taş":
     if bilgisayar=="kağıt":
      updateMesaj("Bilgisayar kazandı") 
      updateBilgisayarSkor()
     else:
      updateMesaj("oyuncu kazandı")
      updateKullanıcıSkor()
 elif oyuncu== "kağıt":
     if bilgisayar=="makas":
       updateMesaj("bilgisayar kazandı")
       updateBilgisayarSkor()
     else:
       updateMesaj("oyuncu kazandı")
       updateKullanıcıSkor()

 elif oyuncu=="makas":
     if bilgisayar=="taş":
       updateMesaj("bilgisayar kazandı")
       updateBilgisayarSkor()
     else:
       updateMesaj("oyuncu kazandı")
       updateKullanıcıSkor()
 else:
     pass
if int(kullanıcıSkor["text"]) == 3:
        updatekullanıcıTurSkor()
elif int(bilgisayarSkor["text"]) == 3:
        updatebilgisayarTurskor()



def resetSkor():
    kullanıcıSkor["text"]=0
    bilgisayarSkor["text"]=0
def resetTurSkor():
   kullanıcıTurSkor["text"]=0
   bilgisayarTurSkor["text"]=0



def resetGame():
    global kullanıcı_galibiyet, bilgisayar_galibiyet
    resetSkor()
    resetTurSkor()
    kullanıcı_galibiyet = 0
    bilgisayar_galibiyet = 0
    msg['text'] = "Oyun Sıfırlandı"
 #seçenek güncellemeleri
 
secenek = ["taş","kağıt","makas"]

def secenekGuncelle(x):
    # bilgisayar için
    bilgisayarSecenek = secenek[randint(0, 2)]  
    
    if bilgisayarSecenek == "taş": 
        bil_label.configure(image=tas_img_bil)
    elif bilgisayarSecenek == "kağıt":
        bil_label.configure(image=kagıt_img_bil)
    else:
        bil_label.configure(image=makas_img_bil)

    # kullanıcı için
    if x == "taş":
        kul_label.configure(image=tas_img)
    elif x == "kağıt":
        kul_label.configure(image=kagit_img)
    else:
        kul_label.configure(image=makas_img)

    # Kazananı kontrol et
    kontrolKazanan(x, bilgisayarSecenek)


  #buton
tas =Button(app,width=20,height=2,text="TAŞ", bg="#FF3E4D", fg="white", command=lambda: secenekGuncelle("taş")).grid(row=2, column=1)
  
kagıt =Button(app,width=20,height=2,text="KAĞIT", bg="#FAD02E", fg="white", command=lambda: secenekGuncelle("kağıt")).grid(row=2, column=2) 
  
  
makas =Button(app,width=20,height=2,text="MAKAS", bg="#0ABDE3", fg="white", command=lambda: secenekGuncelle("makas")).grid(row=2, column=3)


# sıfırla butonu
reset_button = Button(app, width=20, height=2, text="SIFIRLA", bg="#2C3E50", fg="white", command=resetGame).grid(row=4, column=2)


#skor butonu

app.mainloop()  


     
  

