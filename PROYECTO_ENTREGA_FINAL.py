"""
Luz Patricia Hernández A01637277
Iker Borja Rios A01637972
Jesús Yael Ramos Armenta A01637426
-> Equipo 1
30/09/22
Entrega 1

"""
from tabulate import tabulate
from tqdm import tqdm
from time import sleep
from datetime import datetime
import winsound
from colorama import Fore, Back, Style
from PIL import Image
import sys 

""" Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL """


def printBanner():
	print(Fore.RED+"""
    ███████╗██╗   ██╗██████╗ ███████╗██████╗ ███╗   ███╗ █████╗ ████████╗██╗  ██╗
    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
    ███████╗██║   ██║██████╔╝█████╗  ██████╔╝██╔████╔██║███████║   ██║   ███████║
    ╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
    ███████║╚██████╔╝██║     ███████╗██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
    ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝""" + Style.RESET_ALL)
printBanner()
print(Back.YELLOW+ Style.BRIGHT+"\n*****************   BIENVENIDOS A SUPERMATH QUEST   *****************\n"+Style.RESET_ALL)
puntaje = 0 
nombre= input("Ingresa tu nombre\n>> ")

def sonidos(sound):#Emitirá un sonido dependiendo si la pregunta es correcta o incorrecta
    if sound==1:
        sound=winsound.Beep(1500,250),winsound.Beep(2000,200) 
    elif sound== 2:
        sound=winsound.Beep(300,350),winsound.Beep(250,200)

def funcionesYecuaciones(puntaje):#
    print(Fore.BLACK+Back.WHITE+"\n*** TEMAS DE FUNCIONES Y ECUACIONES ***"+Style.RESET_ALL+Fore.LIGHTRED_EX+"\na)\tInterecciones en x & y\nb)\tCalcular la pendiente\nc)\tSalir de TEMAS DE FUNCIONES Y ECUACIONES\n"+Style.RESET_ALL)
    user_choice=input("Ingrese una opción\n>> ").lower()
    
    while True:
        while user_choice not in ["a","b","c"]:
            user_choice=input("Ingresa una de las opciones del menu (a,b,c)\n>> ").lower()

        if user_choice=="a":
            print("\n1-Nivel de dificultad 1 ->\t15 pts\n2-Nivel de dificultad 2 ->\t20 pts \n3-Nivel de dificultad 3 ->\t25 pts")
            nivel=int(input("Elige el nivel de dificultad\n>> "))
            while nivel not in [1,2,3]:
                nivel=int(input("Ingresa una de las opciones del menu (1,2,3)\n>> "))
            interxy(nivel,puntaje)
        
        elif user_choice=="b":
            print("\n1-Nivel de dificultad 1 ->\t15 pts\n2-Nivel de dificultad 2 ->\t20 pts \n3-Nivel de dificultad 3 ->\t25 pts")
            nivel=int(input("Elige el nivel de dificultad\n>> "))
            while nivel not in [1,2,3]:
                nivel=int(input("Ingresa una de las opciones del menu (1,2,3)\n>> "))
            pendiente(nivel, puntaje)

        else: 
            print("Has sálido de Funciones y ecuaciones")
            break
        break
    printBanner()
    menu(puntaje)
    return puntaje
    
def interxy(nivel,puntaje): #listo
    tema="interxy"
    explicaciones(tema)
    if nivel==1:
        d_preguntas_N1={"\nIdentifica si cada frase es:\na)\tUna expresión\nb)\tEcuación\nc)\tDesigualdad\n\n4y + 8 = 9\n" : "b","\nIdentifica si cada frase es:\na)\tUna expresión\nb)\tEcuación\nc)\tDesigualdad\n\n3-2\n":"a","\nIdentifica si cada frase es:\na)\tUna expresión\nb)\tEcuación\nc)\tDesigualdad\n\n(7 / y) < 6\n":"c"}

        for pregunta in d_preguntas_N1.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()

            if respuesta == d_preguntas_N1[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)

                puntaje=puntosTotales(puntaje,15)

                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)
        encabezado = ["Termino","Frase"]
        contenido= [["4y + 8 = 9", "Ecuación"],["3-2","Expresión "], ["(7/y)<6","Desigualdad "]]
        TABLA=(tabulate(contenido,encabezado,tablefmt='fancy_grid',colalign=("center",)))
        print(TABLA)

    elif nivel==2:
        d_preguntas_N2={"¿Cuál es la intersección en y de una recta cuya ecuación es y= 5x - 4?\na)\t(4/5,0)\nb)\t(-4,0)\nc)\t(5,-4)\n\n":"a"}
        for pregunta in d_preguntas_N2.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
            if respuesta == d_preguntas_N2[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)

                puntaje=puntosTotales(puntaje,20)

                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)    
    else:
        d_preguntas_N3={"\nHallar el punto de corte (o intersección) entre las siguientes rectas:\ny = 1 - 2x\ny= 3x + 6\na)\t( 2,5 )\nb)\t(1,3)\nc)\t(-1,3)\n\n":"c"} 
        for pregunta in d_preguntas_N3.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
            if respuesta == d_preguntas_N3[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)

                puntaje=puntosTotales(puntaje,25)

                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)   
    funcionesYecuaciones(puntaje)

def pendiente(nivel,puntaje): 
    tema="pendiente"
    explicaciones(tema)
    if nivel==1:
        d_preguntas_N1={"Los puntos (1, 1) y (3, 5) son parte de una recta. ¿Cuál es la pendiente de la recta?\na)\t4\nb)\t2":"2"}
        for pregunta in d_preguntas_N1.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b"]:
                respuesta=input("Ingresa una de las opciones (a,b)\n>> ").lower()
            if respuesta == d_preguntas_N1[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)

                puntaje=puntosTotales(puntaje,25)

                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)   
    elif nivel==2:
        d_preguntas_N2={"Determina la pendiente de una recta que contiene a los puntos (-3, -2) y (2, -7).\na)\t-1\nb)\t-3":"a"}
        for pregunta in d_preguntas_N2.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b"]:
                respuesta=input("Ingresa una de las opciones (a,b)\n>> ").lower()
            if respuesta == d_preguntas_N2[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)

                puntaje=puntosTotales(puntaje,25)

                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound) 
    else:
        im = Image.open("pendienteAngulo.jpeg")
        im=im.show(im)
        d_preguntas_N3={"Obten la pendiente calculando tangente del ángulo\na)\t0.65\nb)\t0.58\nc)\t0.45":"b"}
        for pregunta in d_preguntas_N3.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
            if respuesta == d_preguntas_N3[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)

                puntaje=puntosTotales(puntaje,25)

                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound) 
    funcionesYecuaciones(puntaje)
        

def geo_trig(puntaje): # listo
    print("\n*** TEMAS DE GEMOETRÍA Y TRIGONOMETRÍA ***\na)\tÁreas\nb)\tPerímetros\nc)\tSalir de TEMAS DE GEMOETRÍA Y TRIGONOMETRÍA")
    user_choice=input("Ingrese una opción\n>> ").lower()
    while True:
        while user_choice not in ["a","b","c"]:
            user_choice=input("Ingresa una de las opciones del menu (a,b,c)\n>> ").lower()
            
        if user_choice=="a":
            print("\n1-Nivel de dificultad 1 ->\t15 pts\n2-Nivel de dificultad 2 ->\t20 pts \n3-Nivel de dificultad 3 ->\t25 pts")
            nivel=int(input("Elige el nivel de dificultad\n>> "))
            while nivel not in [1,2,3]:
                nivel=int(input("Ingresa una de las opciones del menu (1,2,3)\n>> "))
            areas(nivel,puntaje)

        elif user_choice=="b":
            print("\n1-Nivel de dificultad 1 ->\t15 pts\n2-Nivel de dificultad 2 ->\t20 pts \n3-Nivel de dificultad 3 ->\t25 pts")
            nivel=int(input("Elige el nivel de dificultad\n>> "))
            while nivel not in [1,2,3]:
                nivel=int(input("Ingresa una de las opciones del menu (1,2,3)\n>> "))
            perimetros(nivel,puntaje)

        else: 
            print("Has sálido de Geometría y trigonometría")
            break
        break
    printBanner()
    menu(puntaje)
    return puntaje
def perimetros(nivel,puntaje): 
    tema="perimetros"
    explicaciones(tema)
    if nivel==1:  
        print("Se mostrará una imagen")
        sleep(2)
        im = Image.open("perimetro1.jpeg")
        im=im.show(im)
        d_preguntas_N1={"Calcula el perimetro\na)\t12 cm\nb)\t8 cm\nc)\t10cm":"a"}
        for pregunta in d_preguntas_N1.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
            if respuesta == d_preguntas_N1[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,15)
                sound=1
                sonidos(sound)
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)

    elif nivel==2:
        print("Se mostrará una imagen")
        sleep(2)
        im = Image.open("perimetro.jpeg")
        im=im.show(im)
        d_preguntas_N2={"Calcula el perimetro de la figura\na)\t58 cm\nb)\t48 cm":"a"}
        for pregunta in d_preguntas_N2.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
            if respuesta == d_preguntas_N2[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,15)
                sound=1
                sonidos(sound)
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)
    else:
        print("Se mostrará una imagen")
        sleep(2)
        im = Image.open("perimetros3.jpeg")
        im=im.show(im)
        d_preguntas_N3={"Calcula el perimetro de la figura\na)\t25 cm\nb)\t24 cm":"b"}
        for pregunta in d_preguntas_N3.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
            if respuesta == d_preguntas_N3[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,15)
                sound=1
                sonidos(sound)
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)
    geo_trig(puntaje)
                 
def areas(nivel,puntaje): #faltan preguntas
    tema="areas"
    explicaciones(tema)
    if nivel==1:  
        print("Se mostrará una imagen")
        sleep(2)
        im = Image.open("perimetro1.jpeg")
        im=im.show(im)
        d_preguntas_N1={"Calcula el area\na)\t8\nb)\t4\nc)\t12":"a"}
        for pregunta in d_preguntas_N1.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b","c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
            if respuesta == d_preguntas_N1[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,15)
                sound=1
                sonidos(sound)
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)

    elif nivel==2:
        print("Se mostrará una imagen")
        sleep(2)
        im = Image.open("perimetro.jpeg")
        im=im.show(im)
        d_preguntas_N2={"Calcula el area de la figura\na)\t192\nb)\t185":"a"}
        for pregunta in d_preguntas_N2.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b"]:
                respuesta=input("Ingresa una de las opciones (a,b)\n>> ").lower()
            if respuesta == d_preguntas_N2[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,15)
                sound=1
                sonidos(sound)
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)
    else:
        print("Se mostrará una imagen")
        sleep(2)
        im = Image.open("perimetros3.jpeg")
        im=im.show(im)
        d_preguntas_N3={"Calcula el area de la figura\na)\t20\nb)\t30":"b"}
        for pregunta in d_preguntas_N3.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b"]:
                respuesta=input("Ingresa una de las opciones (a,b)\n>> ").lower()
            if respuesta == d_preguntas_N3[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,15)
                sound=1
                sonidos(sound)
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)
    geo_trig(puntaje)


def divisibilidad(puntaje):#completo
    print("\n*** TEMAS DE DIVISIBILIDAD ***\na)\tMúltiplos\nb)\tSalir de TEMAS DE DIVISIBILIDAD")
    user_choice=input("Ingrese una opción\n>> ").lower()
    while True:
        while user_choice not in ["a","b"]:
            user_choice=input("Ingresa una de las opciones del menu (a,b,c)\n>> ").lower()

        if user_choice=="a":
            print("\n1-Nivel de dificultad 1 ->\t15 pts\n2-Nivel de dificultad 2 ->\t20 pts \n3-Nivel de dificultad 3 ->\t25 pts")
            nivel=int(input("Elige el nivel de dificultad\n>> "))
            while nivel not in [1,2,3]:
                nivel=int(input("Ingresa una de las opciones del menu (1,2,3)\n>> "))
            multiplos(nivel,puntaje)
        else: 
            print("Has sálido de Divisibilidad")
            break
        break
    printBanner()
    menu(puntaje)
    return puntaje
def multiplos(nivel,puntaje): #completo
    tema="multiplos"
    explicaciones(tema)
    if nivel==1:
        d_preguntas_N1={"\n¿Es  540720 divisible entre 10?\na)\tsí\nb)\tno":"a", "\nEs 313756 divisible entre 2\na)\tsí\nb)\tno":"a"}
        for pregunta in d_preguntas_N1.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b"]:
                respuesta=input("Ingresa una de las opciones (a,b)\n>> ").lower()
            if respuesta == d_preguntas_N1[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,15)
                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)
    elif nivel==2:
        d_preguntas_N2={"\n¿El 2 es factor o múltiplo de 16?\na)\tmútiplo\nb)\tfactor":"b","\n¿El 32 es múltiplo o factor de 16?\na)\tmútiplo\nb)\tfactor":"a"}
        for pregunta in d_preguntas_N2.keys():
            respuesta = input(f"{pregunta}\n>>> ")
            while respuesta not in ["a","b"]:
                respuesta=input("Ingresa una de las opciones (a,b)\n>> ").lower()
            if respuesta == d_preguntas_N2[pregunta]:
                print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,20)
                sound=1
                sonidos(sound)                
            else:
                print(Back.RED+"Incorrecto :// "+Style.RESET_ALL)
                puntaje=puntosTotales(puntaje,0)
                sound=2
                sonidos(sound)
    else:
        print("\nA continuación, se mostrará una imagen. Observe el problema")
        sleep(3)    
        im = Image.open("preguntaSILLA.jpeg")
        im=im.show(im)
        respuesta=input("Según el planteamiento ¿cuál es el número mayor de estudiantes que puede haber por filas?\na)\t27\nb)\t18\nc)\t8\n >> ").lower()
        while respuesta not in ["a","b", "c"]:
                respuesta=input("Ingresa una de las opciones (a,b,c)\n>> ").lower()
        if respuesta == "b":
            print(Back.GREEN+"\nCorrecto :) "+Style.RESET_ALL)
            puntaje=puntosTotales(puntaje,25)
            sound=1
            sonidos(sound)                
        else:
            print(Back.RED+"Incorrect :// "+Style.RESET_ALL)
            puntaje=puntosTotales(puntaje,0)
            sound=2
            sonidos(sound)
    divisibilidad(puntaje)
  
def explicaciones(tema): #listo
    print(Back.WHITE+Fore.BLUE+"EXPLICACIÓN TEMA"+Style.RESET_ALL)
    if tema=="interxy":
        print(Fore.GREEN+"\n<<Cuando una recta intersecta dos ejes de coordenadas, el punto donde la recta cruza el eje x se llama intersección en x y el punto donde la recta cruza el eje y intersección en y.>>\n"+Fore.LIGHTMAGENTA_EX+"Has click en el siguiente link para ver la explicaión de un video de YouTube:\n->"+Fore.BLUE+"_https://youtu.be/BFegi8hlUd4_"+Style.RESET_ALL)
        print(Fore.YELLOW+"\nPara encontrar la intersección en y, sustituimos 0 por x en la ecuación, porque cada punto en el eje y tiene un valor de 0 en la coordenada x.")
        print("\nA continuación, se mostrará una imagen")
        im = Image.open("intersecciones ejemplo.jpg")
        im=im.show(im)
        sleep(3)
    elif tema=="pendiente":
        print(Fore.GREEN+"\n<<La pendiente se calcula como desplazamiento vertical entre el desplazamiento horizontal (cambio en y dividido entre el cambio en x).>>\n"+Fore.LIGHTMAGENTA_EX+"Has click en el siguiente link para ver la explicaión de un video de YouTube:\n->"+Fore.BLUE+"_https://youtu.be/ULxjPNTiAZ8_" + Style.RESET_ALL)
       
    elif tema=="perimetros":
        print(Fore.GREEN+"\nEl perímetro de una figura plana es igual a la suma de las longitudes de sus lados.\n"+Fore.LIGHTMAGENTA_EX+"Has click en el siguiente link para ver la explicaión de un video de YouTube:\n->"+Fore.BLUE+"_https://youtu.be/QtHQFAbgdPU_"+Style.RESET_ALL)
    elif tema=="areas":
        print(Fore.GREEN+"\n<<El área puede ser definida como la medida de la superficie, y se obtiene partir de multiplicar la base por la altura.>>\n"+Fore.LIGHTMAGENTA_EX+"Has click en el siguiente link para ver la explicaión de un video de YouTube:\n->"+Fore.BLUE+"_https://youtu.be/5z3h53xQVq0_" + Style.RESET_ALL)
    
    elif tema=="numprimos":
        print(Fore.GREEN+"\n<<Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, que si intentamos dividirlos por cualquier otro número, el resultado no es entero.>>\n"+Fore.LIGHTMAGENTA_EX+"Has click en el siguiente link para ver la explicaión de un video de YouTube:\n->"+Fore.BLUE+"_https://youtu.be/VB0vwQ6YbME_" +Style.RESET_ALL)
    elif tema== "multiplos":
        print(Fore.GREEN+"\n<<Los múltiplos de un número son todos los posibles resultados de multiplicar ese número por todos los números naturales.>>\n"+Fore.LIGHTMAGENTA_EX+"Has click en el siguiente link para ver la explicaión de un video de YouTube:\n->"+Fore.BLUE+"_ https://www.youtube.com/watch?v=7XNeElmBk9I"+Style.RESET_ALL)

def puntosTotales(puntaje,puntos): 
     puntaje += puntos
     print(Fore.GREEN+f"Tu puntaje es: {puntaje} puntos "+Style.RESET_ALL)
     return puntaje
"""
    It takes two arguments, adds them together, and returns the result
    
    :param puntaje: The total score
    :param puntos: The points you get for the question
    :return: the value of the variable "puntaje"
    """

def menu(puntaje):

    while True:
        print(Fore.BLUE+"Práctica tus habilidades matemáticas resolviendo ejercicios."+Fore.GREEN+ Back.WHITE+ Style.BRIGHT+"\n>>> INSTRUCCIONES:\n" + Style.RESET_ALL + Fore.GREEN+ "\n->\tPor cada pregunta que respondas correctamente, obtendras puntos\n->\tIntenta contestar la mayor cantidad de preguntas")
        print(Fore.MAGENTA+"Dependiendo de la dificultad de la pregunta seran los puntos que obtendras:")
        print("\n1-Nivel de dificultad 1 ->\t15 pts\n2-Nivel de dificultad 2 ->\t20 pts \n3-Nivel de dificultad 3 ->\t25 pts\n")
        print(Fore.YELLOW+ Back.WHITE+ Style.BRIGHT+"<<< MENU PRINCIPAL >>>"+Back.RESET+Fore.YELLOW+Style.NORMAL+"\na)\tFunciones y ecuaciones\nb)\tDivisibilidad\nc)\tGeometría y trigonometría\nd)\t"+Fore.LIGHTRED_EX+"Salir del programa")
        
        # Asking the user to input a letter from a to d.
        user_choice=input(Fore.YELLOW+Style.BRIGHT+"Ingrese un tema para prácticar ejercicios (a,b,c,d)\n>> "+Style.RESET_ALL).lower()
        while user_choice not in ["a","b","c","d"]:
            user_choice=input("Escoge una de las opciones del menu (a,b,c,d)\n>> ").lower()
    
        if user_choice=="a":
            funcionesYecuaciones(puntaje)

        elif user_choice=="b":
            divisibilidad(puntaje)

        elif user_choice=="c":
            geo_trig(puntaje)
        else: 
            print(f"Gracias por utilizar SUPERMATH QUEST,"+Fore.GREEN+f" tu puntaje fue de {puntaje}"+Style.RESET_ALL)

            # A progress bar.
            for i in tqdm(range(100), desc=Fore.MAGENTA+"El programa está agregando sus resultados al registro de resultados. Espere..."):
                sleep(0.01)

            archivo = open( 'Registro_juego','r')
            contenido = archivo.read()
            print(contenido)
            archivo.close()
            print("Referencias\n-\thttps://www.problemasyecuaciones.com/geometria2D/interseccion/rectas-parabolas-interseccion-punto-ejemplos-problemas-resueltos.html\n-\thttps://es.khanacademy.org/math/2-secundaria-pe")
            sys.exit("")
        break
        

# Writing the name of the user and the date in a file called "Registro_juego"
now = datetime.now()
archivo = open("Registro_juego","a")
archivo.write("\n**** Historial de usuarios ****")
archivo.write('\nFecha: '+ str(now))
archivo.write('\nNombre usuario: '+ nombre)
archivo.close()
menu(puntaje)