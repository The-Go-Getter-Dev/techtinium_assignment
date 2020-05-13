for running script type python application.py
#INPUT
it ask for 2 inputs resource counts and resource time to run
#OUTPUT
provide optimal allocation of the resources


#Approch

1. Considerations- The data is presented in form of csvs both of them is named as follows:
    a.country_alloc.csv= Contains data of country availablity and price for resource bundles
    b.resource_capacity.csv= Contains the number of units in a bundle

2. Algorithm- 
    
    function implmentation in read_data_generate_priortyQue(file_src1,filesrc2)  output=> dict of priorty list for each regions:
        a. first fetching data from the 2 sources
        b. mapping the bundles count with the regional_availablity data
        c. generation of priority que on the basis of cost per unit for that region 
    
    function implmentation in get_subset():
        d. checking for resource bundle that is allowed for request( for request of 50 4XLarge-80 and above units bundle are not permisable )
            reduces the operational cost, can be better if binary search is implemented
    
    function implmentation in get_optimal():
        e. from the priortiy que choosing the least per unit system(resource) from priorty que of a particular region
        f. assigning as much bundle as we can and deducting the requiremnts_unit appropriately and adding cost as per time
        g. repeating e and f steps untill requeriments are zero for that region
        h. repeating e,f and g for each region
        f. making the appropriate formating and return allocation

