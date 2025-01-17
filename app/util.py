""" Use library here to format nested dictionary"""
import hashlib
import requests
import stripe
from app.config import REWARDS
import base64 # base32 is a function in base64
import hashlib

# email = "somebody@example.com"






salt = str("a6ecdd933b3842bcb467fed4073cb852")



stripe.api_key = "sk_live_WxCFh6xG9z079NoOOy4Nufbp"




# Put together who referred who



def send_simple_message(email, subject, html_template):
    return requests.post(
        "https://api.mailgun.net/v3/funguana.com/messages",
        auth=("api", "key-b42d805f39588a464b8db0daaeb0d380"),
        data={"from": "Funguana, Inc <kevin@funguana.com>",
              "to": [email],
              "subject": "{}".format(subject),
              "html": "<html>{}</html>".format(html_template)
        })


def check_and_send(first, second, third):
    """ Gets the first second and thrid level referrals and checks to see if the user earned a reward"""
    ref_check = ['first', 'second', 'third']
    pass

def any_none(array_of_values):
    if not isinstance(array_of_values, list):
        return False
    
    for i in array_of_values:
        if i is None:
            return False
    
    return True


def hash_pass(password):
    password = str(password)
    hashed = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
    return hashed


def which_none(dict_of_values):
    if not isinstance(dict_of_values, dict):
        return []
    
    ret_list = []
    dict_keys = dict_of_values.keys()
    for key in dict_keys:
        if dict_of_values[key] is None:
            ret_list.append(key)
    
    return ret_list



def referral_hash(email):
    md5 = hashlib.md5()
    md5.update(email.encode('utf-8'))

    hash_in_bytes = md5.digest()

    result = base64.b32encode(hash_in_bytes)


    # Or you can remove the extra "=" at the end

    result = result.strip(b'=')
    
    return str(result.decode("utf-8"))



def formatting(status, msg, data):
    return {
        "status": status,
        "msg": msg,
        "data": data
    }

