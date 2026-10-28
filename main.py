import cv2 as cv
import numpy as np

#botar o video na mesma pasta desse código, inserir o nome do video entre as aspas
video = 'pendulo.mp4'
videoCapture = cv.VideoCapture(video) 

while True: 
    ret, frame = videoCapture.read() #vai retornar um booleano para caso o frame foi obtido ou não

    if not ret: break #interrompe o loop caso falhou em pegar o frame

    #transforme o video em preto e branco, e depois usa o gaussian blur. Ajuda na remoção de ruido do video
    cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(cinza, (17,17), 0) 


    cv.imshow("pendulo", blur)
    if cv.waitKey(1) & 0xFF == ord('q'): break #espera um milissegundo, e se apertar a tecla q encerra o programa


#libera a captura do video e fecha a janela aberta
videoCapture.release() 
cv.destroyAllWindows()