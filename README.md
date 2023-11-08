# CHALLENGE_KeystrokeDinamics
<h2>CHALLENGE_KeystrokeDinamics</h2>
<p>La dinámica de pulsaciones de teclas (keystroke dynamics, en inglés) es una técnica de biometría conductual que se utiliza para identificar o autenticar a un individuo según su patrón de escritura en el teclado. Para ello se usa una red neuronal entrenada con los patrones de varios usuarios. por consiguiente para ejecutar el challenge es necesario haber hecho un enrollment (entrenamiento) previo con el usuario.
</p>
<h3>descripcion de ficheros</h3>
<p><ul>CapturaDatosreturn.py: Este archivo contiene un método que genera un juego y devuelve los tiempos y los ID de cada tecla capturada.</ul>
<ul>crearBBD.py: En este archivo se encuentra el código para generar un modelo y entrenarlo.</ul>
<ul>keystroke.py: Este archivo utiliza el método de captura de datos mencionado anteriormente y, utilizando los datos capturados, realiza predicciones sobre el modelo entrenado anteriormente.</ul>
<ul>teclas.npy: Este archivo contiene todos los IDs correspondientes a las teclas de un teclado normal. Se utiliza para generar los ID necesarios en el proceso.</ul>
<ul>deteclasAnumero.py: En este archivo se encuentra el código que transforma las teclas en IDs.</ul>
</p>
