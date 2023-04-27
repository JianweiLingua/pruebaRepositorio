#! /usr/bin/env python
# -*-enconding: utf-8 -*-
class Ejercicio:
    # Menú
    def menu(self):
        import csv
        from xml.dom import minidom
        import glob
        import os
        
        CAMBIOS = 32
        
        array = []
        # array_idiomas = []
        array_numeros = []
        # array_palabras = []
        # Bucle infinito
        while True:
            print("1. Generar archivos XML.")
            print("2. Mostrar los idiomas con sus cantidades de palabras.")
            print("3. Mostrar los idiomas con sus cantidades de palabras totales.")
            print("4. Generar archivos CSV.")
            
            # ==================================================================================            
            # Caso 1
            # Caso que sustituye palabras y genera varios archivos XML según la cantidad de .logs
            # ================================================================================== 
            
            def case1():
                # Se le pide la ruta donde están todos los archivos
                ruta = input("Escribe la ruta de los archivos: ")
                extension = '.log'

                # Usa el patrón de búsqueda para obtener una lista de archivos con la extensión especificada
                archivos = glob.glob(ruta + '/*' + extension)
                for archivo in archivos:
                    # Asigna por separado el nombre y su extensión
                    nombre_archivo, ext = os.path.splitext(
                        os.path.basename(archivo))
                    try:
                        with open(nombre_archivo+ext, "r") as file:
                            contenido = file.read()
                        # Escribe etiquetas al principio y final del contenido y sustituye las palabras con espacios
                        contenido = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<task>\n" + contenido
                        contenido = contenido.replace(
                            "TM SENTENCES", "TM_SENTENCES")
                        contenido = contenido.replace(
                            "MT SENTENCES", "MT_SENTENCES")
                        contenido = contenido.replace("MT WORDS", "MT_WORDS")
                        contenido = contenido.replace(
                            "MT CHARACTERS", "MT_CHARACTERS")
                        contenido = contenido + "</task>"

                        # Al terminar se genera un archivo XML con el contenido nuevo
                        with open(nombre_archivo + ".xml", "w") as file:
                            file.write(contenido)
                        print("Archivo/s generado")
                    except FileNotFoundError:
                        print("Archivo no encontrado")
                    except UnboundLocalError:
                        print("No se pudo acceder a la variable")
                    except:
                        print("Ha ocurrido un error inesperado.")
            
            # ==================================================================================            
            # Caso 2
            # Caso que muestra cada idioma con su cantidad de palabras
            # ================================================================================== 
            
            def case2():
                # Se le pide la ruta donde están todos los archivos
                ruta = input("Escribe la ruta de los archivos: ")
                extension = '.xml'
                # Usa el patrón de búsqueda para obtener una lista de archivos con la extensión especificada
                archivos = glob.glob(ruta + '/*' + extension)
                for archivo in archivos:
                    # Se le asigna sólo el archivo con su extensión
                    nombre_archivo = os.path.basename(archivo)
                    print("==================================================")
                    print("Archivo " + nombre_archivo + ":")
                    try:
                        # Se le parsea con minidom
                        doc = minidom.parse(nombre_archivo)
                        raiz = doc.getElementsByTagName('task')[0]
                        task_events = raiz.getElementsByTagName('TaskEvent')
                        # Bucle for para recorrer todo el documento
                        for task_event in task_events:
                            # Recojo todos los datos necesarios, se utilizarán para el caso 3 también
                            array.append(task_event.getElementsByTagName(
                                'TRANSLATION_DIRECTION')[0].firstChild.data)
                            array_numeros.append(
                                int(task_event.getElementsByTagName('WORDS')[0].firstChild.data))
                        # Muestro los datos
                        for i in range(0, len(array)):
                            print("Idioma: " + str(array[i]) +
                                  " con " + str(array_numeros[i]) + " palabras")
                        print("==================================================")
                    except FileNotFoundError:
                        print("Archivo no encontrado")
                    except UnboundLocalError:
                        print("No se pudo acceder a la variable")
                    except:
                        print("Ha ocurrido un error inesperado.")
            
            # ==================================================================================            
            # Caso 3
            # Caso que muestra cada idioma con su cantidad total de palabras
            # ================================================================================== 
            
            def case3():
                # diccionario para guardar los arrays
                diccionario = {}
                # método zip para recorrer las 2 listas a la vez
                for idioma, numero in zip(array, array_numeros):
                    # si el idioma no está en diccionario, se le añade el idioma con su número
                    if idioma not in diccionario:
                        diccionario[idioma] = numero
                    # si el idioma existe se le suma el número al número ya asignado
                    else:
                        diccionario[idioma] += numero
                # muestro el diccionario
                print(diccionario)
                """ try:
                    # Se le añade el primer idioma de la variable array al array_idiomas que está vacío
                    array_idiomas.append(array[0])
                    # Se recorre la variable array por completo
                    for idioma_actual in array:
                        # booleano que se asigna el valor de False en cada interacción
                        encontrado = False
                        # Se recorre el array_idiomas por completo
                        for idioma_guardado in array_idiomas:
                            # Si el idioma_actual de array está en idioma_guardado
                            if idioma_actual == idioma_guardado:
                                # Se le asigna el valor de true al booleano y sale de este bucle
                                encontrado = True
                                break
                        # Si no se ha encontrado el idioma, el booleano seguirá en False, entonces se le añade ese idioma al array_idiomas
                        if not encontrado:
                            array_idiomas.append(idioma_actual)
                    # Se le añade el primer valor del array_numeros a array_palabras
                    array_palabras.append(int(array_numeros[0]))
                    # Bucle for que recorrerá el array por completo
                    for i in range(0, len(array)):
                        # Segundo bucle para comparar con el primer bucle
                        for j in range(0, len(array_idiomas)):
                            # Si el el valor de la posición j no está en la i
                            if array[i] != array_idiomas[j]:
                                # Se le añade el valor al array_palabras
                                array_palabras.append(int(array_numeros[i]))
                            else:
                                # Si los idiomas coinciden, se le suma el número a esa posición
                                array_palabras[j] = array_palabras[j] + 
                                    int(array_numeros[i])
                    # Muestra el resultado
                    for i in range(0, len(array_idiomas)):
                        print("Idioma: " + str(array_idiomas[i]) +
                              " con un total de " + str(array_palabras[i]) + " palabras")
                except IndexError:
                    print("Escoge la opción 2 antes de esta") """
            
            # ==================================================================================            
            # Caso 4
            # Caso que genera varios archivos CSV, según la cantidad de XMLs
            # ================================================================================== 
            
            def case4():
                # Se le pide la ruta donde están todos los archivos
                ruta = input("Escribe la ruta de los archivos: ")
                extension = '.xml'
                # Usa el patrón de búsqueda para obtener una lista de archivos con la extensión especificada
                archivos = glob.glob(ruta + '/*' + extension)
                for archivo in archivos:
                    # Asigna por separado el nombre y su extensión
                    nombre_archivo, ext = os.path.splitext(
                        os.path.basename(archivo))
                    try:
                        doc = minidom.parse(nombre_archivo+ext)
                        raiz = doc.getElementsByTagName('task')[0]
                        task_events = raiz.getElementsByTagName('TaskEvent')
                        # Genera un fichero CSV
                        with open(nombre_archivo + ".csv", mode="w", newline='') as csv_file:
                            # El signo ; será el delimitador
                            writer = csv.writer(csv_file, delimiter=';')
                            # En la primera línea se escribirá lo siguiente
                            writer.writerow(
                                ["TaskEvent:id", "TRANSLATION_DIRECTION", "WORDS"])
                            # Se recorre el fichero XML recogiendo los datos necesarios
                            for task_event in task_events:
                                task_id = task_event.getAttribute("id")
                                translation_direction = task_event.getElementsByTagName(
                                    "TRANSLATION_DIRECTION")[0].firstChild.nodeValue
                                words = task_event.getElementsByTagName(
                                    "WORDS")[0].firstChild.nodeValue
                                # Se escribe los datos dentro del archivo CSV
                                writer.writerow(
                                    [task_id, translation_direction, words+";"])
                        print("\nFichero CSV creado")
                    except FileNotFoundError:
                        print("Archivo no encontrado")
                    except UnboundLocalError:
                        print("No se pudo acceder a la variable")
                    except:
                        print("Ha ocurrido un error inesperado.")
            # Si se introduce algo que no está permitido saltará este mensaje

            def default():
                print("Opción no válida")
            # switch para cada caso
            switch = {
                1: case1,
                2: case2,
                3: case3,
                4: case4
            }
            try:
                opcion = int(input("Introduce una opción: "))
                # Según la opción escogida se hará una acción en concreto
                switch.get(opcion, default)()
            except ValueError:
                print("Por favor ingresa solo números enteros.")
            except:
                print("Ha ocurrido un error inesperado.")


ejercicio = Ejercicio()
ejercicio.menu()
