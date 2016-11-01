#################################### TRUCK MODEL ####################################
truck_model_project = 'Projects/TruckModel/TruckModel.emp'
#hh_employment_file = 'tazdata.in'
districts_file = 'districts19_ga.ens'
truck_trips_h5_filename = 'inputs/4k/auto.h5'
truck_base_net_name = 'am_roadway.in'
#TOD to create Bi-Dir skims (AM/EV Peak)
truck_generalized_cost_tod = {'5to9' : 'am', '15to18' : 'pm'}
#GC & Distance skims that get read in from Soundcast

# 4k time of day
tod_list = ['am','md', 'pm', 'ni']
# External Magic Numbers
LOW_STATION = 1511
HIGH_STATION = 1528
EXTERNAL_DISTRICT = 'ga20'

truck_adjustment_factor = {'ltpro': 0.544,
							'mtpro': 0.545,
							'htpro': 0.530,
							'ltatt': 0.749,
							'mtatt': 0.75,
							'htatt': 1.0}