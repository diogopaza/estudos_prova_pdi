import cv2
import numpy as np

imagem = cv2.imread("jogador.jpg")
mascara = np.zeros( imagem.shape[:2], dtype="uint8")

"""
for y in range( 0, mascara.shape[0], 1):
    for x in range(0, mascara.shape[1],1):
        mascara[y, x] = (255,255,255)
"""

(cX, cY) = ( imagem.shape[1] //2, imagem.shape[0] // 2 )
cv2.circle( mascara, (cX, cY ), 100, 255, -1)
imagem_com_mascara = cv2.bitwise_and( imagem, imagem, mask=mascara)
cv2.imshow("mascra", imagem_com_mascara )
print( imagem )
