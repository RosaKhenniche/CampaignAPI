import sys
sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages') # Replace this with the place you installed facebookbusiness using pip
sys.path.append('home/rosa/anaconda3/lib/python3.7/site-packages/facebook_business-7.0.1-py3.7.egg') # same as above


from facebook_business.adobjects.adaccount import AdAccount

from facebook_business.adobjects.campaign import Campaign

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.customaudience import CustomAudience
import credentials
import createAdset
import json
import pymysql
import pymysql.cursors


###########################################"dataBase_Connexion"####################################################################
with open(r'database_credentials.json') as f:
    data = json.load(f)
    host = data['host']
    user = data['user']
    password = data['password']
    database = data['database']
    port = data['port']
    charset = data['charset']

conn = pymysql.connect(host='129.88.46.38', user='adanalyst', password='q2<u:%/C:-', database='AdAnalyst_EXT', port=3306, charset='utf8',
cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
###################################################################################################################################
my_account_id=credentials.my_account_id
my_app_id = credentials.my_app_id
my_app_secret = credentials.my_app_secret
my_access_token = credentials.my_access_token
# proxies = {'http': '<HTTP_PROXY>', 'https': '<HTTPS_PROXY>'} # add proxies if needed

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, my_account_id)
######################################################CREATECAMPAIGN###################################################################

class attributes:
    def __init__(self,name):
        self.name=name

exp1=attributes('Test2_Oxfo_campaignExperiment2_L1_')
exp2=attributes('Test2_Oxfo_campaignExperiment2_L2_')
exp3=attributes('Test2_Oxfo_campaignExperiment2_L3_')



def createCampaign(exp):
    fields = [
    ]
    params = {
        'name': exp.name,
        'objective': 'REACH',
        'status': 'ACTIVE',
        'special_ad_categories': [],
    }

    campaign= AdAccount(my_account_id).create_campaign(fields=fields, params=params, )
    return print (campaign)

if __name__=='__main__':

    camp=createCampaign(exp1)
    camp2 = createCampaign(exp2)
    camp3 = createCampaign(exp3)
    print ('This is the a try ')




