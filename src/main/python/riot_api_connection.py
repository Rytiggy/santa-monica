# coding: utf-8

import requests

my_api_key = "RGAPI-9c2b1602-ebbe-4c9e-8068-8698ca534623"
summoner_miss = 'Miss'
summoner_slayre = 'Slayre'
summoner_by_name = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key=".format(summoner_slayre)

full_endpoint = summoner_by_name + my_api_key
full_endpoint


response = requests.get(full_endpoint)
type(response)


my_summoner_info = response.json()
my_summoner_info['id']

