# -*- coding: utf-8 -*-

from sympy.solvers import solve
from sympy import Symbol
import numpy as np
import csv
with(open("Book1.csv","r")) as csvfile:
    rdr=csv.reader(csvfile)
    arr=[]
    for rows in rdr:
        arr.append((rows[0],rows[1]))
    print(arr)

t = Symbol("t")
n1 = float(59.92)
n2 = float(17.06)
n3 = float(1.29)
i=0
#aggh
for (a,b) in arr:
        
    Mnt =float(b)*pow(10,6)
    #aewfdsg
    Nrl = float(a);
    #aefdgg
    fy = float(250);
    thick = solve(((Mnt*(0.5*n1 + n3)*t)/(0.08333*pow(n1,3)*pow(t,4) + 0.16667*n2*pow(n3,4)*pow(t,4) + 0.5*n2*pow(n3,2)*pow((n1 + n3),2)*pow(t,4))) + (Nrl/((2*n2*pow(n3,2) + n1)*pow(t,2))) - 0.8*fy,t)
    solution=[]
    for i in range(len(thick)):
        try:
            temp=float(thick[i])
            if temp>0:
                solution.append(temp)
        except:
            print(" ")
    print(solution)
    for i in range(len(solution)):
        d=n1*solution[i]
        b=n2*n3*solution[i]
        T=n3*solution[i]
        D=d+2*T
        area = 2*b*T + d*solution[i]
        dic = {"D": round(D,2),"t":round(solution[i],2),"B":round(b,2), "T":round(T,2),  "area": round(area,2)}
        print(dic)
        list1=[D,solution[i],b,T,area]
        
        with(open("optimal inertia I section.csv","a")) as csvfile:
           wrt=csv.writer(csvfile)
           wrt.writerow(list1)