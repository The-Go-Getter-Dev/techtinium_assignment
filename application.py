import pandas as pd

# reading data from the multiple source and getting regional level que data with priorty over per unit cost of system

def read_data(regional_availability_file,per_packge_count_file): 
    try:   
        df=pd.read_csv(regional_availability_file,"\t",header='infer')
        no_of_unit=pd.read_csv(per_packge_count_file,"-",header=None)
    except OSError as e :
        print(e)
    no_of_unit.reset_index(drop=True, inplace=True)

    capacity_count=dict(zip(no_of_unit[0].to_list(),[int(num.split(" ")[0]) for num in no_of_unit[1].to_list()]))
    # since we can always find the total cost if ewe have type and 
    df.iloc[:,[0]].values.tolist()
    width=df.shape[1]

    regions_que={}
    columns=df.columns
    capacity=df.iloc[:,0]
    counter=0
    # mapping data from two sources
    for country in columns[1:]:
        detail_list=[]
        if regions_que.get(country)==None:
            regions_que[country]=[]
            for row in df[country].values:
                val= 0 if row.split(" ")[1] =="" else int(row.split(" ")[1])
                if val>0:
                    detail_list=[val,int(capacity_count.get(capacity[counter])),capacity[counter],val/int(capacity_count.get(capacity[counter]))]    
                regions_que[country].append(detail_list)
                counter+=1
            counter=0    
        else:
            for row in df[country].values:
                val= 0 if row.split(" ")[1] =="" else int(row.split(" ")[1])
                if val>0:
                    detail_list=[val,int(capacity_count.get(capacity[counter])),capacity[counter],val/int(capacity_count.get(capacity[counter]))]
                regions_que[country].append(detail_list)
                counter+=1
    return regions_que


# filtering the subsets from the available resource which are feasiable
def get_subset(total_instance,regions_que):
    subset_total_instance={}
    for region in  regions_que.keys():
        for available_resource in regions_que[region][::-1]:
            if total_instance >=available_resource[1]:
                if subset_total_instance.get(region)==None:
                    subset_total_instance[region]=[]
                    subset_total_instance[region].append(available_resource)
                else:
                    subset_total_instance[region].append(available_resource)
    return subset_total_instance

# getting the optimal resource allocations
def get_optimal(total_units,time_to_run,regional_availability_file,per_packge_count_file):
    if total_units<0 and type(total_units)==int:
        raise AttributeError("total_units must be greater then zero and integer")
    if time_to_run<0 and type(time_to_run)==int:
        raise AttributeError("time must be in hours must be greater then zero and integer")
    
    regional_priorty_que=read_data(regional_availability_file,per_packge_count_file)
    
    subset_data=get_subset(total_units,regional_priorty_que)
    for region in subset_data.keys():
        subset_data[region]=sorted(subset_data.get(region), key = lambda x: x[3])    
    total_expense={"Outputs":[]}
    
    for region in subset_data.keys():
        cost=0
        selected_machine=[]
        required_tot=int(total_units)
        for systm in subset_data.get(region):
            if required_tot==0:
                break
            assign_of=required_tot//systm[1]
            required_tot-=assign_of*systm[1]
            if assign_of>0:
                selected_machine.append((systm[2],assign_of))
                cost+=time_to_run*assign_of*systm[0]
        total_expense.get("Outputs").append({'region':region,"total_cost":cost,"machines":selected_machine})
            
    return(total_expense)


if __name__=="__main__":
    # give total no of units required
    tot_unit=int(input("give total_units"))
    # get total_time to run
    time_to_run=int(input("time to run for"))
    # file path of the regional data
    regional_availability_file="country_alloc.csv"
    #file path of resource bundle capacity
    per_packge_count_file="resource_capacity.csv"
    
    # function call for getting optimal data
    output=get_optimal(tot_unit,time_to_run,regional_availability_file,per_packge_count_file)
    print(output)

    