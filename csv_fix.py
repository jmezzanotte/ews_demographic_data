'''
    Author          : John Mezzanotte
    Project         : EWS (Excel based)
    Date Created    : 9-22-2016
    Last Modified   : 9-22-2016
    Description     : 

'''

import pandas as pd 
import os

if __name__ == "__main__" :

    # Set up directories
    root = r"<root directory>"
    os.chdir(root)

    input_file = '<inut file>.csv'
    output_file = '<output file>.csv'

    df = pd.read_csv(input_file)

    df.Disability[pd.isnull(df.Disability) ] = ''
    df.Disability[df.Disability == ' '] = ''
    
      
    df.to_csv(output_file, sep=',')
    

    
