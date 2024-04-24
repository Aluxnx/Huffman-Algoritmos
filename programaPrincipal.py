import tkinter as tk
from tkinter import filedialog
import heapq
import os

# Definición de la clase Nodo que representará cada nodo en el árbol de Huffman.
class Nodo:
    def __init__(self, char, freq):
        self.char = char  # Carácter del nodo
        self.freq = freq  # Frecuencia del carácter
        self.left = None  # Enlace al nodo hijo izquierdo
        self.right = None  # Enlace al nodo hijo derecho

    def __lt__(self, other):
        # Permite que Python compare dos nodos usando su frecuencia
        return self.freq < other.freq

# Función para calcular la frecuencia de cada carácter en el texto.
def calcular_frecuencias(texto):
    frecuencias = {}
    for char in texto:
        if char not in frecuencias:
            frecuencias[char] = 0
        frecuencias[char] += 1
    return frecuencias

# Función para construir el árbol de Huffman usando una cola de prioridad (heap).
def construir_arbol(frecuencias):
    heap = []
    # Crea un heap inicial con todos los caracteres y sus frecuencias.
    for char, freq in frecuencias.items():
        heapq.heappush(heap, (freq, Nodo(char, freq)))
    
    # Combina los dos nodos menos frecuentes hasta que solo queda un nodo en el heap.
    while len(heap) > 1:
        freq1, nodo1 = heapq.heappop(heap)
        freq2, nodo2 = heapq.heappop(heap)
        nodo = Nodo(None, freq1 + freq2)
        nodo.left = nodo1
        nodo.right = nodo2
        heapq.heappush(heap, (freq1 + freq2, nodo))
    
    return heap[0][1]

# Función para generar los códigos de Huffman de cada carácter.
def generar_codigos(nodo, prefijo="", codigo={}):
    if nodo.char is not None:  # Si el nodo es una hoja, asocia el código actual al carácter
        codigo[nodo.char] = prefijo
    else:  # De lo contrario, continúa por el árbol
        generar_codigos(nodo.left, prefijo + "0", codigo)
        generar_codigos(nodo.right, prefijo + "1", codigo)
    return codigo

# Función para comprimir el texto original en una cadena de bits usando los códigos de Huffman.
def comprimir(texto, codigos):
    return ''.join(codigos[char] for char in texto)

# Función para descomprimir el texto comprimido.
def descomprimir(texto_comprimido, codigos):
    inv_codigos = {v: k for k, v in codigos.items()}  # Invierte el diccionario de códigos
    current_code = ""
    decompressed_text = ""
    
    for bit in texto_comprimido:
        current_code += bit
        if current_code in inv_codigos:  # Si el código actual corresponde a un carácter, agrégalo al texto
            decompressed_text += inv_codigos[current_code]
            current_code = ""
    
    return decompressed_text

# Función que se ejecuta al presionar el botón de la GUI. Permite seleccionar un archivo y procesar su contenido.
def abrir_archivo():
    filepath = filedialog.askopenfilename()  # Abre un cuadro de diálogo para seleccionar un archivo
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            texto = file.read()
        
        frecuencias = calcular_frecuencias(texto)
        arbol = construir_arbol(frecuencias)
        codigos = generar_codigos(arbol)
        texto_comprimido = comprimir(texto, codigos)
        texto_descomprimido = descomprimir(texto_comprimido, codigos)
        
        text_widget.delete('1.0', tk.END)  # Limpia el widget de texto
        # Muestra las frecuencias y el texto comprimido/descomprimido en la GUI
        text_widget.insert(tk.END, "Frecuencias:\n" + str(frecuencias) + "\n")
        text_widget.insert(tk.END, "Texto Comprimido:\n" + texto_comprimido + "\n")
        text_widget.insert(tk.END, "Texto Descomprimido:\n" + texto_descomprimido + "\n")

# Configuración de la interfaz gráfica de usuario (GUI)
root = tk.Tk()
root.title("Compresor Huffman Simplificado")

text_widget = tk.Text(root, height=20, width=100)
text_widget.pack(padx=10, pady=10)

btn_examinar = tk.Button(root, text="Examinar y Procesar", command=abrir_archivo)
btn_examinar.pack(pady=20)  # Coloca el botón en la ventana principal con un padding vertical

# Inicia el bucle principal de la aplicación que mantiene la ventana abierta
root.mainloop()