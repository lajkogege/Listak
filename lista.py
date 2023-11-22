import random

"""Generélj 5 véletlen számot [10 30) között"""
def veletlen():
    list=[]
    """listávan azonos típusú adatok legyenek """
    i:int=0
    while i<5:
        szam=random.random()*(35-10)+10
        """A lista végéhez füzzöm az katuális elemet"""
        list.append(szam)
        i+=1

    return list

listam=veletlen()

"""irjuk ki egymás alá a lista elemeit"""
def lista_kiir(lista):
    for i in range (0, len(lista), 1):
        print(f"A lista {i}. eleme: {lista[i]}")

lista_kiir(listam)


def lista_kiir2(lista):
    i:int=0
    while i<=len(lista):
        print(f"A lista {i}. eleme: {lista[i]}")
        i+=1

lista_kiir2(listam)
