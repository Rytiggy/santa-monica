# coding: utf-8
# pip install cassiopeia

import cassiopeia as cass
import requests
from keys import * 
import random

# Lookup Variables
api_key = API_KEY
summoner_name = 'Miss'
cass.set_riot_api_key(api_key)  # This overrides the value set in your configuration/settings.
cass.set_default_region("NA")

summoner = cass.get_summoner(name=summoner_name)
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region))
champions = cass.get_champions()
random_champion = random.choice(champions)
print("She enjoys playing champions such as {name}.".format(name=random_champion.name))

challenger_league = cass.get_challenger_league(queue=cass.Queue.ranked_solo_fives)
best_na = challenger_league[0].summoner
print("She's not as good as {name} at League, but probably a better python programmer!".format(name=best_na.name))

from cassiopeia import Summoner

def print_summoner(name: str, region: str):
    summoner = Summoner(name=name, region=region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)
    print("Account ID:", summoner.account_id)
    print("Level:", summoner.level)
    print("Revision date:", summoner.revision_date)
    print("Profile icon ID:", summoner.profile_icon.id)
    print("Profile icon name:", summoner.profile_icon.name)
    print("Profile icon URL:", summoner.profile_icon.url)
    print("Profile icon image:", summoner.profile_icon.image)

print()
print(print_summoner(summoner_name, "NA"))
print()

# Get encryptedSummonerId from summoners v4 endpoint
summoner_by_name = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key=".format(summoner_name)
full_endpoint = summoner_by_name + api_key
# print(f"The full endpoint is {full_endpoint}")

# Execute request frome endpount
response = requests.get(full_endpoint)
print(f"The type of response: {type(response)}")

# Print encryptedSummonerId 
my_summoner_info = response.json()
