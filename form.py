# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pickle
from keras.models import Sequential, model_from_json
from keras.layers import Dense, LeakyReLU, Dropout, BatchNormalization
from keras.optimizers import Adam
import keras as K
import sys,os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QGridLayout
from PyQt5.QtGui import *

#Adana Verileri
modelFile = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelAdana_yeni.json", "r")
modelH5File ="C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelAdana_yeni.h5"

model2File = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/KNNModelAdana_yeni.sav", "rb")
model3File = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/EnerjiKNNModelAdana_yeni.sav", "rb")
scalerFile = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scalerAdana_yeni.sav", "rb")
scaler2File = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler2rAdana_yeni.sav", "rb")
scaler3File = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler3rAdana_yeni.sav", "rb")


#Konya Verileri
modelFileKonya = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelKonya_yeni.json", "r")
modelH5FileKonya = "C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelKonya_yeni.h5"

model2FileKonya = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/KNNModelKonya_yeni.sav", "rb")
model3FileKonya = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/EnerjiKNNModelKonya_yeni.sav", "rb")
scalerFileKonya = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scalerKonya_yeni.sav", "rb")
scaler2FileKonya = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler2Konya_yeni.sav", "rb")
scaler3FileKonya = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler3Konya_yeni.sav", "rb")

#Ankara Verileri
modelFileAnkara = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelAnkara_yeni.json", "r")
modelH5FileAnkara = "C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelAnkara_yeni.h5"

model2FileAnkara = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/KNNModelAnkara_yeni.sav", "rb")
model3FileAnkara = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/EnerjiKNNModelAnkara_yeni.sav", "rb")
scalerFileAnkara = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scalerAnkara_yeni.sav", "rb")
scaler2FileAnkara = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler2Ankara_yeni.sav", "rb")
scaler3FileAnkara = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler3Ankara_yeni.sav", "rb")


#Manisa Verileri
modelFileManisa = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelManisa_yeni.json", "r")
modelH5FileManisa = "C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/DeepLearningModelManisa.h5"

model2FileManisa = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/KNNModelManisa_yeni.sav", "rb")
model3FileManisa = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/EnerjiKNNModelManisa_yeni.sav", "rb")
scalerFileManisa = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scalerManisa_yeni.sav", "rb")
scaler2FileManisa = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler2Manisa_yeni.sav", "rb")
scaler3FileManisa = open("C:/Users/GULDANE ONCUL/Desktop/BitirmeMakineÖğrenmesiModelleri/scaler3Manisa_yeni.sav", "rb")


import requests






class Ui_Form(object):
    Form = None
    
    def tahminEt(self):
        if str(self.comboBox.currentText()) is not "":
            kullanilacak=["saat","gun","isinim","sicaklik","hucreSicakligi","ruzgarHizi","PR"]
            gelen_sutunlar=["tarih","isinim","sicaklik","hucreSicakligi","ruzgarHizi","PR"]
            tarih = self.line_tarih.text() + " " + self.saat_sec.text()
            gelen_veriler = [[
                    tarih,
                    float(self.line_isinim.text().replace(",", ".")),
                    float(self.line_sicaklik.text().replace(",", ".")),
                    float(self.line_hucre.text().replace(",", ".")),
                    float(self.line_ruzgar.text().replace(",", ".")),
                    #float(self.line_Dc.text().replace(",", ".")),
                    float(self.line_pr.text().replace(",", "."))
                    ]]
            
            gelen_test = pd.DataFrame(gelen_veriler, columns=gelen_sutunlar)
            gelen_test['tarih']=pd.to_datetime(gelen_test['tarih'], format='%d.%m.%Y %H:%M:%S')
            gelen_test["saat"] = (gelen_test.tarih.astype("int64") // 10**9) % (60*60*24)
            gelen_test["gun"] = gelen_test.tarih.dt.dayofyear
            print(gelen_test)
            gelen_x = gelen_test[kullanilacak]
            gelen_x_sc = self.scaler.transform(gelen_x)
            enerjiSonuc = self.model.predict(gelen_x_sc)
            gunlukUretimSonuc = self.model2.predict(gelen_x_sc)
            
    # =============================================================================
            enerjiSonucInversed = self.scaler2.inverse_transform(enerjiSonuc)
            print("Enerji Tahmin:", enerjiSonucInversed[0][0])
            self.line_enerji.setText(str(int(enerjiSonucInversed[0][0])))
    # =============================================================================
    # =============================================================================
    #         print("Enerji Tahmin:", enerjiSonuc)
    #         self.line_enerji.setText(str(enerjiSonuc[0][0]))
    # =============================================================================
            
            gunlukUretimSonucInversed = self.scaler3.inverse_transform(gunlukUretimSonuc)
            print("Günlük Üretim Tahmin:", gunlukUretimSonucInversed[0][0])
            self.line_gunluk.setText(str(int(gunlukUretimSonucInversed[0][0])))

           
    def on_combobox_changed(self, value):
        print("combobox changed", value)
        sehir=str(self.comboBox.currentText())
        #aralik=str(self.comboBoxtahmin_aralik.currentText())
        print(sehir)
        if sehir=="Adana":
            loaded_model_json = modelFile.read()
            self.model = model_from_json(loaded_model_json)
#            if aralik=="Haftalık":
#                 qimg = QtGui.QPixmap("adanahaftalik_enerji.png")
#                 qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label.setPixmap(qimg)
#                 self.gorsel_label.resize(qimg.size())
#                 
#                 gunluk_img= QtGui.QPixmap("adanahaftalik_gunluk.png")
#                 gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                 self.gorsel_label_gunluk.resize(gunluk_img.size())
#            elif aralik=="Aylık":                
#                 qimg = QtGui.QPixmap("adanaaylik_enerji.png")
#                 qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label.setPixmap(qimg)
#                 self.gorsel_label.resize(qimg.size())
#                 
#                 gunluk_img= QtGui.QPixmap("adanaaylik_gunluk.png")
#                 gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                 self.gorsel_label_gunluk.resize(gunluk_img.size())
        # load weights into new model
            self.model.load_weights(modelH5File)
            print("Loaded model from disk")
    
            self.model2 = pickle.load(model2File)
            self.model3 = pickle.load(model3File)
    
            self.scaler = pickle.load(scalerFile)
            self.scaler2 = pickle.load(scaler2File)
            self.scaler3 = pickle.load(scaler3File)
            
        elif sehir=="Ankara":
            loaded_model_json = modelFileAnkara.read()
            self.model = model_from_json(loaded_model_json)
        # load weights into new model
#            if aralik=="Haftalık":
#                 qimg = QtGui.QPixmap("ankarahaftalik_enerji.png")
#                 qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label.setPixmap(qimg)
#                 self.gorsel_label.resize(qimg.size())
#                 
#                 gunluk_img= QtGui.QPixmap("ankarahaftalik_gunluk.png")
#                 gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                 self.gorsel_label_gunluk.resize(gunluk_img.size())
#            elif aralik=="Aylık":
#                 qimg = QtGui.QPixmap("ankaraaylik_enerji.png")
#                 qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label.setPixmap(qimg)
#                 self.gorsel_label.resize(qimg.size())
#                 
#                 gunluk_img= QtGui.QPixmap("ankaraaylik_gunluk.png")
#                 gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                 self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                 self.gorsel_label_gunluk.resize(gunluk_img.size())
            self.model.load_weights(modelH5FileAnkara)
            print("Loaded model from disk")
    
            self.model2 = pickle.load(model2FileAnkara)
            self.model3 = pickle.load(model3FileAnkara)
    
            self.scaler = pickle.load(scalerFileAnkara)
            self.scaler2 = pickle.load(scaler2FileAnkara)
            self.scaler3 = pickle.load(scaler3FileAnkara)
        elif sehir=="Konya":
            loaded_model_json = modelFileKonya.read()
            self.model = model_from_json(loaded_model_json)
        # load weights into new model
#            if aralik=="Haftalık":
#                qimg = QtGui.QPixmap("konyahaftalik_enerji.png")
#                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label.setPixmap(qimg)
#                self.gorsel_label.resize(qimg.size())
#                
#                gunluk_img= QtGui.QPixmap("konyahaftalik_gunluk.png")
#                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                self.gorsel_label_gunluk.resize(gunluk_img.size())
#            elif aralik=="Aylık":
#                qimg = QtGui.QPixmap("konyaaylik_enerji.png")
#                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label.setPixmap(qimg)
#                self.gorsel_label.resize(qimg.size())
#                
#                gunluk_img= QtGui.QPixmap("konyaaylik_gunluk.png")
#                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                self.gorsel_label_gunluk.resize(gunluk_img.size())
            self.model.load_weights(modelH5FileKonya)
            print("Loaded model from disk")
    
            self.model2 = pickle.load(model2FileKonya)
            self.model3 = pickle.load(model3FileKonya)
    
            self.scaler = pickle.load(scalerFileKonya)
            self.scaler2 = pickle.load(scaler2FileKonya)
            self.scaler3 = pickle.load(scaler3FileKonya)
        elif sehir=="Manisa":
            loaded_model_json = modelFileManisa.read()
            self.model = model_from_json(loaded_model_json)
        # load weights into new model
#            if aralik=="Haftalık":
#                qimg = QtGui.QPixmap("manisahaftalik_enerji.png")
#                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label.setPixmap(qimg)
#                self.gorsel_label.resize(qimg.size())
#                
#                gunluk_img= QtGui.QPixmap("manisahaftalik_gunluk.png")
#                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                self.gorsel_label_gunluk.resize(gunluk_img.size())
#            elif aralik=="Aylık":
#                qimg = QtGui.QPixmap("manisaaylik_enerji.png")
#                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label.setPixmap(qimg)
#                self.gorsel_label.resize(qimg.size())
#                
#                gunluk_img= QtGui.QPixmap("manisaaylik_gunluk.png")
#                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#                self.gorsel_label_gunluk.setPixmap(gunluk_img)
#                self.gorsel_label_gunluk.resize(gunluk_img.size())
            self.model.load_weights(modelH5FileManisa)
            print("Loaded model from disk")
    
            self.model2 = pickle.load(model2FileManisa)
            self.model3 = pickle.load(model3FileManisa)
    
            self.scaler = pickle.load(scalerFileManisa)
            self.scaler2 = pickle.load(scaler2FileManisa)
            self.scaler3 = pickle.load(scaler3FileManisa)
    def on_combobox_changed_aralik(self, value):
        print("aralık combobox changed", value)
        sehir=str(self.comboBox.currentText())
        aralik=str(self.comboBoxtahmin_aralik.currentText())
        if sehir=="Adana":
            if aralik=="Haftalık":
                qimg = QtGui.QPixmap("adanahaftalik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("adanahaftalik_gunluk.png")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
            elif aralik=="Aylık":               
                qimg = QtGui.QPixmap("adanaaylik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("adanaaylik_gunluk.png")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
        elif sehir=="Ankara":
            if aralik=="Haftalık":
                qimg = QtGui.QPixmap("ankarahaftalik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("ankarahaftalik_gunluk.png")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
            elif aralik=="Aylık":
                qimg = QtGui.QPixmap("ankaraaylik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("ankaraaylik_gunluk.png")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
        elif sehir=="Konya":
            if aralik=="Haftalık":
                qimg = QtGui.QPixmap("konyahaftalik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("konyahaftalik_gunluk.png")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
            elif aralik=="Aylık":
                qimg = QtGui.QPixmap("konyaaylik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("konyaaylik_gunluk.PNG")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
        elif sehir=="Manisa":
            if aralik=="Haftalık":
                qimg = QtGui.QPixmap("manisahaftalik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("manisahaftalik_gunluk.png")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
            elif aralik=="Aylık":
                qimg = QtGui.QPixmap("manisaaylik_enerji.png")
                qimg = qimg.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label.setPixmap(qimg)
                self.gorsel_label.resize(qimg.size())
                
                gunluk_img= QtGui.QPixmap("manisaaylik_gunluk.png")
                gunluk_img=gunluk_img.scaled(400, 300, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                self.gorsel_label_gunluk.setPixmap(gunluk_img)
                self.gorsel_label_gunluk.resize(gunluk_img.size())
    def tarihSec(self):
        self.tarih_sec.setVisible(True)
    
    def tarihSecim(self):
        tarih = self.tarih_sec.selectedDate()        
        print("Seçilen Tarih: {}".format(tarih))
        self.line_tarih.setText(str(tarih.day()) + "." +
                                str(tarih.month()) + "." +
                                str(tarih.year()))
        self.tarih_sec.setVisible(False)
    def gorsel(self):
        self.tahmin_dialog = QtWidgets.QDialog(self.Form)
        self.tahmin_dialog.resize(650, 400)
        self.tahmin_dialog.setWindowTitle("Güneş Paneli Tahmin Sistemi/Grafikler")
       
        
        self.comboBoxtahmin_aralik = QtWidgets.QComboBox(self.tahmin_dialog)
        self.comboBoxtahmin_aralik.setGeometry(QtCore.QRect( 170, 25, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.comboBoxtahmin_aralik.setFont(font)
        self.comboBoxtahmin_aralik.setObjectName("lbl_fotogoster")
        self.comboBoxtahmin_aralik.addItem("Haftalık")
        self.comboBoxtahmin_aralik.addItem("Aylık")
        #self.comboBoxtahmin_aralik.addItem("500-750")
        
        self.gorsel_label = QtWidgets.QLabel(self.tahmin_dialog)
        self.gorsel_label.setWordWrap(True)
        self.gorsel_label.setGeometry(QtCore.QRect(100, 40, 91, 22))
        
        self.gorsel_label_gunluk = QtWidgets.QLabel(self.tahmin_dialog)
        self.gorsel_label_gunluk.setWordWrap(True)
        self.gorsel_label_gunluk.setGeometry(QtCore.QRect(100, 140, 91, 22))
        
        self.lbl_enerji_gr=QtWidgets.QLabel(self.tahmin_dialog)
        self.lbl_enerji_gr.setGeometry(QtCore.QRect(50, 140, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_gunluk=QtWidgets.QLabel(self.tahmin_dialog)
        self.lbl_gunluk.setGeometry(QtCore.QRect(50, 240, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_fotogoster = QtWidgets.QLabel(self.tahmin_dialog)
        self.lbl_fotogoster.setGeometry(QtCore.QRect(170,5, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_secimse_grafik = QtWidgets.QLabel(self.tahmin_dialog)
        self.lbl_secimse_grafik.setGeometry(QtCore.QRect(50,5, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        
        
        self.comboBox_sehir_grafik = QtWidgets.QComboBox(self.tahmin_dialog)
        self.comboBox_sehir_grafik.setGeometry(QtCore.QRect(50, 25, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
       
        self.lbl_secimse_grafik.setText("Şehir Seçimi")
        self.lbl_secimse_grafik.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        
        self.comboBox_sehir_grafik.setFont(font)
        self.comboBox_sehir_grafik.setObjectName("lbl_secim_grafik")
        self.comboBox_sehir_grafik.addItem("Adana")
        self.comboBox_sehir_grafik.addItem("Ankara")
        self.comboBox_sehir_grafik.addItem("Konya")
        self.comboBox_sehir_grafik.addItem("Manisa")
        
    

        self.lbl_fotogoster.setText("Aralık seçiniz")
        self.lbl_fotogoster.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_enerji_gr.setText("Enerji Grafiği")
        self.lbl_enerji_gr.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_gunluk.setText("G. Üretim Grafiği")
        self.lbl_gunluk.setStyleSheet("color: blue;" "selection-background-color: blue;")
        self.comboBoxtahmin_aralik.currentTextChanged.connect(self.on_combobox_changed_aralik)
        self.comboBox_sehir_grafik.currentTextChanged.connect(self.on_combobox_changed_aralik)
        
        self.lbl_aciklama = QtWidgets.QLabel(self.tahmin_dialog)
        self.lbl_aciklama.setGeometry(QtCore.QRect(10,200, 2500, 250))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_aciklama.setText("Yukarıdaki grafiklerde mavi çizgiler gerçek değerleri, sarı/turuncu çizgiler ise modelin tahmin ettiği değerleri göstermektedir. ")
        self.lbl_aciklama.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.tahmin_dialog.show()
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(744, 500)
        self.Form = Form
        self.line_ruzgar = QtWidgets.QLineEdit(Form)
        self.line_ruzgar.setGeometry(QtCore.QRect(110, 230, 113, 20))
        self.line_ruzgar.setObjectName("line_ruzgar")
        #self.line_Dc = QtWidgets.QLineEdit(Form)
        #self.line_Dc.setGeometry(QtCore.QRect(110, 270, 113, 20))
        #self.line_Dc.setObjectName("line_Dc")
        self.lbl_pr = QtWidgets.QLabel(Form)
        self.lbl_pr.setGeometry(QtCore.QRect(40, 270, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pr.setFont(font)
        self.lbl_pr.setObjectName("lbl_pr")
        self.line_gunluk = QtWidgets.QLineEdit(Form)
        self.line_gunluk.setGeometry(QtCore.QRect(420, 190, 113, 20))
        self.line_gunluk.setObjectName("line_gunluk")
        self.line_hucre = QtWidgets.QLineEdit(Form)
        self.line_hucre.setGeometry(QtCore.QRect(110, 180, 113, 20))
        self.line_hucre.setObjectName("line_hucre")
        
        self.but_tahmin = QtWidgets.QPushButton(Form)
        self.but_tahmin.setGeometry(QtCore.QRect(110, 360, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(80)
        self.but_tahmin.setFont(font)
        self.but_tahmin.setObjectName("but_tahmin")
        
        self.but_gorsel = QtWidgets.QPushButton(Form)
        self.but_gorsel.setGeometry(QtCore.QRect(400, 360, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(80)
        self.but_gorsel.setFont(font)
        self.but_gorsel.setObjectName("but_gorsel")
        
        self.line_pr = QtWidgets.QLineEdit(Form)
        self.line_pr.setGeometry(QtCore.QRect(110, 270, 113, 20))
        self.line_pr.setObjectName("line_pr")
        self.lbl_enerji = QtWidgets.QLabel(Form)
        self.lbl_enerji.setGeometry(QtCore.QRect(420, 60, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_enerji.setFont(font)
        self.lbl_enerji.setObjectName("lbl_enerji")
        self.line_tarih = QtWidgets.QLineEdit(Form)
        self.line_tarih.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.line_tarih.setObjectName("line_tarih")
        self.line_isinim = QtWidgets.QLineEdit(Form)
        self.line_isinim.setGeometry(QtCore.QRect(110, 130, 113, 20))
        self.line_isinim.setObjectName("line_isinim")
        #self.lbl_dcGuc = QtWidgets.QLabel(Form)
        #self.lbl_dcGuc.setGeometry(QtCore.QRect(40, 270, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        #self.lbl_dcGuc.setFont(font)
        #self.lbl_dcGuc.setObjectName("lbl_dcGuc")
        self.lbl_hucrescaklg = QtWidgets.QLabel(Form)
        self.lbl_hucrescaklg.setGeometry(QtCore.QRect(20, 180, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hucrescaklg.setFont(font)
        self.lbl_hucrescaklg.setObjectName("lbl_hucrescaklg")
        self.lbl_tarih = QtWidgets.QLabel(Form)
        self.lbl_tarih.setGeometry(QtCore.QRect(50, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tarih.setFont(font)
        self.lbl_tarih.setObjectName("lbl_tarih")
        self.line_sicaklik = QtWidgets.QLineEdit(Form)
        self.line_sicaklik.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.line_sicaklik.setObjectName("line_sicaklik")
        self.lbl_gunluktah = QtWidgets.QLabel(Form)
        self.lbl_gunluktah.setGeometry(QtCore.QRect(420, 160, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_gunluktah.setFont(font)
        self.lbl_gunluktah.setObjectName("lbl_gunluktah")
        self.lbl_ruzgar = QtWidgets.QLabel(Form)
        self.lbl_ruzgar.setGeometry(QtCore.QRect(30, 230, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_ruzgar.setFont(font)
        self.lbl_ruzgar.setObjectName("lbl_ruzgar")
        self.line_enerji = QtWidgets.QLineEdit(Form)
        self.line_enerji.setGeometry(QtCore.QRect(420, 90, 113, 20))
        self.line_enerji.setObjectName("line_enerji")
        self.lbl_sacaklk = QtWidgets.QLabel(Form)
        self.lbl_sacaklk.setGeometry(QtCore.QRect(50, 130, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_sacaklk.setFont(font)
        self.lbl_sacaklk.setObjectName("lbl_sacaklk")
        self.lbl_snm = QtWidgets.QLabel(Form)
        self.lbl_snm.setGeometry(QtCore.QRect(50, 90, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_snm.setFont(font)
        self.lbl_snm.setObjectName("lbl_snm")
        self.lbl_saat = QtWidgets.QLabel(Form)
        self.lbl_saat.setGeometry(QtCore.QRect(240, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_saat.setFont(font)
        self.lbl_saat.setObjectName("lbl_saat")
        self.saat_sec = QtWidgets.QTimeEdit(Form)
        self.saat_sec.setGeometry(QtCore.QRect(290, 50, 71, 22))
        self.saat_sec.setDisplayFormat("HH:mm:ss")
        self.saat_sec.setObjectName("saat_sec")
        self.tarih_sec = QtWidgets.QCalendarWidget(Form)
        self.tarih_sec.setGeometry(QtCore.QRect(110, 50, 296, 183))
        self.tarih_sec.setObjectName("tarih_sec")
        self.tarih_sec.setVisible(False)
        
        self.lbl_secim = QtWidgets.QLabel(Form)
        self.lbl_secim.setGeometry(QtCore.QRect(50, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.lbl_saat.setFont(font)
        self.lbl_saat.setObjectName("lbl_secim")
        
        
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 20, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("lbl_secim")
        self.comboBox.addItem("Adana")
        self.comboBox.addItem("Ankara")
        self.comboBox.addItem("Konya")
        self.comboBox.addItem("Manisa")
        
        
        
        


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.but_tahmin.clicked.connect(self.tahminEt)
        self.line_tarih.selectionChanged.connect(self.tarihSec)
        self.tarih_sec.selectionChanged.connect(self.tarihSecim)
        self.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.but_gorsel.clicked.connect(self.gorsel)
        #elf.comboBoxtahmin_aralik.currentTextChanged.connect(self.on_combobox_changed)
        
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Güneş Paneli Tahmin Sistemi")
        
           
        #Form.setStyleSheet("background-color:green;")
        #Form.setStyleSheet("{background-image: url(:fotovoltaik-paneller-1.jpg);}")
        #Form.setStyleSheet("{background-image: url(1.png);}")
        Form.setStyleSheet("QWidget#Form {background-image: url(fotovoltaik-paneller-1.jpg);}")
        
        self.lbl_pr.setText(_translate("Form", "PR"))
        self.lbl_pr.setStyleSheet("color: white;" "selection-background-color: white;")
        self.but_tahmin.setText(_translate("Form", "TAHMİN ET"))
        self.but_tahmin.setStyleSheet("color: orange;" "selection-background-color: orange;")
        
        self.but_gorsel.setText(_translate("Form", "Grafikler"))
        self.but_gorsel.setStyleSheet("color: orange;" "selection-background-color: orange;")
        
        self.lbl_enerji.setText(_translate("Form", "Enerji Tahmini"))
        self.lbl_enerji.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        #self.lbl_dcGuc.setText(_translate("Form", "Dc Güç"))
        #self.lbl_dcGuc.setStyleSheet("color: white;" "selection-background-color: white;")
        
        self.lbl_hucrescaklg.setText(_translate("Form", "Hücre Sıcaklığı"))
        self.lbl_hucrescaklg.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_tarih.setText(_translate("Form", "Tarih"))
        self.lbl_tarih.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_gunluktah.setText(_translate("Form", "Günlük Üretim Tahmini"))
        self.lbl_gunluktah.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_ruzgar.setText(_translate("Form", "Rüzgar Hızı"))
        self.lbl_ruzgar.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_sacaklk.setText(_translate("Form", "Işınım"))
        self.lbl_sacaklk.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_snm.setText(_translate("Form", "Sıcaklık"))
        self.lbl_snm.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_saat.setText(_translate("Form", "Saat"))
        self.lbl_saat.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        self.lbl_secim.setText(_translate("Form", "Şehir Seçimi"))
        self.lbl_secim.setStyleSheet("color: blue;" "selection-background-color: blue;")
        
        
       
        self.comboBox.setItemText(0, _translate("MainWindow", "Adana"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ankara"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Konya"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Manisa"))
        
 
if __name__ == "__main__":
    import sys   
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec_()

