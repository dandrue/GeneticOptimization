# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:05:36 2021

@author: Diego Rueda
"""

import Restrictions
import genes
import math
import functions

def InitPob():
    initIn = []
    initInCod = []    
    while len(initIn)<(2*len(genes.genes)):
        "Agregar sección para la determinación de restricciones, solo los individuos que cumplan pasan a la población inicial"
        crom = []
        cromValues = []
        for j in genes.genes:
            genRes = j[3]
            n = functions.genRandom(genRes)
            res = math.log(genRes,2)
            #print(n)
            value = j[1]+n*j[4]
            #print(value)
            string = functions.decToBin(int(n), int(res))
            crom.append(string)
            cromValues.append(value)
        values = Restrictions.rest(cromValues)
        if sum(values) <= 0:
            initInCod.append("".join(crom))
            initIn.append(cromValues)
    #print(initIn)
    #print(initInCod)
    return [initIn,initInCod]

InitPob()