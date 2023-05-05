# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:44:11 2023

@author: Shohjahon Qosimov
"""

#davlatlar=["USA","Canada","China","France","Argentina"]
#royhat=list(range(120,1200,2))
#print(davlatlar.sort())
#print(max(royhat)-min(royhat))

#print(min(royhat))
#print(len(royhat))

#boshi=royhat[0:20]
#oxiri=royhat[-20:-1]
#print(oxiri)

taomlar=["osh","manti","chuchvara","xonim","mastava"]
nonushta=taomlar[:]
nonushta.remove("osh",)
nonushta.remove("mastava")
nonushta.append("tuxum")
nonushta.append("sosiska")

#print(taomlar)
#print(nonushta)

nonushta[0]="qaymoq va non"
print(nonushta)