import requests
import json

get_token = requests.post("https://us.battle.net/oauth/token", data={'client_id': '6fbf754cc0134fe4b083471bc62bec28', 'client_secret': 'nIFh9vRBIpdGDD4khpHFlSc510OpcgxI', 'grant_type': 'client_credentials'})
response = get_token.json()
token = response["access_token"]

headers = {}
headers["Authorization"] = f"Bearer {token}"

def realm_request():

    realms = requests.get("https://us.api.blizzard.com/data/wow/search/connected-realm?namespace=dynamic-us&status.type=UP&realms.timezone=America%2FNew_York&orderby=id&_page=1&access_token=USLeGaNbhoZuMOBjIzYJ6oWlbf0A7dYakb", headers=headers)

    return realms.json()


def auction_request(realm_id):

    auctions = requests.get(f"https://us.api.blizzard.com/data/wow/connected-realm/{realm_id}/auctions?namespace=dynamic-us&locale=en_US&access_token=USLeGaNbhoZuMOBjIzYJ6oWlbf0A7dYakb", headers=headers)

    return auctions.json()


def class_request():

    classes = requests.get("https://us.api.blizzard.com/data/wow/item-class/index?namespace=static-us&locale=en_US&access_token=USLeGaNbhoZuMOBjIzYJ6oWlbf0A7dYakb", headers=headers)

    return classes.json()


def item_info(item_id):
    
    items = requests.get(f"https://us.api.blizzard.com/data/wow/item/{item_id}?namespace=static-us&locale=en_US&access_token=USLeGaNbhoZuMOBjIzYJ6oWlbf0A7dYakb", headers=headers)

    return items.json()


def item_media(item_id):

    media = requests.get(f"https://us.api.blizzard.com/data/wow/media/item/{item_id}?namespace=static-us&locale=en_US&access_token=USLeGaNbhoZuMOBjIzYJ6oWlbf0A7dYakb", headers=headers)

    return media.json()