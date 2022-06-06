#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diego Rueda
"""
import functions as f
import math
import genes as gn
import InitPob

"""
Declaración de genes,

El usuario ingresa la información utilizando la función f.init()
"""
genes = gn.genes
pob = InitPob.InitPob()
indValues = pob[0]
indCod = pob[1]
"""
Teniendo la información de los genes se procede a generar la población inicial
se puede generar aleatoriamente ó ingresarla utilizando la estructura del sistema
"""

"""
Se definen los parámetros de elitismo, puntos de cruce en el crossover, número de iteraciones
y factor de penalización de algoritmo
"""
mutationRate = 0.75
elitismRate = 0.2
crossPoints = 1
penFactor = 1
iterations = 10000

"""
Se evalúan las restricciones y el fitness de cada uno de los elementos de la población
inicial
"""
#indValues = f.initPoblation(genes)[0]
#indCod = f.initPoblation(genes)[1]

"""
Utilizando los individuos de la población inicial se inicia la iteración, selección,
crossover, decodificación y evaluación de la nueva generación
"""
experimentos = 100
maxExperimentos = []
maxExpNum = []
for e in range(experimentos):
    #indValues = f.initPoblation(genes)[0]
    #indCod = f.initPoblation(genes)[1]
    #indValues = [[11.75,9.25,8],[9.5,8.25,10.75],[21.5,10,11.25],[8,14.25,11],[10,6.25,12.75],[21.25,13.25,10.5]]
    #indCod = ["000110110001000100001100","000100100000110100010111", "010000100001010000011001", "000011000010010100011000", "000101000000010100011111", "010000010010000100010110"]
    bestFitsCroms = []
    bestFitsNum = []
    bestRes = []
    [result,percentage,totalPercentage, restrictions] = f.evaluation(indValues, penFactor)
    #print(result,percentage,totalPercentage,restrictions)
    gen = indCod
    for i in range(iterations):
        cromSel = f.selection(totalPercentage,elitismRate, result, gen)
        gen = f.crossOver(cromSel, crossPoints)
        gen = f.mutation(gen,mutationRate)
        genValues = f.decod(genes, gen)
        [result,percentage,totalPercentage, restrictions] = f.evaluation(genValues,penFactor)
        for j in range(len(restrictions)):
            if sum(restrictions[j]) == 0:
                bestFitsCroms.append(result[j])
                bestFitsNum.append(genValues[j])
                #print(i)
    try:
        print(max(bestFitsCroms))
        ind = bestFitsCroms.index(max(bestFitsCroms))
        print(bestFitsNum[ind])
        maxExperimentos.append(max(bestFitsCroms))
        ind = bestFitsCroms.index(max(bestFitsCroms))
        maxExpNum.append(bestFitsNum[ind])
    except ValueError:
        pass

#print(maxExperimentos)
print("---------------------------------------------------------------------")
print(min(maxExperimentos))
ind = maxExperimentos.index(min(maxExperimentos))
print(maxExpNum[ind])
print(max(maxExperimentos))
ind = maxExperimentos.index(max(maxExperimentos))
print(maxExpNum[ind])
import statistics
if experimentos > 1:
    print(statistics.stdev(maxExperimentos))
    print(statistics.mean(maxExperimentos))
