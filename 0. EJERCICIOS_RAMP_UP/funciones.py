def piramide(num):
    for i in range(num,0,-1):
        pir = print(str(list(range(i,0,-1))).replace("[","").replace("]","").replace(",",""))
    return pir

def comparador(num1,num2):
    if num1 == num2:
        return "Los números son iguales."
    elif num1 < num2:
        return "El primer número es menor que el segundo."
    else:
        return "El segundo número es mayor que el primero."
    
def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def area_cuadrado(lado):
    return lado**2

def triangulo(base,altura):
    return (base*altura)/2

def area_circulo(radio):
    import math
    return math.pi*radio**2

def elevar(lista):
    new_list = []
    if len(lista) >=1 : 
        for elemento in lista:
            if (type(elemento) == int) or (type(elemento) == float): 
                new_list.append(elemento**2)
            else: 
                print("La lista contiene elementos no validos")
                return None 
        return new_list  
    else:
        print("La lista está vacia")
        return None

def pali(palabra):
    if (palabra.lower() == palabra.lower()[::-1]):
        return True 
    else:
        return False

def divisores(num):
    lista_divisores = []
    for div in range(1, num + 1):
        if num % div == 0:
            lista_divisores.append(div)
    return lista_divisores

def primo(num):
    lista_divisores = []
    for div in range(1, num + 1):
        if num % div == 0:
            lista_divisores.append(div)

    if len(lista_divisores) == 2:
        return True
    else:
        return False
