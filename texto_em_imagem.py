import cv2

imagem = cv2.imread( "jogador.jpg")

cv2.putText( imagem, 'Jogador', (280,65), cv2.FONT_HERSHEY_SIMPLEX,  1.0, (255,255,255), lineType=cv2.LINE_AA)
cv2.imshow( "output", imagem)
