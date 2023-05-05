# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:27:25 2023

@author: Shohjahon Qosimov
"""

#ismlar=["Nurbek","Jasur","Ixtiyor"]
#print(f"Salom, {ismlar[0]} IT qilyapsanmi?")
#print(f"{ismlar[1]} kutib tur yangi narsalar o'rganib qo'yma!")

#sonlar=[17,73,93,27,-1,76.9]
#yosh=27
#print(f"Mening yoshim {sonlar[0]} da")

#t_shaxslar=["Alisher Navoiy","Buxoriy","Amir Temur","Benjamin Franklin"]
#x_shaxslar=["Ilon Mask","Lisa","Jony","Bill Gates","Shavkat Mirziyoyev"]
#tarixiy=t_shaxslar.pop(3)
#print(f"Men {tarixiy}dan pul topish sirlarini so'ragan bo'lar edim")
#ideal=x_shaxslar.pop(0)
#print(f"Hozirgi kundagi eng boy odam - {ideal} hisoblanadi")

friends=[]
friends.append("Nurbek")
friends.append("Jasur")
friends.remove("Jasur")
friends.insert(0, "Ixtiyor")
friends.append("Javlon")
yangi_mehmonlar=[]
yangi_mehmonlar.append(friends.pop(1))