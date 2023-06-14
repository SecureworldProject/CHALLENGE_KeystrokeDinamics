#importamos todas las librerias correspondientes
from  CapturaDatosreturn import capDatos
import lock
import os
from deteclasAnumero import arrayentero,creararray
import numpy as np
from tensorflow import keras

props_dict = {}
DEBUG_MODE = True

# funcion init devuelve un 0 que es valido ya que suponemos que el usuario va a tener siempre 8un teclado con el que pueda escribir
def init(props):
    global props_dict
    print("Python: starting challenge init()")
    #cargamos el json que le pasemos y lo guardamos en la variable global
    props_dict = props
    return 0



def executeChallenge():
    print("Python: starting executeChallenge()")
    url=props_dict["url"]
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
    midict = {}
    init(midict)
    executeChallenge()
