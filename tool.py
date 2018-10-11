# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:04:41 2017

@author Ömer Seyrekbasan
"""
import os
import time

while (True):
    #sistem çağrısı yapılarak arp -a komutu çalıştırılıp tmp file ına dump edilir
    os.system('arp -a> tmp')
    #tmp file ı okunur
    infile = open('tmp', 'r')
    
    arp_mac = []
   
    #her satırdaki mac adresleri okunur
    for line in infile:
        new_mac =''
        new_mac+=line[24:41]
        arp_mac.append(new_mac)
                 
    i=0
    j=1
    unique=0
    #aynı mac adresinden 2 adet gelene kadar veya tüm adresler kontrol edilene
    #kadar döngüye girilir. Eğer aynı mac adresinden birden fazla varsa 
    #saldırı olabilir.
    while  (i<len(arp_mac) and unique==0):
        j=i+1
        while(j<len(arp_mac) and unique==0):
            if (arp_mac[i]==arp_mac[j] and arp_mac[i]!="ff-ff-ff-ff-ff-ff"):
                unique=1
            else:
                j=j+1
        i=i+1
        
    if (unique==0):
        print("Everything is in order!" )
        print("Time="+time.strftime("%X"))
        
    else: 
        print("Arp Attack Detected!")
        print("Time="+time.strftime("%X"))
    time.sleep(15)