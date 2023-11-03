import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, LSTM,SimpleRNN,GRU,BatchNormalization,Input
import tensorflow as tf
from deteclasAnumero import leerdatosbufalo,leerdatos

#--------------------------------------------------------
#importamos los datos para analizarlos en la red neuronal
#dimension de entrada de la red neuronal el primer digito es el tamaño de la ventana el otro se mantiene siempre
dim=[50,6]#modificable
#cargamos el dataset con el que vamos a entrenar  a la red neuronal
#
#metodo1=modo empresarial
#metodo 2=modo parental

metodo=1

X_trainf,Y_trainf=leerdatos(dim,metodo)

#---------------------------------------------------------
#creamos el modelo
dim_salida = 10
na =16

modelo = Sequential()
modelo.add(Input(shape=dim))
modelo.add(GRU(units=na))

modelo.add(BatchNormalization())
modelo.add(Dense(dim_salida, activation='softmax'))
#imprimimos el modelo escogido
print(modelo.summary())

#seleccionamos el compilador y las metricas
modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=["accuracy"])
#sgd  adam

#barajamos los datos para que no esten seguidos

X_trainf=tf.random.shuffle(X_trainf, seed=1234)
Y_trainf=tf.random.shuffle(Y_trainf, seed=1234)

# entremnamos el modelo
modelo.fit(X_trainf,Y_trainf,
           #validation_data=(X_testf, Y_testf),
           epochs=60
           #callbacks=[tensorboard_callback,cm_callback]
           )
#guardamos el modelo en la misma carpeta aunque se puede pasar una ruta especifica

########################################
#pensamos si pasar la ruta por el json
modelo.save('path_to_my_model.h5')



   
