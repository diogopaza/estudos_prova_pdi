import cv2

imagem = cv2.imread( "jogador.jpg ")
for y in range( 0, imagem.shape[0], 1):#percorre linhas
   for x in range( 0, imagem.shape[1],1):#percorre colunas
       imagem[x, y ]= (255,255,255)#deixa imagem em branco
cv2.imshow('input', imagem)
