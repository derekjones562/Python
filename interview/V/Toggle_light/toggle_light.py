import json

import requests


class VivintLightSwitchTest(object):
    """ Class for testing a lightswitch via api """

    def __init__(self, *args):
        self.api_url = "https://vivintsky.com/api/5077675869538674/1/switches/77"
        self.content_type = "application/json"
        self.auth = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1Yzk1MGVkOTM1MGU1OGRjM2UzMjIwMDUiLCJlbWFpbCI6ImRlcmVrLmpvbmVzNTYyQGdtYWlsLmNvbSIsImF1ZCI6ImYzYzE4ZTE2NjhhNzQ4Yjc4MzhiY2VmNzRmZGViM2Y2IiwianRpIjoiSklGNzNsQW5EQ0dSYjdUVjR2VHRUMCIsImlzcyI6Imh0dHBzOlwvXC9pZC52aXZpbnQuY29tIiwiaWF0IjoxNTUzMjcyNTUwLCJleHAiOjE1NTMyNzQzNTAsInBpLnNyaSI6ImVZZ19xd041UGI5WklqcktxMGEtdjNJeTZuZyIsIm5vbmNlIjoiTFRhbWpDa1ZsNHNLS0pIREdzS0JvbGRsTktRWlV2Z08ifQ.2CnYl7Q82zaGRROEEgr1lpjBekR56AhLjdqSOLffxtw"
        self.cookie = "oauth_state=ECe3EjApCogyHp2tmBXjUquElqZjvGFl; oidc_nonce=LTamjCkVl4sKKJHDGsKBoldlNKQZUvgO; id_token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1Yzk1MGVkOTM1MGU1OGRjM2UzMjIwMDUiLCJlbWFpbCI6ImRlcmVrLmpvbmVzNTYyQGdtYWlsLmNvbSIsImF1ZCI6ImYzYzE4ZTE2NjhhNzQ4Yjc4MzhiY2VmNzRmZGViM2Y2IiwianRpIjoiSklGNzNsQW5EQ0dSYjdUVjR2VHRUMCIsImlzcyI6Imh0dHBzOlwvXC9pZC52aXZpbnQuY29tIiwiaWF0IjoxNTUzMjcyNTUwLCJleHAiOjE1NTMyNzQzNTAsInBpLnNyaSI6ImVZZ19xd041UGI5WklqcktxMGEtdjNJeTZuZyIsIm5vbmNlIjoiTFRhbWpDa1ZsNHNLS0pIREdzS0JvbGRsTktRWlV2Z08ifQ.2CnYl7Q82zaGRROEEgr1lpjBekR56AhLjdqSOLffxtw; mp_bd4f702237eb092bf4e2eaacdf17437d_mixpanel=%7B%22distinct_id%22%3A%20%22derek.jones562%40gmail.com%22%2C%22%24device_id%22%3A%20%22169a641e29c3f4-07202441fea66d-36617902-1fa400-169a641e29d552%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22Screen%20Mode%22%3A%20%22Desktop%22%2C%22%24user_id%22%3A%20%22derek.jones562%40gmail.com%22%2C%22App%22%3A%20%22Web%22%2C%22Version%22%3A%20%220.0.5032%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22Panel%20Id%22%3A%205077675869538674%2C%22Service%20Number%22%3A%205497149%2C%22Panel%20Version%22%3A%200%7D"
        self.data = {"s": False,
                      "_id": 77
                      }

    def _get_headers(self):
        headers = {'Cookie': self.cookie,
                   'Authorization': self.auth,
                   'Content-Type': self.content_type}
        return headers

    def toggle_on(self):
        self.data['s'] = True
        response = requests.put(self.api_url, data=json.dumps(self.data), headers=self._get_headers())
        print (response)

    def toggle_off(self):
        self.data['s'] = False
        response = requests.put(self.api_url, data=json.dumps(self.data), headers=self._get_headers())
        print(response)




lightswitch = VivintLightSwitchTest()
#lightswitch.toggle_on()
lightswitch.toggle_off()