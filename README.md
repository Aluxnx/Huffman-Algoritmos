# Huffman-Algoritmos
# Huffman-Algoritmos
Reporte del Funcionamiento del Código de Compresión de Huffman 
El código proporcionado implementa un programa de compresión y descompresión de texto utilizando el algoritmo de Huffman, operando a través de una interfaz gráfica de usuario (GUI) creada con tkinter.

Objetivo del Programa:
El propósito de este programa es permitir a los usuarios comprimir y descomprimir archivos de texto mediante el algoritmo de Huffman, que es un método popular de compresión de datos sin pérdida. Este algoritmo utiliza la frecuencia de los caracteres para crear un árbol de codificación, donde los caracteres más frecuentes tienen códigos más cortos.

Definición de la Clase Nodo:
La clase Nodo representa cada nodo en el árbol de Huffman. Contiene atributos para el carácter (char), la frecuencia (freq) y enlaces a los nodos hijo izquierdo (left) y derecho (right). El método __lt__ se sobrecarga para permitir la comparación basada en frecuencias, facilitando el manejo en la cola de prioridades.

Cálculo de Frecuencias:
La función calcular_frecuencias(texto) genera un diccionario con las frecuencias de aparición de cada carácter en el texto. Esta información es esencial para construir el árbol de Huffman.

Construcción del Árbol de Huffman:
Utiliza la estructura de datos de cola de prioridades (heap) para construir el árbol. Los nodos con menor frecuencia se combinan progresivamente hasta que queda un solo nodo que representa el árbol completo.

Generación de Códigos de Huffman:
A partir del árbol de Huffman, esta función asigna un código binario a cada carácter. Los caracteres más frecuentes reciben códigos más cortos.

Compresión y Descompresión:
comprimir(texto, codigos) convierte el texto en una cadena de bits utilizando los códigos de Huffman.
descomprimir(texto_comprimido, codigos) realiza el proceso inverso, reconstruyendo el texto original a partir de la cadena de bits.

Interfaz Gráfica de Usuario:
Se utiliza tkinter para crear una ventana con un botón que permite al usuario seleccionar un archivo y procesar su contenido mostrando las frecuencias, el texto comprimido y el texto descomprimido.

Función de Apertura y Procesamiento de Archivo:
Al hacer clic en el botón, el usuario puede seleccionar un archivo. El programa lee el contenido, ejecuta las funciones de cálculo de frecuencia, construcción de árbol, generación de códigos, compresión y descompresión, y muestra los resultados.

Justificación del Diseño:
El diseño se enfoca en la simplicidad y la enseñanza. Utilizando tkinter, se proporciona una interfaz amigable que oculta la complejidad del algoritmo de Huffman, permitiendo a los usuarios interactuar fácilmente con el programa. El manejo de estructuras como colas de prioridad y la recursividad en la generación de códigos ilustra eficazmente el poder y la eficiencia del algoritmo de Huffman.

Conclusión:
Este programa ofrece una herramienta educativa y práctica para entender y aplicar la compresión de datos mediante el algoritmo de Huffman. La GUI facilita la interacción y visualización de los procesos de compresión y descompresión, haciendo tangibles los conceptos de codificación eficiente basada en frecuencias.
