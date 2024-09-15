"""
TASK #2: Order Game

You are given an array of integers, @ints, whose length is a power of 2. Write a script to play the order game (min and max) and return the last element.


Supongamos que @ints = [3, 5, 2, 9, 12, 15, 8, 10], cuya longitud es 8 (una potencia de 2).
Primera ronda (mínimo): Seleccionamos el mínimo de cada par → [3, 2, 12, 8]
Segunda ronda (máximo): Seleccionamos el máximo de cada par → [3, 12]
Tercera ronda (mínimo): Seleccionamos el mínimo de los dos → [3]
Resultado final: 3

"""
import numpy as np

def es_potencia(potencia: int,num:int) -> bool:
    """Verifica si un número es una potencia de numero."""
    if num < 1:
        return False
    while num % potencia == 0:
        num //= potencia
    return num == 1

def dividir_en_n(ints: np.ndarray, n: int = 2)-> np.ndarray:
    if len(ints)>= n:
        new_ints = ints.reshape(-1, n)
    else:
        new_ints = ints 
    return new_ints



def ronda(ints: np.ndarray | list, ronda_par:bool = False)-> int:
    
    assert len(ints) > 0 and es_potencia(2,len(ints)), "El array de integers no es potenciad de 2"  
    assert isinstance(ints, (list,np.ndarray)), "El argumento ints pasado no es un array"
    assert isinstance(ronda_par, bool), "El argumento ronda_par pasado no es un bool"

    ints = np.asarray(ints) 
    seleccion = ints.copy()
    for _ in range(0,len(seleccion)-2,2):
        pares = dividir_en_n(seleccion)
        
        seleccion = np.array([max(par) if ronda_par else min(par) for par in pares])
        ronda_par = not ronda_par

    return seleccion[0]




print(ronda([3, 5, 2, 9, 12, 15, 8, 10]))

