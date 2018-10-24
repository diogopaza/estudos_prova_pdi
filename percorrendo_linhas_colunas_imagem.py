
import cv2

imagem = cv2.imread('jogador.jpg')
for y in range( 0, imagem.shape[0], 1):#percorre linhas
    for x in range(0, imagem.shape[1], 1):#percorre colunas
        imagem[y,x] = (0,(x*y)%256,0)
    
cv2.imshow('output', imagem)
 
"""
imagem = cv2.imread( "jogador.jpg ")
for y in range( 0, imagem.shape[0], 10):
   for x in range( 0, imagem.shape[1],10):
       imagem[y:y+5, x:x+5 ]= (0,255,255)

cv2.imshow('input', imagem)
"""


