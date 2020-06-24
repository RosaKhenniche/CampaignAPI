import sys
sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages') # Replace this with the place you installed facebookbusiness using pip
sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages/facebook_business-7.0.1-py3.7.egg') # same as abov
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.targeting import Targeting
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.adset import AdSet

from collections import defaultdict
import math
import sys
import pickle
import time
import json
import os
# import MySQLdb
from facebookads.adobjects.targeting import Targeting

import datetime
from facebookads.adobjects.adset import AdSet
import itertools
import credentials
from facebook_business.adobjects.adaccount import AdAccount

CAMPAIGN_IDL1= 23844808967600604
CAMPAIGN_IDL2= 23844808967630604
CAMPAIGN_IDL3= 23844808967660604

CUSTOMAUDI_L1= 23844808973880604
CUSTOMAUDI_L2= 23844808973900604
CUSTOMAUDI_L3= 23844808973910604


AD_ACCOUNT_ID = 902035343547108
PAGE_ID_ADIMPACT=109802180769863
PAGE_ID_NUTRI=103496758063375
PAGE_ID_PIETONNI=106325221127660

my_account_id = credentials.my_account_id
my_app_id = credentials.my_app_id
my_app_secret = credentials.my_app_secret
my_access_token = credentials.my_access_token
# proxies = {'http': '<HTTP_PROXY>', 'https': '<HTTPS_PROXY>'} # add proxies if needed
ad_account = AdAccount(fbid=my_account_id)
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, my_account_id)
#####################################################################################################################################
targeting = {
    Targeting.Field.geo_locations: {
        Targeting.Field.countries: ['US'],
    },

}


#####################################################################################################################################
# def create_ad_set():

# today = datetime.date.today()
# start_time = str(today + datetime.timedelta(weeks=1))
# end_time = str(today + datetime.timedelta(weeks=2))


# adset = AdSet(parent_id='act_<AD_ACCOUNT_ID>')
# adset.update({
#   AdSet.Field.name: 'My_Ad_Set1306',
#  AdSet.Field.campaign_id:CAMPAIGN_ID,
# AdSet.Field.daily_budget: 1000,
# AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
# AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
# AdSet.Field.bid_amount: 2,
#  AdSet.Field.targeting: targeting,
# AdSet.Field.status: AdSet.Status.paused,
#  AdSet.Field.promoted_object: {"page_id": 109182080692597},
# AdSet.Field.start_time: start_time,
# AdSet.Field.end_time: end_time,
# })


# adset.remote_create(params=None)
#########################################################################################################

#######################################################################################################

today = datetime.date.today()
start_time = str(today + datetime.timedelta(weeks=1))
end_time = str(today + datetime.timedelta(weeks=2))

############################################"campaignExperiment_1_try_1"####################################################
fields = [
]
params = {
    'name': 'Test2_Oxfo_AdSetExperiment2_L1_D1',
    'lifetime_budget': '10000',
    'start_time': '2020-06-23T09:00:00-0800',
    'end_time': '2020-06-24T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL1,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L1}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_1_try_1')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))

############################################"campaignExperiment_1_try_2"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L1_D2',
    'lifetime_budget': '10000',
     'start_time': '2020-06-24T09:00:00-0800',
    'end_time': '2020-06-25T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL1,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L1}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_1_try_2')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))

############################################"campaignExperiment_1_try_3"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L1_D3',
    'lifetime_budget': '10000',
     'start_time': '2020-06-25T09:00:00-0800',
    'end_time': '2020-06-26T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL1,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L1}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_1_try_3')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))
############################################"campaignExperiment_2_try_1"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L2_D1',
    'lifetime_budget': '10000',
    'start_time': '2020-06-23T09:00:00-0800',
    'end_time': '2020-06-24T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL2,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L2}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_2_try_1')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))
############################################"campaignExperiment_2_try_2"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L2_D2',
    'lifetime_budget': '10000',
    'start_time': '2020-06-24T09:00:00-0800',
    'end_time': '2020-06-25T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL2,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L2}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_2_try_2')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))
############################################"campaignExperiment_2_try_3"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L2_D3',
    'lifetime_budget': '10000',
    'start_time': '2020-06-25T09:00:00-0800',
    'end_time': '2020-06-26T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL2,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L2}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_2_try_3')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))
############################################"campaignExperiment_3_try_1"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L3_D1',
    'lifetime_budget': '10000',
    'start_time': '2020-06-23T09:00:00-0800',
    'end_time': '2020-06-24T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL3,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L3}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_3_try_1')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))
############################################"campaignExperiment_3_try_2"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L3_D2',
    'lifetime_budget': '10000',
    'start_time': '2020-06-24T09:00:00-0800',
    'end_time': '2020-06-25T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL3,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L2}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_3_try_2')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))
############################################"campaignExperiment_3_try_3"####################################################
fields = [
]
params = {
    'name': 'Test2_New_Oxfo_AdSet_Experiment1_L3_D3',
    'lifetime_budget': '10000',
    'start_time': '2020-06-25T09:00:00-0800',
    'end_time': '2020-06-26T09:00:00-0800',
    'campaign_id': CAMPAIGN_IDL3,
    'bid_amount': '6000',
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {'age_min':13,'age_max':65,'custom_audiences':[{"id":CUSTOMAUDI_L3}],'device_platforms':['desktop'],'facebook_positions':['feed'],'publisher_platforms':['facebook']},
    'status': 'ACTIVE',
    'frequency_control_specs':[{"event": "IMPRESSIONS", "interval_days":1, "max_frequency":3}],
    'promoted_object': {'page_id': 106325221127660}

}
print('Adset_campaignExperiment_3_try_3')
print (AdAccount(my_account_id).create_ad_set(fields=fields,params=params))
######################################################CreateAd#####################################################
###################################################################################################################
