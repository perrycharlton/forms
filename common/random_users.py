from urllib import request
import json


def get_users(paras=2):
    b_uri = "https://randomuser.me/api/?"
    b_amount = "results=" + str(paras)
    passwords = "password=special,upper,8,20"
    nat = "nat=gb"
    uri = b_uri + b_amount + '&' + passwords + '&' + nat
    try:
        uResponse = request.urlopen(uri)
    except request.HTTPError:
        return "Connection Error"
    text = json.loads(uResponse.read().decode('utf-8'))

    return text['results']