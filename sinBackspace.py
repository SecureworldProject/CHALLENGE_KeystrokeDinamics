from pynput import keyboard as kb
import datetime
import pandas as pd
import numpy as np
tiempopul=[]
tiempointer=[]
Key=[]
Keynum=[]
keynumtemp=0
tiempo=datetime.datetime.now()
combinacion=[]
#hola que tal estas
def difftiempo(temp):
	global tiempo
	resul=temp-tiempo
	tiempo=datetime.datetime.now()
	return resul.total_seconds()
	
def uncombinacion(tecla):
	global keynumtemp
	try:
		if tecla==kb.Key.space or tecla==kb. Key.enter or tecla==kb.Key.backspace or tecla==kb.Key.caps_lock:
			Key.append(str(tecla))
			Keynum.append(tecla.value.vk)
			tiempointer.append(difftiempo(datetime.datetime.now()))
			print(' Se ha pulsado la tecla ' + str(tecla))
		else:
			
			combinacion.index(str(tecla))
	except:
		combinacion.append(str(tecla))
		if keynumtemp==0:
			keynumtemp=tecla.value.vk
		else:
			keynumtemp+=tecla.value.vk
#	
		print(combinacion)
		print(keynumtemp)
#
def pulsa(tecla):
	global combinacion
	global keynumtemp
	if tecla == kb.Key.esc:
		return False
	else:
		try:
			if len(combinacion)==0:
				Key.append( tecla.char)
				
				Keynum.append(tecla.vk)
				tiempointer.append(difftiempo(datetime.datetime.now()))
			else:
				combinacion.append(tecla.char)
				Key.append(str(combinacion))
				keynumtemp+=tecla.vk
				Keynum.append(keynumtemp)
				tiempointer.append(difftiempo(datetime.datetime.now()))
		except AttributeError:
			uncombinacion(tecla)


def suelta(tecla):
	global keynumtemp
	if(len(combinacion)==0):
		print('pulsacion')
		tiempopul.append(difftiempo(datetime.datetime.now())) 
	
		print('Se ha soltado la tecla ' + str(tecla))
	elif(len(combinacion)==1):
		print('pulsacion')
		tiempopul.append(difftiempo(datetime.datetime.now())) 
	
		print('Se ha soltado la tecla ' + str(tecla))
		combinacion.pop(0)
		keynumtemp=0
	else:
		combinacion.pop(0)

	



kb.Listener(pulsa, suelta).run()
print(Key)


datos = pd.concat([pd.DataFrame(tiempopul),pd.DataFrame(tiempointer),pd.DataFrame(Keynum),pd.DataFrame(Key)], axis=1)

print( datos)
print(Keynum)
datos.to_excel('sergio.xlsx')
