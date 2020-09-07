# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:35:53 2020

@author: Macrov
"""
from DATA import dataManagement as dama
from DATA import mailManagement as mail
import pandas as pd
import numpy as np


####################### this are some tests ##############################

#Mail tests

mail.authenticate()
content=np.array([])
content=mail.readMail("materiales")
print("\n",content)


#Data handling tests
try:
    
    fin="MACRO.xlsx"
    data=dama.read(fin)


    listProducts = ['1.1.1','2.2.2','2.2.3']
    quantity=[1,2,3]
    budget=dama.budget(data,listProducts,quantity)
    print(budget)
    fout="macrov.xlsx"
    dama.export(data,fout)
except:
    print("Error en encontrar el archivo")



####################### end of tests #####################################
  
###############   Forms ###################################################

"""
IMPORTANTE: BORRAR esta seccion cuando se terminen los forms
-Aca es toda la creacion de los forms web, todos los datos que se extraigan de los forms colocarlos en unas variables y ya 

-lo hacen Leidy y diana
"""

