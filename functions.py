#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diego Rueda
"""
import numpy as np
import Restrictions, ObjectiveFunction
import math

def init():
    nGenes = int(input("Introduzca el número de genes del sistema: "))
    info = []
    for i in range(nGenes):
        try:
            genName = input("Introduzca el nombre del gen \"Nombre\" default gen" + str(i)+" :")
            if genName == "":
                genName = "gen" + str(i)
        except SyntaxError:
            genName = "gen"+str(i)
        genMin = float(input("Introduzca el valor mínimo para " + genName + " :"))
        genMax = float(input("Introduzca el valor máximo para " + genName + " :"))
        bitRes = int(input("Introduzca el número de bits 2^q :"))
        delta = float(input("Introduzca el valor del delta: "))
        info.append([genName,genMin,genMax, bitRes, delta])
    #print(info)
    return info

def initPoblation(genes):
    initIn = []
    initInCod = []
    "Agregar sección para la determinación de restricciones, solo los individuos que cumplan pasan a la población inicial"
    for i in range(2*len(genes)):
        crom = []
        cromValues = []
        for j in genes:
            genRes = j[3]
            n = genRandom(genRes)
            res = math.log(genRes,2)
            value = j[1]+n*j[4]
            string = decToBin(int(n), int(res))
            crom.append(string)
            cromValues.append(value)
        initInCod.append("".join(crom))
        initIn.append(cromValues)
    return [initIn, initInCod]

def decToBin(n, l):
    nBin = np.binary_repr(n,l)
    return nBin

def genRandom(bitRes):
    rnd = np.random.randint(0, bitRes)
    return rnd

def evalRestrictions(initValues, factor):
    restValues  = []
    restrictions = []
    for i in initValues:
         rest = Restrictions.rest(i)
         #print(rest)
         value = 0
         for h in range(len(rest)):
             value+= rest[h]**2
         penalization = factor * value
         restValues.append(penalization)
         restrictions.append(rest)
    #print(restrictions)
    return [restValues,restrictions]

def evalObjectiveFunction(initValues):
    fitness = []
    for i in initValues:
        fitValue = ObjectiveFunction.objectiveFunction(i)
        fitness.append(fitValue)
    return fitness

def evaluation(initValuesDec, factor):
    rest = evalRestrictions(initValuesDec,factor)[0]
    restrictions = evalRestrictions(initValuesDec,factor)[1]
    fitness = evalObjectiveFunction(initValuesDec)
    result = []
    for i in range(len(rest)):
        value = fitness[i]-rest[i]
        #print(rest[i])
        if value<0:
            value = 10000
        #print(value)
        result.append(value)
    total = sum(result)
    percentage = [x / total for x in result]
    totalPercentage = []
    for i in range(len(percentage)):
        if i ==0:
            totalPercentage.append(percentage[i])
        else:
            totalPercentage.append(percentage[i]+totalPercentage[i-1])
    return [result,percentage,totalPercentage,restrictions]

def selection(totalPercentage, elitismRate, result, indCod):
    selectionRate = 1 - elitismRate
    ind = len(totalPercentage)*selectionRate
    ind = round(ind)
    cromSel = elitism(result, indCod, len(totalPercentage)-ind)
    #print(totalPercentage)
    #print(indCod)
    while len(cromSel) < len(totalPercentage):
        value = np.random.random()
        #print(value)
        for j in totalPercentage:
            if value>j:
                pass
            else:
                cromSel.append(indCod[totalPercentage.index(j)])
                break
        else:
                if result[totalPercentage.index(j)]==100:
                    pass
                else:
                    cromSel.append(indCod[totalPercentage.index(j)])
                    break
    #print("-----------------Selection-------------------------") 
    #print(cromSel)
    return cromSel

def crossOver(cromSel, nPoints):
    nextGen = []
    randomValue = len(cromSel)
    for i in range(int(len(cromSel)/2)):

        value1 = np.random.randint(0,randomValue)
        value2 = np.random.randint(0,randomValue)
        crossPoints = []
        for j in range(nPoints):
            crossPoints.append(np.random.randint(0,len(cromSel[i])))
        #print(sorted(crossPoints))
        crossPoints = sorted(crossPoints)
        crom_1 = cromSel[value1]
        crom_2 = cromSel[value2]
        seg_1 = []
        seg_2 = []
        for k in range(len(crossPoints)):
            seg = (lambda seg1: seg1[crossPoints[k-1]:crossPoints[k]] if k>0 else seg1[:crossPoints[k]])(crom_1)
            seg_1.append(seg)
            seg = (lambda seg2: seg2[crossPoints[k-1]:crossPoints[k]] if k>0 else seg2[:crossPoints[k]])(crom_2)
            seg_2.append(seg)
        seg_1.append(crom_1[crossPoints[-1]:])
        seg_2.append(crom_2[crossPoints[-1]:])
        #print(seg_1)
        #print(seg_2)
        crom_1 = []
        crom_2 = []
        for l in range(len(seg_1)):
            if i%2==0:
                crom_1.append(seg_1[l])
                crom_2.append(seg_2[l])
            else:
                crom_1.append(seg_2[l])
                crom_2.append(seg_1[l])
        #print(crom_1)
        #print(crom_2)
        crom_1 = "".join(crom_1)
        crom_2 = "".join(crom_2)
        nextGen.append(crom_1)
        nextGen.append(crom_2)
    #print(cromSel)
    #print("---------------------Next Gen---------------------------")
    #print(nextGen)
    return nextGen


def elitism(result, indCod, ind):
    labels = range(len(result))
    dic = dict(zip(labels, result))
    dic_2 = dict(zip(labels, indCod))
    values = sorted(result, reverse = True)
    sel = values[:ind]
    indSel = []
    for i in sel:
        val_list = list(dic.values())
        index = val_list.index(i)
        indSel.append(dic_2[index])
    #print(sel, indSel)
    return indSel

def mutation(binGen, mutationRate):
    outputGen = []
    for i in binGen:
        outputCrom = []
        av = 0
        for j in range(len(i)):
            option = np.random.random()
            if option<=mutationRate:
                if i[j] == "0":
                    outputCrom.append("1")
                else:
                    outputCrom.append("0")
                #print("Mutation")
                #print(i)
                #print("".join(outputCrom))
                av = 1
            else:
                outputCrom.append(i[j])
        #if av==1:
        #    print(i)
        #    print("".join(outputCrom))
            #outputCrom = "".join(outputCrom)
        outputGen.append("".join(outputCrom))
    #print(outputGen)
    return outputGen

def decod(genes, gen):
    bitRes = []
    for i in genes:
        res = math.log(i[3],2)
        #print(res)
        bitRes.append(int(res))
    #print(bitRes)
    bit = []
    for i in range(len(bitRes)):
        if i==0:
            bit.append(bitRes[i])
        else:
            bit.append(bitRes[i]+bit[i-1])
    #print(bit)
    genSep = []
    genDecod = []
    for i in gen:
        #print(i)
        singleCrom = []
        singleDecodCrom = []
        ant = 0
        for j in range(len(bit)):
            val = i[ant:bit[j]]
            decodVal = int(val,2)
            #print(decodVal)
            singleCrom.append(val)
            singleDecodCrom.append(decodVal)
            ant = bit[j]
        #print(singleCrom)
        #print(singleDecodCrom)
        genSep.append(singleCrom)
        genDecod.append(singleDecodCrom)
        #print(genDecod)
    
    genValues = []
    for j in range(len(genDecod)):
        crom = []
        #print(genDecod[j])
        for k in range(len(genDecod[j])):
            value = genes[k][1] + genDecod[j][k]*genes[k][4]
            #print(value)
            crom.append(value)
        genValues.append(crom)

    return genValues
