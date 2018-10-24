import cv2

imagem = cv2.imread( "jogador.jpg ")
(b, g, r) = imagem[0,0]
print(b, g, r)

cv2.imshow('input', imagem)
