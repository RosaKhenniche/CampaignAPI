import sys

sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages')  # Replace this with the place you installed facebookbusiness using pip
sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages/facebook_business-7.0.1-py3.7.egg')  # same as above
sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages/facebookads-2.11.4.dist-info')
sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages/facebookads')
from facebook_business.adobjects.adaccount import AdAccount

from facebook_business.adobjects.campaign import Campaign

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebookads.adobjects.customaudience import CustomAudience
import credentials

my_account_id = credentials.my_account_id
my_app_id = credentials.my_app_id
my_app_secret = credentials.my_app_secret
my_access_token = credentials.my_access_token
# proxies = {'http': '<HTTP_PROXY>', 'https': '<HTTPS_PROXY>'} # add proxies if needed

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, my_account_id)

###################################################campaignExperiment_3_try_1"####################################################################
fields = [
]
params = {
  'name': 'Test2_Oxfo_campaignExperiment2_L1_',
  'subtype': 'CUSTOM',
  'description': '',
  'source':'',
  'customer_file_source': 'USER_PROVIDED_ONLY',
}

print ('1',AdAccount(my_account_id).create_custom_audience(
  fields=fields,
  params=params,
)  )

############################################################campaignExperiment_3_try_2##########################################################################

fields = [
]
params = {
  'name': 'Test2_Oxfo_campaignExperiment2_L2_',
  'subtype': 'CUSTOM',
  'description': '',
  'source':'',
  'customer_file_source': 'USER_PROVIDED_ONLY',
}

print ('2',AdAccount(my_account_id).create_custom_audience(
  fields=fields,
  params=params,
)  )
############################################################campaignExperiment_3_try_3##########################################################################

fields = [
]
params = {
  'name': 'Test2_Oxfo_campaignExperiment2_L3_',
  'subtype': 'CUSTOM',
  'description': '',
  'source':'',
  'customer_file_source': 'USER_PROVIDED_ONLY',
}

print ('3',AdAccount(my_account_id).create_custom_audience(
  fields=fields,
  params=params,
)  )
