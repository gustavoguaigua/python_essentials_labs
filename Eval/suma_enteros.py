# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:15:36 2023

@author: User
"""

def suma_enteros(*var):
    suma=0
    for i in var:
        suma+=i    
    return f"La suma de estos {len(var)} números es: {suma}"
