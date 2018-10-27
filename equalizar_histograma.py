from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread("jogador.jpg")
img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist( img )
cv2.imshow('sf', h_eq)
"""
plt.figure()
plt.title( "Histograma Equalizado")
plt.xlabel( "Intensidade")
plt.ylabel("Quantidade de pixel")
plt.hist( h_eq.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()


plt.figure()
plt.title( "Histograma Original")
plt.xlabel( "Intensidade")
plt.ylabel("Quantidade de pixel")
plt.hist( img.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()
"""
