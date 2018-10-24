import cv2

imagem = cv2.imread( 'jogador.jpg')
recorte = imagem[220:280, 248:304]

cv2.imshow('output', recorte)
