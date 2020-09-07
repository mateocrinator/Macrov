# -- coding: utf-8 --
"""Wed Aug  17 11:37:50 2020

@author: Macrov
"""


import pandas as pd
import os


def read(file):
        """
        Reads the specified file
        and return a dataframe with the file info
        PARAMS:
            file: the name of the file(Database)
        RETURNS:
            Dataframe containing the file data
        """
        try:
            data = pd.read_excel(os.path.join(os.path.dirname(_file_),"../BD/{}").format(file), shet_name=0)
            return data
        except:
            print("No such file")    
    
def export(data,file):
        """
        Reads the dataframe, export the new data
        and return if the export has beean a succes or a failure
        PARAMS:
            data: the dataframe
            file: File name of the exported data
            
        RETURNS:
            Succes or failure
        """
        state="Failure"
        try:
            dataframe = pd.DataFrame(data, columns = ['No. Item', 'Analisis de precios unitarios', 'Unidad',
                                                  'Importe de materiales', 'Importe de mano de obra',
                                                  'Importe de equipo','Importe de auxiliares','Importe de conceptos',
                                                  'Precio unitario'])
            dataframe.to_excel(os.path.join(os.path.dirname(_file_),"../BD/{}").format(file),sheet_name='Presupuesto')
            state="Success"
            return(state)
        except:
            return(state)    
            
    
def budget(data,productsIds, quantity):
        """
        Reads the dataframe and the id of the products wnated in that dataframe
        and return the total budget required for those products
        PARAMS:
            data: the dataframe
            productsId: the list of id's wnated for the budget
            quantity: the list of how much product is required
        RETURNS:
            The total budget
        """
        
        data=data.fillna(0)
        budg=0
        products=productsIds
        quantity=quantity
        
        dataFilter = data[data['No. Item'].isin(products)]
        prices=dataFilter['Precio Unitario'].tolist()
        
        for i in range(len(quantity)):
            budg+=quantity[i]*prices[i]
        return budg 
    


"""
file="MACRO.xlsx"
listProducts = ['1.1.1','2.2.2','2.2.3']
quantity=[1,2,3]
  
data=read(file)
bud=budget(data,listProducts,quantity)
fout="MacrovExported.xlsx"

print(bud)
print(export(data,fout))

"""