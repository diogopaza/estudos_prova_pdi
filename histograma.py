from matplotlib import pyplot as plt
import cv2

img = cv2.imread("jogador.jpg")
img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
#Função calcHist para calcular o histograma da imagem
h = cv2.calcHist( [img], [0], None, [256], [0,256])
plt.figure()
plt.title( "Histograma")
plt.xlabel( "Intensidade")
plt.ylabel("Quantidade de pixel")
plt.plot( h )
plt.xlim([0,256])
plt.show()





