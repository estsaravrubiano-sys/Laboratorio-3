import tkinter as tk

from Documento import Documento
from cola import cola


# ---------- VARIABLES ----------

cola = cola()

imprimiendo = False

documento_actual = None

pagina_actual = 0


# ---------- FUNCIONES ----------

def agregar_documento():

    nombre = entrada_nombre.get()
    paginas = int(entrada_paginas.get())
    tiempo = float(entrada_tiempo.get())

    documento = Documento(nombre, paginas, tiempo)

    cola.agregar(documento)

    entrada_nombre.delete(0, tk.END)
    entrada_paginas.delete(0, tk.END)
    entrada_tiempo.delete(0, tk.END)

    mostrar_cola()


def mostrar_cola():

    texto_cola.delete("1.0", tk.END)

    if cola.esta_vacia():

        texto_cola.insert(
            tk.END,
            "No hay documentos en cola"
        )

    else:

        for documento in cola.documentos:

            texto_cola.insert(
                tk.END,
                documento.nombre +
                " - " +
                str(documento.paginas) +
                " páginas - " +
                str(documento.tiempo) +
                " segundos\n"
            )


def iniciar_impresion():

    global imprimiendo
    global documento_actual
    global pagina_actual

    if cola.esta_vacia():

        etiqueta_estado.config(
            text="No hay documentos en cola"
        )

    else:

        imprimiendo = True

        documento_actual = cola.primero()

        pagina_actual = 1

        imprimir_pagina()


def imprimir_pagina():

    global pagina_actual
    global documento_actual
    global imprimiendo

    if imprimiendo == True:

        etiqueta_estado.config(
            text="Imprimiendo: " +
            documento_actual.nombre
        )

        texto_impresion.insert(
            tk.END,
            "Página " +
            str(pagina_actual) +
            " de " +
            str(documento_actual.paginas) +
            "\n"
        )

        if pagina_actual < documento_actual.paginas:

            pagina_actual = pagina_actual + 1

            ventana.after(
                int(documento_actual.tiempo * 1000),
                imprimir_pagina
            )

        else:

            texto_impresion.insert(
                tk.END,
                documento_actual.nombre +
                " terminado\n\n"
            )

            cola.sacar()

            mostrar_cola()

            if cola.esta_vacia():

                imprimiendo = False

                etiqueta_estado.config(
                    text="No hay documentos en cola"
                )

            else:

                documento_actual = cola.primero()

                pagina_actual = 1

                ventana.after(
                    int(documento_actual.tiempo * 1000),
                    imprimir_pagina
                )


def detener_impresion():

    global imprimiendo

    imprimiendo = False

    etiqueta_estado.config(
        text="Impresión detenida"
    )

    texto_impresion.insert(
        tk.END,
        "Impresión detenida\n\n"
    )


# ---------- VENTANA ----------

ventana = tk.Tk()

ventana.title("Simulador de impresión")

ventana.geometry("600x650")

ventana.configure(bg="plum1")


# ---------- TÍTULO ----------

titulo = tk.Label(
    ventana,
    text="SIMULADOR DE IMPRESORA",
    font=("arial", 20),
    bg="plum1"
)

titulo.place(x=160, y=20)


# ---------- NUEVO DOCUMENTO ----------

frame1 = tk.LabelFrame(
    ventana,
    text="Nuevo documento",
    font=("arial", 12),
    bg="white",
    width=500,
    height=180
)

frame1.place(x=50, y=70)


# Nombre

etiqueta1 = tk.Label(
    frame1,
    text="Nombre:",
    font=("arial", 12),
    bg="white"
)

etiqueta1.place(x=20, y=25)


entrada_nombre = tk.Entry(
    frame1,
    font=("arial", 12)
)

entrada_nombre.place(x=150, y=25)


# Número de páginas

etiqueta2 = tk.Label(
    frame1,
    text="Número de páginas:",
    font=("arial", 12),
    bg="white"
)

etiqueta2.place(x=20, y=65)


entrada_paginas = tk.Entry(
    frame1,
    font=("arial", 12)
)

entrada_paginas.place(x=180, y=65)


# Tiempo por página

etiqueta3 = tk.Label(
    frame1,
    text="Tiempo por página:",
    font=("arial", 12),
    bg="white"
)

etiqueta3.place(x=20, y=105)


entrada_tiempo = tk.Entry(
    frame1,
    font=("arial", 12)
)

entrada_tiempo.place(x=180, y=105)


# Botón agregar

boton_agregar = tk.Button(
    frame1,
    text="Agregar documento",
    command=agregar_documento
)

boton_agregar.place(x=180, y=140)


# ---------- COLA DE IMPRESIÓN ----------

frame2 = tk.LabelFrame(
    ventana,
    text="Cola de impresión",
    font=("arial", 12),
    bg="white",
    width=500,
    height=130
)

frame2.place(x=50, y=270)


texto_cola = tk.Text(
    frame2,
    width=55,
    height=5,
    font=("arial", 10)
)

texto_cola.place(x=10, y=5)


# ---------- ÁREA DE IMPRESIÓN ----------

frame3 = tk.LabelFrame(
    ventana,
    text="Área de impresión",
    font=("arial", 12),
    bg="white",
    width=500,
    height=120
)

frame3.place(x=50, y=410)


texto_impresion = tk.Text(
    frame3,
    width=55,
    height=5,
    font=("arial", 10)
)

texto_impresion.place(x=10, y=5)


# ---------- ESTADO ----------

etiqueta_estado = tk.Label(
    ventana,
    text="Estado: Impresora detenida",
    font=("arial", 12),
    bg="plum1"
)

etiqueta_estado.place(x=170, y=540)


# ---------- BOTÓN INICIAR ----------

boton_iniciar = tk.Button(
    ventana,
    text="Iniciar impresión",
    command=iniciar_impresion
)

boton_iniciar.place(x=170, y=580)


# ---------- BOTÓN DETENER ----------

boton_detener = tk.Button(
    ventana,
    text="Detener impresión",
    command=detener_impresion
)

boton_detener.place(x=320, y=580)


ventana.mainloop()