import cv2
import numpy as np                         #Importamos Numpy


imagen = cv2.imread('imagen.jpg')          #abrimos la imagen

largo=imagen.shape[1]                      #Extraigo el largo de la imagen

alto=imagen.shape[0]                       #Extraigo el alto de la imagen

corte=imagen[0:alto//2, 0:largo]           #Hacemos el corte, o mas bien la redimesion de mi matriz [empiezo en y:termino en y+altura, empiezo en x:termino en x+largo ]

cv2.imwrite('imagen_recortada.jpg',corte)  #Usamos esta funcion para guardarla en jpg

#cv2.imshow("Imagen recortada", corte)      #Muestro la imagen

#Comentario hecho desde el server

cv2.waitKey(0) 



