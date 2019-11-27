# SECRET KEYS! Contact octopod.project@octo.com for access to the Octopod API
import pandas
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from tace_detection.utils.secret_octopod import OCTOPOD_CLIENT_ID, OCTOPOD_CLIENT_SECRET

token_url = 'https://octopod.octo.com/api/oauth/token'
post_data = {'grant_type': 'client_credentials',
             'client_id': OCTOPOD_CLIENT_ID,
             'client_secret': OCTOPOD_CLIENT_SECRET}
base_octopod_url = 'https://octopod.octo.com/api/v0'
client = BackendApplicationClient(client_id=OCTOPOD_CLIENT_ID)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, client_id=OCTOPOD_CLIENT_ID, client_secret=OCTOPOD_CLIENT_SECRET)


def get_octopod_info():
    all_octo_response = requests.get(base_octopod_url + '/people', token)
    return pandas.read_json(all_octo_response.text)
