import cv2 as cv
import numpy as np
import csv

#botar o video na mesma pasta desse código, inserir o nome do video entre as aspas
video = 'pendulo.mp4'
videoCapture = cv.VideoCapture(video) 

fps = videoCapture.get(cv.CAP_PROP_FPS)

#ARMAZENA DADOS PRO GRÁFICO
posicao_x=[]
posicao_y=[]
tempos=[]
n_frames = 0


while True: 
    ret, frame = videoCapture.read() #vai retornar um booleano para caso o frame foi obtido ou não

    if not ret: break #interrompe o loop caso falhou em pegar o frame


    #corta o video para não aparecer o quadro no fundo, evitando de aparecer circulos indesejados
    altura, largura = frame.shape[:2]
    frame_cortado = frame[int(altura*0.15):, int(largura*0.22):]
    

    #transforme o video em preto e branco, e depois usa o gaussian blur. Ajuda na remoção de ruido do video
    cinza = cv.cvtColor(frame_cortado, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(cinza, (7,7), 0) 

    #bota as circunferencias numa lista
    circulos = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1.2, 150, param1=80, param2=40, minRadius=20, maxRadius=60)

    #se detectou circulos
    if circulos is not None:
        circulos = np.uint16(np.around(circulos[0, :]))  #converte os numeros arredondados para o tipo de dado inteiro, arredonda os valores de ponto flutuante para int

        #desenha os circulos e o centro dele
        for(x,y,r) in circulos:
            cv.circle(frame_cortado, (x,y), r, (0,255,0), 2)
            cv.circle(frame_cortado, (x,y), 2, (0,0,255),3)

        #salva as posições x, y do pendulo, e salva os tempos através da fórmula de calcular o tempo de um video através do fps 
        posicao_x.append(x)
        posicao_y.append(y)
        tempos.append(n_frames/fps)  


    n_frames+=1


    cv.imshow("pendulo", frame_cortado)
    if cv.waitKey(1) & 0xFF == ord('q'): break #espera um milissegundo, e se apertar a tecla 'q' encerra o programa


#libera a captura do video e fecha a janela aberta
videoCapture.release() 
cv.destroyAllWindows()

if tempos:
    with open('dados.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y', 't'])
        for x, y, t in zip(posicao_x, posicao_y, tempos):
            writer.writerow([x, y, t])