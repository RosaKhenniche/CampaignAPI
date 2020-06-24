
import credentials
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adimage import AdImage

from facebook_business.adobjects.helpers.adimagemixin import AdImageMixin
my_account_id = credentials.my_account_id
my_app_id = credentials.my_app_id
my_app_secret = credentials.my_app_secret
my_access_token = credentials.my_access_token
# proxies = {'http': '<HTTP_PROXY>', 'https': '<HTTPS_PROXY>'} # add proxies if needed

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, my_account_id)



CREATIVE_ID_POS=23844809362720604
CREATIVE_ID_NEG=23844809491940604
CREATIVE_ID_NEUT=23844809363200604

####################################################################################################################


#####################################################################################################################
############################################"Test2_New_Nutri_Ad_Experiment1_L1_D1_positive"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L1_D1_',
  'adset_id': '23844809029940604',
  'creative': {'creative_id': CREATIVE_ID_POS },
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L1_D2_NEGATIVE"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L1_D2_',
  'adset_id': '23844809030080604',
  'creative': {'creative_id': CREATIVE_ID_POS},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L1_D3_NEUTRE"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L1_D3_',
  'adset_id': '23844809479600604',
  'creative': {'creative_id': CREATIVE_ID_POS},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L2_D1_positive"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L2_D1_',
  'adset_id': '23844809032480604',
  'creative': {'creative_id': CREATIVE_ID_NEG},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L2_D2_negative"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L2_D2_',
  'adset_id': '23844809033000604',
  'creative': {'creative_id': CREATIVE_ID_NEG},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L2_D3_neutre"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L2_D3_',
  'adset_id': '23844809033240604',
  'creative': {'creative_id': CREATIVE_ID_NEG},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L3_D1_POSITIVE"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L3_D1_',
  'adset_id': '23844809033410604',
  'creative': {'creative_id': CREATIVE_ID_NEUT},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L3_D2_negative"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L3_D2_',
  'adset_id': '23844809033410604',
  'creative': {'creative_id': CREATIVE_ID_NEUT},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L3_D3_neutre"####################################################

fields = [
]
params = {
  'name': 'Test2_New_Oxfo_Ad_Experiment1_L3_D3_',
  'adset_id': '23844809034290604',
  'creative': {'creative_id': CREATIVE_ID_NEUT},
  'status': 'ACTIVE',
}
print( AdAccount(my_account_id).create_ad(
  fields=fields,
  params=params,
))