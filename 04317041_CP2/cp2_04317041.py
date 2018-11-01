import csv
from sklearn import tree
import graphviz
import pandas as pd
import numpy as np


dataset = pd.read_csv('trave.csv') 
#print (dataset.head())
#print(dataset.describe())

#Memisahkan Tabel
X = dataset.drop('MAMPU', axis=1)  
Y = dataset['MAMPU']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

#usia
usia = input("Masukkan Usia Anda (0-80) ? ")
type(usia)
#0 Tua, 1 Muda
if int(usia) < 35 :
	A = 1
else :
	A = 0

#Gender
gender = input("Masukkan Gender Anda (L/P) ? ")
type(gender)
#1 Laki-Laki , 0 Perempuan
if gender == "L" or "l" :
	B = 1
else :
	B = 0

#Punya Penyakit Berat ?
stat = input("Apakah Mempunyai Sakit Berat ? (Y/N) ")
type(stat)
#1 Ya, 2 Tidak
if stat == "Y" or "y" :
	C = 1
else :
	C = 0

#Destinasi Wisata
tempat = input(	"1. Danau Toba \n"
				"2. Pantai Kuta \n"
				"3. Gunung Bromo \n"
				"4. Pulau Sempu \n"
			  	"5. Gunung Rinjani \n"
				"6. Gunung Semeru \n"
			   	"Masukkan Tempat Wisata yang ingin dituju (1-5) : "
			  )
type(tempat)
#1-2 (Ringan) , 3-4 (sedang) , 5-6 (Berat)
if int(tempat) <=2 :
	D = 0
elif int(tempat)<=4 :
	D = 1
else :
	D = 2


prediction = clf.predict([[A,B,C,D]])

#Test Sampling dengan data fix
#prediction = clf.predict([[1. ,0., 1., 2.]])

print("\n" "########################################" "\n")
print("usia anda : " ,usia, "\n" 
	  "Gender anda : " ,gender, "\n"
	  "Punya Penyakit berat " ,stat, "\n"
	  "Tempat yang akan dikunjungi : " ,tempat,"\n"
	  "Anda Dinyatakan : " ,prediction , "\n")

############################################################
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("CP2_04317041")


