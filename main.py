# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:35:53 2020

@author: Macrov
"""
from DATA import dataManagement as dama
from DATA import mailManagement as mail
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


####################### this are some tests ##############################

#Mail tests

mail.authenticate()
content=np.array([])
content=mail.readMail("materiales")
print("\nLectura de correos con titulo materiales\n",content)


#Data handling tests

try:
    
    fin="MACRO.xlsx"
    data=dama.read(fin)
    #data['precio'] = data['Precio Unitario'].astype('category')
    print("\n",data.head())

except:
    print("Error en encontrar el archivo")

b=plt.title("Precios a traves del tiempo")
a=plt.hist(data['Precio Unitario'], bins=100, range=[1200, 735479],density = True,alpha = 0.65, align='left')

plt.savefig("./USERS/grafica.png")
plt.show()

listProducts = ['1.1.1','2.2.2','2.2.3']
quantity=[1,2,3]
budget=dama.budget(data,listProducts,quantity)
print("Presupuesto de para {} en cantidades respectivas {} es de :{}".format(listProducts,quantity,budget))
fout="macrov.xlsx"
print("Export: {}".format(dama.export(data,fout)))

mail.logOut()

####################### end of tests #####################################
  
###############   Forms ###################################################

"""
IMPORTANTE: BORRAR esta seccion cuando se terminen los forms
-Aca es toda la creacion de los forms web, todos los datos que se extraigan de los forms colocarlos en unas variables y ya 

-lo hacen Leidy y diana
"""

