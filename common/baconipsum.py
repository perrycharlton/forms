from urllib import request
# from flask import Blueprint
# bacon = Blueprint('bacon', __name__)


def get_bacon(paras=2):
    b_uri = "https://baconipsum.com/api/?callback=?"
    b_type = "type=meat-and-filler"
    b_amount = "paras=" + str(paras)
    uri = b_uri + '&' + b_type + '&' + b_amount
    try:
        uResponse = request.urlopen(uri)
    except request.HTTPError:
        return "Connection Error"
    text = uResponse.read().decode('utf-8').strip('"[]').splitlines()

    return text
