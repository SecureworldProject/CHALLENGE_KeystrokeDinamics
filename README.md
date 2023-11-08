# CHALLENGE_KeystrokeDinamics
<h2>CHALLENGE_KeystrokeDinamics</h2>
<p>La dinámica de pulsaciones de teclas (keystroke dynamics, en inglés) es una técnica de biometría conductual que se utiliza para identificar o autenticar a un individuo según su patrón de escritura en el teclado. Para ello se usa una red neuronal entrenada con los patrones de varios usuarios. por consiguiente para ejecutar el challenge es necesario haber hecho un enrollment (entrenamiento) previo con el usuario.
</p>
<h3>descripcion de ficheros</h3>
<p>
  <ul>
<li>CapturaDatosreturn.py: Este archivo contiene un método que genera un juego y devuelve los tiempos y los ID de cada tecla capturada.</li>
<li>crearBBD.py: En este archivo se encuentra el código para generar un modelo y entrenarlo.</li>
<li>keystroke.py: Este archivo utiliza el método de captura de datos mencionado anteriormente y, utilizando los datos capturados, realiza predicciones sobre el modelo entrenado anteriormente.</li>
<li>teclas.npy: Este archivo contiene todos los IDs correspondientes a las teclas de un teclado normal. Se utiliza para generar los ID necesarios en el proceso.</li>
<li>deteclasAnumero.py: En este archivo se encuentra el código que transforma las teclas en IDs.</li>
  </ul>
</p>
<h3>modos de funcionamiento</h3>
<p>este challenge tiene dos modos de funcionamiento: modo parental y modo empresarial</p>
<p>
  <ul>
    <li>
      modo empresarial:devuelve un valor entre 0 a 10.
    </li>
    <li>
      modo parental:devuelve un 1 si es padre o madre y un 0 si no es padre y madre
    </li>
  </ul>
</p>
