import numpy as np
from CapturaDatosreturn import capDatos

#funcion en la que trasforma una letra (tecla) en numero para ello lee un array de numpy y asigna un numero que es la posicion dentro del array y si hay un error devuelve 'error'
def teclasNum(STRtecla):
    #para los test de bufalo
    teclas=np.load("teclas.npy")
    try:
        return np.where(teclas==STRtecla)[0][0]/len(teclas)
    except:
        print(STRtecla)

#te genera un array con los datos introducidos con la tecnica de ventana deslizante. la longitud de la ventana deslicante es el primer elemnto del array dim y te genera otro array con el mismo
# tamaño que el array X con el numero pasado en la funcion (num) para que se utilice como el numero de categoria (la prediccion Y_train)
#posibilidad de no devolver el array de etiquetas cuando num = none (no pasar el parametro num)

def arrayentero(array,dim, num=None):
    Y_array=[]
    X_array=[]
    #trasformamos el array en float
    array=np.array(array,dtype='float16')
    #guardamos la dimension de la ventana en una variable
    ventana=dim[0]
    if num is not None:
        #recorremos todos los elementos del array hasta N-longitud de la ventana y lo guardamos en un nuevo array y generamos el array de etiquetas con el num
        for i in range(0,len(array)-ventana):
            X_array.append(array[i:ventana+i,:])
            Y_array.append([num])
        Y_array=np.array(Y_array)
        return X_array,Y_array
    else:
        #recorremos todos los elementos del array hasta N-longitud de la ventana y lo guardamos en un nuevo array
        for i in range(0,len(array)-ventana):
            X_array.append(array[i:ventana+i,:])
        return X_array


#creamos el array con los tiempos oportunos
def creararray(teclas):
    vector=[]
    aux_UD=0
    aux_DD=0
    tmax=1000
    #recorremos todos los elementos del array
    for i in range(len(teclas)):
        if teclas[i][1]=='KeyDown':
            #recorremos todos los elemntos del array desde la posicion i hasta que encuentre el primer vector que contenga la tecla y keyup 
            for j in range(i,len(teclas)):
            
                if teclas[j][1]=='KeyUp' and teclas[j][0]==teclas[i][0] :
                    try:
                        #generamos los tiempos y los introducimos en el elemento anterior  y añadimos un nuevo elemento dentro del array
                        #tiempos
                        HOLD=abs(int(teclas[i][2])/tmax-int(teclas[j][2])/tmax)
                        UD=abs(aux_UD-int(teclas[i][2]))/tmax
                        DD=abs(aux_DD-int(teclas[i][2]))/tmax
                        #genera ['a',hold,'b',hold,UD,DD] si es el primer elemento da error y va al except
                        vector[-1].extend([teclasNum(teclas[i][0]),HOLD,UD,DD])
                        #genera ['b',hold]
                        vector.append([teclasNum(teclas[i][0]),HOLD])
                        #y guardamos en dos variables el up y el down para generar el UD y el DD 
                        aux_UD=int(teclas[j][2])
                        aux_DD=int(teclas[i][2])
                        break
                    except:
                        #guardamos en dos variables el up y el down para generar el UD y el DD 
                        aux_UD=int(teclas[j][2])
                        aux_DD=int(teclas[i][2])
                        #operacion para sacar el hold de la tecla
                        HOLD=abs(int(teclas[i][2])/tmax-int(teclas[j][2])/tmax)
                        #genera ['b',hold]
                        vector.append([teclasNum(teclas[i][0]),HOLD])
                        break
    #eliminamos el ultimo elemento que esta incompleto
    vector.pop(-1)
    #trasformamos el array en un vector de numpy
    vector=np.array(vector)
    #retornamos el vector
    return vector

#cargamos los datos en este caso los de bufalo

def leerdatos(dim):
    X_train=np.load("datos2/alberto1.npy")
    X_trainf,Y_trainf=arrayentero(creararray(X_train),dim,0)


    X_train=np.load("datos2/alberto2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,0)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/bea1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,1)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/bea2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,1)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))
    
    X_train=np.load("datos2/christin21.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,2)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/christina1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,2)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/laura1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,3)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/laura2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,3)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/maria1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,4)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/maria2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,4)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/pepe1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,5)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/pepe2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,5)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/pilar1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,6)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/pilar2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,6)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/yaiza1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,7)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/yaiza2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,7)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/yeyo1.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,8)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.load("datos2/yeyo2.npy")
    X_train,Y_train =arrayentero(creararray(X_train),dim,8)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=capDatos()
    X_train,Y_train =arrayentero(creararray(X_train),dim,9)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=capDatos()
    X_train,Y_train =arrayentero(creararray(X_train),dim,9)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))



    
    return  X_trainf,Y_trainf

def leerdatosbufalo(dim):
    X_train=np.loadtxt("datos3/002000.txt", dtype='str')
    X_trainf,Y_trainf=arrayentero(creararray(X_train),dim,0)


    X_train=np.loadtxt("datos3/003000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,1)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.loadtxt("datos3/004000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,2)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.loadtxt("datos3/005000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,3)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.loadtxt("datos3/006000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,4)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    """
    X_train=np.loadtxt("datos3/006000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,5)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.loadtxt("datos3/007000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,6)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.loadtxt("datos3/008000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,7)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))

    X_train=np.loadtxt("datos3/009000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,8)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))


    X_train=np.loadtxt("datos3/010000.txt", dtype='str')
    X_train,Y_train =arrayentero(creararray(X_train),dim,9)
    X_trainf=np.concatenate((X_trainf,X_train))
    Y_trainf=np.concatenate((Y_trainf,Y_train))
    """

    #creamos la y y algunos parametros para el modelo de la red neuronal

    ############################################################################################   datos test

    X_test=np.loadtxt("datos3/002001.txt", dtype='str')
    X_testf,Y_testf=arrayentero(creararray(X_test),dim,0)

    X_test=np.loadtxt("datos3/003001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,1)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))

    X_test=np.loadtxt("datos3/004001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,2)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))

    X_test=np.loadtxt("datos3/005000.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,3)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))


    X_test=np.loadtxt("datos3/006001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,4)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))


    """
    X_test=np.loadtxt("datos3/006001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,5)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))

    X_test=np.loadtxt("datos3/007001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,6)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))

    X_test=np.loadtxt("datos3/008001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,7)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))

    X_test=np.loadtxt("datos3/009001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,8)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))

    X_test=np.loadtxt("datos3/010001.txt", dtype='str')
    X_test,Y_test =arrayentero(creararray(X_test),dim,9)
    X_testf=np.concatenate((X_testf,X_test))
    Y_testf=np.concatenate((Y_testf,Y_test))
    """
    #print(len(X_trainf))
    return  X_trainf,Y_trainf, X_testf,Y_testf