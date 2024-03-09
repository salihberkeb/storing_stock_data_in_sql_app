import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
from _hisseAppForm import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets



class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_onayla.clicked.connect(self.onayla)
        self.ui.btn_cikis.clicked.connect(self.close)
    

    def onayla(self):
        global hisse_kodu, satis_degeri, alis_degeri , alis_tarihi,satis_tarihi,kar_zarar_miktari , adet
        hisse_kodu=self.ui.txt_hissekodu.text()
        satis_degeri=int(self.ui.txt_satis.text())
        alis_degeri=int(self.ui.txt_alis.text())
        adet=int(self.ui.txt_adet.text())
   
        alis_tarihi=self.ui.date_alis.text()
        satis_tarihi=self.ui.date_satis.text()

        kar_zarar_miktari=str((satis_degeri-alis_degeri)*adet)

        self.ui.lbl_karzarar.setText(kar_zarar_miktari)

        self.hisseleri_ekle(hisse_kodu,alis_degeri,satis_degeri,alis_tarihi,satis_tarihi,kar_zarar_miktari)

        self.ekrani_temizle()


    def hisseleri_ekle(self,hisse_kodu,alis_degeri,satis_degeri,alis_tarihi,satis_tarihi,kar_zarar_miktari):
        connection=mysql.connector.connect(
        host="localhost",
        user="sbb",
        password="",
        database=""

        )
        mycursor=connection.cursor()
        sql="INSERT INTO hisse_tablosu(hisse_kodu,alis_degeri,satis_degeri,adet,alis_tarihi,satis_tarihi,kar_zarar_miktari) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values=[(hisse_kodu,alis_degeri,satis_degeri,adet,alis_tarihi,satis_tarihi,kar_zarar_miktari)]

        mycursor.executemany(sql,values)

        try:
            connection.commit()
            print(f"{mycursor.rowcount} tane kayıt eklendi")
            print(f"son eklenen kaydın id: {mycursor.lastrowid}")
            self.ui.lbl_islemonayi.setText("GEÇERLİ")

        except mysql.connector.Error as err:
            print("hata:",err)
            self.ui.lbl_islemonayi.setText("GEÇERSİZ")
            

        finally:
            # connection.close()
            print("database baglantisi kapandi.")
        
    def kayit_silme():
        pass

    def ekrani_temizle(self):
        self.ui.txt_hissekodu.clear()
        self.ui.txt_alis.clear()
        self.ui.txt_satis.clear()


    
    def close(self):
        quitmessage=QMessageBox.question(self,"Çıkış","Çıkmak istedğine emin misiniz ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if quitmessage==QMessageBox.Yes:
            quit()


def app():

    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()


# list=[]
# while True:
# list.append((hisse_kodu,alis_degeri,satis_degeri,alis_tarihi,satis_tarihi,kar_zarar_miktari))
#     result=input("devam etmek istiyor musnuz? (e/h)")
#     if result == "h":
#         print("Kayıtlarınız veri tabanına aktarılıyor")
#         print(list)
#         hisseleri_ekle(list)
#         break
        
"""
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '10');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '9');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '8');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '7');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '6');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '5');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '4');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '3');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '2');
DELETE FROM `borsa_uygulamasi`.`hisse_tablosu` WHERE (`id` = '1');
"""
