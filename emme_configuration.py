﻿##################################### NETWORK IMPORTER ####################################
project = 'Projects/LoadTripTables/LoadTripTables.emp'
network_summary_project = 'Projects/LoadTripTables/LoadTripTables.emp'
tod_networks = ['am', 'md', 'pm', 'ni']
sound_cast_net_dict = {'5to9' : 'am', '9to15' : 'md', '15to18' : 'pm', '18to5' : 'ni'}
load_transit_tod = ['5to9', '9to15', '15to18', '18to5']

#mode_crosswalk_dict = {'b': 'bp', 'bwl' : 'bpwl', 'aijb' : 'aimjbp', 'ahijb' : 'ahdimjbp', 
#                      'ashijtuvb': 'asehdimjvutbp', 'r' : 'rc', 'br' : 'bprc', 
#                      'ashijtuvbwl' : 'asehdimjvutbpwl', 'ashijtuvbfl' : 'asehdimjvutbpfl', 
#                      'asbw' : 'asehdimjvutbpwl', 'ashijtuvbxl' : 'asehdimjvutbpxl', 
#                      'ahijstuvbw' : 'asehdimjvutbpw'}
mode_file = 'modes.txt'
transit_vehicle_file = 'vehicles.txt' 
base_net_name = '_roadway.in'
turns_name = '_turns.in'
transit_name = '_transit.in'
shape_name = '_link_shape_1002.txt'
no_toll_modes = ['s', 'h', 'i', 'j']
unit_of_length = 'mi'    # units of miles in Emme
coord_unit_length = 0.0001894    # network links measured in feet, converted to miles (1/5280)
headway_file = 'sc_headways.csv'

################################### SKIMS AND PATHS ####################################
log_file_name = 'skims_log.txt'
STOP_THRESHOLD = 0.025
parallel_instances = 4   # Number of simultaneous parallel processes. Must be a factor of 4.
max_iter = 50             # Assignment Convergence Criteria
best_relative_gap = 0.01  # Assignment Convergence Criteria
relative_gap = .0001
normalized_gap = 0.01

MIN_EXTERNAL = 1511      #zone of externals 
MAX_EXTERNAL = 1528      #zone of externals 
HIGH_TAZ = 1359
LOW_PNR = 1360 #external dummy is also included
HIGH_PNR = 1510

SPECIAL_GENERATORS = {"SeaTac":1356,"Tacoma Dome":1357,"exhibition center":1359, "Seattle Center":1358}
feedback_list = ['Banks/5to9/emmebank','Banks/15to18/emmebank']

# Time of day periods
hwy_tod = {'am':4,'md':6,'pm':3,'ni':11}
tods = ['5to9', '9to15', '15to18', '18to5']
project_list = ['Projects/' + tod + '/' + tod + '.emp' for tod in tods]

## HDF5 Groups and Subgroups
hdf5_maingroups = ["Daysim","Emme","Truck Model","UrbanSim"]
hdf5_emme_subgroups = tods
emme_matrix_subgroups = ["Highway", "Walk", "Bike", "Transit"]
hdf5_urbansim_subgroups = ["Households","Parcels","Persons"]
hdf5_freight_subgroups = ["Inputs","Outputs","Rates"]
hdf5_daysim_subgroups = ["Household","Person","Trip","Tour"]

# Skim for time, cost
skim_matrix_designation_all_tods = ['t','c']  # Time (t) and direct cost (c) skims
skim_matrix_designation_limited = ['d']    # Distance skim

# Skim for distance for only these time periods
distance_skim_tod = ['5to9', '15to18']
generalized_cost_tod = ['5to9', '15to18']
gc_skims = {'light_trucks' : 'lttrk', 'medium_trucks' : 'metrk', 'heavy_trucks' : 'hvtrk', 'sov' : 'svtl2'}

# Bike/Walk Skims
bike_walk_skim_tod = ['5to9']

# Transit Inputs:
transit_skim_tod = load_transit_tod
transit_submodes = ['b', 'c', 'f', 'p', 'r']
transit_node_attributes = {'headway_fraction' : {'name' : '@hdwfr', 'init_value': .5}, 
                           'wait_time_perception' :  {'name' : '@wait', 'init_value': 2},
                           'in_vehicle_time' :  {'name' : '@invt', 'init_value': 1}}
transit_node_constants = {'am':{'4943':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'}, 
                          '4944':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'},
                          '4945':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'}, 
                          '4952':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'},
                          '4961':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'}},
                          'pm':{'4943':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'}, 
                          '4944':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'},
                          '4945':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'}, 
                          '4952':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'},
                          '4961':{'@hdwfr': '.1', '@wait' : '1', '@invt' : '.70'}}}

transit_network_tod_dict = sound_cast_net_dict                

transit_tod = {'5to9' : {'4k_tp' : 'am', 'num_of_hours' : 4},
               '9to15' : {'4k_tp' : 'md', 'num_of_hours' : 6}, 
               '15to18' : {'4k_tp' : 'pm', 'num_of_hours' : 3},
               '18to5' : {'4k_tp' : 'ni', 'num_of_hours' : 2}} #trying 2 hours of service instead of 11
                
# Transit Fare:
zone_file = 'inputs/Fares/transit_fare_zones.grt'
peak_fare_box = 'inputs/Fares/am_fares_farebox.in'
peak_monthly_pass = 'inputs/Fares/am_fares_monthly_pass.in'
offpeak_fare_box = 'inputs/Fares/md_fares_farebox.in'
offpeak_monthly_pass = 'inputs/Fares/md_fares_monthly_pass.in'
fare_matrices_tod = ['5to9', '9to15']

# Intrazonals
intrazonal_dict = {'distance' : 'izdist', 'time auto' : 'izatim', 'time bike' : 'izbtim', 'time walk' : 'izwtim'}
taz_area_file = 'inputs/intrazonals/taz_acres.in'
origin_tt_file = 'inputs/intrazonals/origin_tt.in'
destination_tt_file = 'inputs/intrazonals/destination_tt.in'

# Zone Index
#tazIndexFile = '/inputs/TAZIndex_5_28_14.txt'

# SUPPLEMENTAL#######################################################
#Trip-Based Matrices for External, Trucks, and Special Generator Inputs
supplemental_loc = 'outputs/supplemental/'
hdf_auto_filename = 'inputs/4k/auto.h5'
hdf_transit_filename = 'inputs/4k/transit.h5' 
group_quarters_trips = 'outputs/supplemental/group_quarters/'
ext_spg_trips = 'outputs/supplemental/ext_spg/'
supplemental_modes = ['svtl2', 'trnst', 'bike', 'h2tl2', 'h3tl2', 'walk', 'lttrk','metrk','hvtrk']
hh_trip_loc = '/supplemental/generation/rates/hh_triprates.in'
nonhh_trip_loc = '/supplemental/generation/rates/nonhh_triprates.in'
puma_taz_loc = '/supplemental/generation/ensembles/puma00.ens'
taz_data_loc = '/supplemental/generation/landuse/tazdata.in'
pums_data_loc = '/supplemental/generation/pums/' 
externals_loc = '/supplemental/generation/externals.csv'
# Special generator zones and demand (dictionary key is TAZ, value is demand)
spg_general = {1357: 1682,
               1359: 7567,
               1358: 14013}    
spg_airport = {1356: 101838}

# Using one AM and one PM time period to represent AM and PM skims
am_skim_file_loc = 'inputs/5to9.h5'
pm_skim_file_loc = 'inputs/15to18.h5'
trip_table_loc = 'outputs/prod_att.csv'
output_dir = 'outputs/supplemental/'
ext_spg_dir = 'outputs/supplemental/ext_spg'
gq_directory = 'outputs/supplemental/group_quarters'
gq_trips_loc = 'outputs/gq_prod_att.csv'
supplemental_project = 'projects/supplementals/supplementals.emp'
# Iterations for fratar process in trip distribution
bal_iters = 5
# Define gravity model coefficients
autoop = 16.75    # Auto operation costs (in hundreds of cents per mile?)
avotda = 0.0303    # VOT

# Change modes for toll links
toll_modes_dict = {'asehdimjvutbpfl' : 'aedmvutbpfl', 'asehdimjvutbpwl' :	'aedmvutbpwl', 'ahdimjbp' : 'admbp'}