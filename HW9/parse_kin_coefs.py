#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:44:03 2017

@author: filipmichalsky
"""
#def species_txt_to_dict(xml_file):
file = open('thermo.txt','r')
lines = file.readlines()

species_dict ={}
Low = {}
High = {}

for i in lines:
    chars = i.split()
    #print(chars)
    if chars[-1]=='1':
        current_specie = chars[0]
        species_dict[current_specie]={'low':{},'high':{}}
        #Low Tmax Tmin
        Ltmin = chars[-4]
        Ltmax = chars[-2]
        Htmin = chars[-2]
        Htmax = chars[-3]
        #print(Ltmin,Ltmax,Htmin,Htmax)
    elif chars[-1] =='2':
        a1= i[0:15]
        a2= i[15:30]
        a3 = i[30:45]
        a4 = i[45:60]
        a5 = i[60:75]
        #print(i)
        #print(a1,a2,a3,a4,a5)
    elif chars[-1] == '3':
        a6 = i[0:15]
        a7 = i[15:30]
        
        coefs_highT = [a1,a2,a3,a4,a5,a6,a7]
        #for index,j in enumerate(coefs_highT):
        #    coefs_highT[index]=float(j)
        
        #print("coefs",coefs_highT)
        l1 = i[30:45]
        l2 = i[45:60]
        
    elif chars[-1] == '4':
        l3= i[0:15]
        l4= i[15:30]
        l5 = i[30:45]
        coefs_lowT = [l1,l2,l3,l4,l5]
        #for index,j in enumerate(coefs_lowT):
        #    coefs_lowT[index]=float(j)
            
        #print("low coef",coefs_lowT)
        species_dict[current_specie]['low']['coefs'] = coefs_lowT
        species_dict[current_specie]['low']['tmax'] = Ltmax
        species_dict[current_specie]['low']['tmin'] = Ltmin
        
        species_dict[current_specie]['high']['coefs'] = coefs_highT
        species_dict[current_specie]['high']['tmax'] = Htmax
        species_dict[current_specie]['high']['tmin'] = Htmin
        
        #print("current coefs",species_dict[current_specie]['high']['coefs'])
    if chars[0]=="END":
        #print("END")
        break
        
#print(species_dict)

from copy import deepcopy
import xml.etree.ElementTree as ET
#use the template file
tree = ET.parse('example_thermo.xml')
root = tree.getroot()

#get a node of species
specie = deepcopy(root.find('speciesData').find('species'))

#remove all the species from the parent
old_species = root.find('speciesData').findall('species')

for item in old_species:
    root.find('speciesData').remove(item)

for index,key in enumerate(species_dict):
    
    temp = deepcopy(specie)
    temp.set('name',str(key))
    
    #species_dict[key]['low']['coefs']
    
    NASA = temp.find('thermo').findall('NASA')
    
    NASA[0].find('floatArray').text = ', '.join(species_dict[key]['low']['coefs'])
    NASA[0].set("Tmax",species_dict[key]['low']['tmax'])
    NASA[0].set("Tmin",species_dict[key]['low']['tmin'])
    
    NASA[1].find('floatArray').text = ', '.join(species_dict[key]['high']['coefs'])
    NASA[1].set("Tmax",species_dict[key]['high']['tmax'])
    NASA[1].set("Tmin",species_dict[key]['high']['tmin'])
    
    root.find('speciesData').append(temp)

#creating my SpeciesArray
for item in root.find('phase'):
    specie_names = [value for value in species_dict]
    item.text = " ".join(specie_names)
    #item.text = [value for value in species_dict]
    #elements.extend(item.text.strip().split())

tree.write("filename.xml")


#pretify the resulting xml
import xml.dom.minidom

xml = xml.dom.minidom.parse("filename.xml") # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
