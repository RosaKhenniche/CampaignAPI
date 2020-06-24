
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


PAGE_ID_PIETONNI=106325221127660


####################################################################################################################


#####################################################################################################################
############################################"Test2_New_Nutri_Ad_Experiment1_L1_D1_positive"####################################################
def hashedImage():
  image = AdImage(parent_id=my_account_id)
  image[AdImage.Field.filename] = 'oxford_posi.jpg'
  image.remote_create()
  hashed = image[AdImage.Field.hash]
  return   hashed


# Output image Hash



fields = [

]
params = {
    'name': 'Sample Creative',

    'object_story_spec': {'page_id': PAGE_ID_PIETONNI,
                          'link_data': {'image_hash': hashedImage(), 'link': 'https://londonist.com/london/news/oxford-street',
                                        'message': 'Oxford Street is going car-free! The plan is aimed at tackling growing air quality concerns and congestion at peak travel level',
                                        'title': 'Oxford Street is going car-free! The plan is aimed at tackling growing air quality concerns and congestion at peak travel level'}},
}
print('positive')
print(AdAccount(my_account_id).create_ad_creative(
    fields=fields,
    params=params,
))

############################################"Test2_New_Nutri_Ad_Experiment1_L1_D2_negative"####################################################
def hashedImage():
  image = AdImage(parent_id=my_account_id)
  image[AdImage.Field.filename] = 'negative.jpg'
  image.remote_create()
  hashed = image[AdImage.Field.hash]
  return   hashed


# Output image Hash



fields = [

]
params = {
    'name': 'Sample Creative',

    'object_story_spec': {'page_id': PAGE_ID_PIETONNI,
                          'link_data': {'image_hash': hashedImage(), 'link': 'https://londonist.com/london/news/oxford-street',
                                        'message': 'It is not only about Oxford Street itself but many neighboring ones too. That would create a new congestion problem',
                                        'title':'It is not only about Oxford Street itself but many neighboring ones too. That would create a new congestion problem'}},
}
print('negative')
print(AdAccount(my_account_id).create_ad_creative(
    fields=fields,
    params=params,
))
############################################"Test2_New_Nutri_Ad_Experiment1_L1_D1_neutre"####################################################
def hashedImage():
  image = AdImage(parent_id=my_account_id)
  image[AdImage.Field.filename] = 'Oxford_neu.jpg'
  image.remote_create()
  hashed = image[AdImage.Field.hash]
  return   hashed


# Output image Hash



fields = [

]
params = {
    'name': 'Sample Creative',

    'object_story_spec': {'page_id': PAGE_ID_PIETONNI,
                          'link_data': {'image_hash': hashedImage(), 'link': 'https://www.curbed.com/2017/11/7/16618438/london-oxford-street-car-free-pedestrian-plan',
                                        'message': 'Oxford Street is going car-free! the first stage was wrapped in 2018. The second and third would be completed in 2020',
                                        'title':'Oxford Street is going car-free! the first stage was wrapped in 2018. The second and third would be completed in 2020'}},
}
print('neutre')
print(AdAccount(my_account_id).create_ad_creative(
    fields=fields,
    params=params,
))