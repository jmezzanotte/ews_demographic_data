# ews_demographic_data

#Author
John Mezzanotte

#Date Created 
2-01-2015

#Description
This Python package creates test fake student demographic data spdifically for the Early Warning System online tool developed by the 
American Institutes for Research. The database attributes generated are specific to those used in in the Early Warning System tool 
application. 

#Other Packages used 
This script depends on the python package faker. This package was developed by the group at https://github.com/joke2k
and can be downloaded here: https://github.com/joke2k/faker


#Usage
```
from ews import demographic_data

# create an instance of CreateData
data = demographic_data.CreateData(500)
data.write()
```
