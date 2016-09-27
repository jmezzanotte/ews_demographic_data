"""
    Written-by : John Mezzanotte
    Project : EWS Excel Support
    Date-last-modified: 9-26-16
    Description: Cohort value needs to have an actual word to be read and
                 not just a integer (even if that integer is stored as a
                 string. This program will attach a prefix to the values
                 in the cohort column to all the EWS system to interpret the
                 categories correctly.
"""

import os
import csv

def tab(data, column) :

    """Takes a dictreader object and a column from that dictreader as input"""

    table = {}
    
    for i in data :
        if i[column] not in table :
            # add it to tab
            table[i[column]] = 1 
        else:
            # add tabulation
            table[i[column]] += 1

    #place the cursor back at 0
    
    return table

if __name__ == "__main__":


    root = os.path.abspath("<directory>")
    src_data = "<source data file>.csv"
    out_data = "<out data file>.csv"

    field_names = [
        'First Name',
        'Last Name',
        'Student Id',
        'Grade',
        'Date of Birth',
        'Gender',
        'Ethnicity',
        'Disability',
        'Disadvantaged',
        'ELL Status',
        'Cohort',
        'Enrollment Status',
        'Date of Status Change',
        'Quarter 1 Days',
        'Quarter 2 Days',
        'Quarter 3 Days',
        'Quarter 4 Days',
        'Guardian(s)',
        'Phone',
        'Email',
        'Comments'
    ]


    target_col = 'Cohort'
    with open(os.path.join(root, src_data), 'rb') as f, open(os.path.join(root, out_data), 'wb') as out:

        data = csv.DictReader(f)
        
        w = csv.DictWriter(out, field_names)
        w.writeheader()
         
        for i in data :
            if i[target_col] == '9' :
                i[target_col] = 'grade 9'
            elif i[target_col] == '10' :
                i[target_col] = 'grade 10'
            elif i[target_col] == '11' :
                i[target_col] = 'grade 11'
            elif i[target_col] == '12' :
                i[target_col] = 'grade 12'

            w.writerow(i)

        

    # run tests on both files to make sure each 

    with open(os.path.join(root, src_data), 'rb') as original:
        y = csv.DictReader(original)
        for i in field_names:
            if i == 'Cohort':
                print tab(y, i)
            original.seek(0)


    with open(os.path.join(root, out_data), 'rb') as out :
        test = csv.DictReader(out)
        for i in field_names :
            if i == 'Cohort' :
                print tab(test,i)
            out.seek(0)
       


