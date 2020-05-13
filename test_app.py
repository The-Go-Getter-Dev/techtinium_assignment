import pytest
from application import get_optimal,read_data_generate_priortyQue,get_subset
regional_availability_file="country_alloc.csv"
per_packge_count_file="resource_capacity.csv"
#negative values for uni allocataion
def test_negtive_unit_alloc_get_optimal():
    unit_alloc=-1
    time_to_run=1
    with pytest.raises(AttributeError):
        get_optimal(unit_alloc,time_to_run,regional_availability_file,per_packge_count_file)

def test_negative_time_to_run_get_optimal():
    unit_alloc=-1
    time_to_run=1
    with pytest.raises(AttributeError):
        get_optimal(unit_alloc,time_to_run,regional_availability_file,per_packge_count_file)

# test error file not found as refrence is done so that cause UnboundLocal error
def test_file_not_exist_read_data_generate_priortyQue():
    with pytest.raises(UnboundLocalError):
        read_data_generate_priortyQue("",per_packge_count_file)
