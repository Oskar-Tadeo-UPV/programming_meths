#Agregando elementos a una lista
motorcycles = ['honda', "mortalica", 'yamaha']
print(motorcycles)

#Metodo appendo
motorcycles.append("kawasaki")
print(motorcycles)

"""
    El método 'append' ayuda a crear listas facilmente de manera
    dinamica
"""
motorcycles_2 = [] #lista vacia
print(motorcycles_2)

motorcycles_2.append("honda") # 1 elemento
motorcycles_2.append("yamaha") # 2 elementos
motorcycles_2.append("suzuki") # 3 elementos

print(motorcycles_2)
print("-------------------------------------------------------------------------------------------")
#Metodo insert
"""
.insert(indice,elemento)
Añade el elemento por el indice seleccionado
"""
motorcycles_3 = ['honda', "mortalica", 'yamaha','suzuki']
motorcycles_3.insert(4,"mortalica")
print(motorcycles_3)
print("-------------------------------------------------------------------------------------------")
#Metodo pop
"""
.pop(*)
Elimina elementos por indice
"""
motorcycles_4 = ['honda', 'mortalica', 'yamaha','suzuki']
motorcycles_4.pop() #borrara suzuki "Ultimo de la lista"
print(motorcycles_4)
motorcycles_4.pop(0) #borrara 'honda' indice 0
print(motorcycles_4)
print("-------------------------------------------------------------------------------------------")
#Metodo remove
"""
.remove(*)
Elimina elementos por valor
"""
motorcycles_5 = ['honda', 'mortalica', 'yamaha', 'suzuki', 'hd', 'kawasaki']
motorcycles_5.remove('yamaha') #borrara yamaha "elemento seleccionado por argumento" 
print(motorcycles_5)
print("-------------------------------------------------------------------------------------------")

#Metodo sort
"""
Ordenar la lista de manera permanente (Argumento opcional de sort[reverse=True])
"""