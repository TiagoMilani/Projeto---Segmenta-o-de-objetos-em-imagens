
#!/usr/bin/env python
# coding: utf-8
import cv2        #biblioteca de cores      
import numpy as np     #biblioteca de matrizes
def imagem(caminho):
    image = cv2.imread(caminho)              #oque chama a imagem
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   #Função que seleciona a cor 

    ret, thresh = cv2.threshold(gray, 0, 255, 
                                cv2.THRESH_BINARY_INV +
                                cv2.THRESH_OTSU) 
    cv2.imshow('imagem', thresh)         #retorna imagem 1

    kernel = np.ones((3, 3), np.uint8) 
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, 
                                kernel, iterations = 2) 
    bg = cv2.dilate(closing, kernel, iterations = 1) 
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
    ret, fg = cv2.threshold(dist_transform, 0.02
                            * dist_transform.max(), 255, 0) 

    cv2.imshow('imagem 2', fg)            #retorna imagem 2

    print(bg)                             #retorna matrix
    cv2.waitKey(0)     
  


