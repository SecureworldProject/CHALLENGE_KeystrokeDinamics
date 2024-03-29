#importamos todas las librerias correspondientes
from  CapturaDatosreturn import capDatos
import lock
import os
from deteclasAnumero import arrayentero,creararray
import numpy as np
from tensorflow import keras

props_dict = {}
DEBUG_MODE = True
url=''

# funcion init devuelve un 0 que es valido ya que suponemos que el usuario va a tener siempre 8un teclado con el que pueda escribir
def init(props):
    global props_dict
    global url
    print("Python: starting challenge init()")
    #cargamos el json que le pasemos y lo guardamos en la variable global
    props_dict = props
    url=props_dict["url"]
    return 0



def executeChallenge():
    print("Python: starting executeChallenge()")
    
    #comprobamos las variables de entorno y cogemos el de SECUREMIRROR_CAPTURES
    dataPath = os.environ['SECUREMIRROR_CAPTURES']
    print ("storage folder is :",dataPath)
    #abrimos lock
    lock.lockIN("keystroke")
    #ejecutamos el codigo de captura de datos 
    datos=capDatos()
    #seleccionamos la dimension de la ventana
    dim=[50,6]
    #tratamos los datos 
    datos=arrayentero(creararray(datos),dim)
    datos=np.array(datos)
       
    #cargamos el modelo
    #############################
    #cambiar la ruta si se pasa por el json
    new_model = keras.models.load_model(url+"path_to_my_model.h5")
    #cerramos el lock
    lock.lockOUT("keystroke")
    #predecimos la cvategoria de los nuevo datos
    new_predictions = new_model.predict(datos)
    print(np.argmax(new_predictions, axis=1))
    # y nos quedamos con la categoria que mas se repite
    cad=np.bincount(np.argmax(new_predictions, axis=1)).argmax()
    #cad es el resultado que vamos a devolver si es modo parental entrara dentro del if y si no. devolvera directamente cad la "categoria"
    
    if props_dict['metodo']=='parental':
        if cad>7:
            #si la categoria es 8 o 9 es el padre o madre por lo tanto devolvera un 1
            cad=0
        else:
            cad=1
            
    #y generamos el resultado
    cad="%d"%(cad)
    key = bytes(cad,'utf-8')
    key_size = len(key)
    result = (key, key_size)
    print("result:", result)
    return result

#
# esta parte del codigo no se ejecuta a no ser que sea llamada desde linea de comandos
if __name__ == "__main__":
    midict = {"metodo":2}
    props_dict = midict
    url='./'
    executeChallenge()
