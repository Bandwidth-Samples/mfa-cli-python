"""
app.py

2FA CLI sample app using Bandwidth's 2FA API
"""
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.twofactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.twofactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema

import os

try:
    BW_USERNAME = os.environ['BW_USERNAME']
    BW_PASSWORD = os.environ['BW_PASSWORD']
    BW_ACCOUNT_ID = os.environ['BW_ACCOUNT_ID']
    BW_NUMBER = os.environ['BW_NUMBER']
    BW_VOICE_APPLICATION_ID = os.environ['BW_VOICE_APPLICATION_ID']
    BW_MESSAGING_APPLICATION_ID = os.environ['BW_MESSAGING_APPLICATION_ID']
except:
    print("Please set the environmental variables defined in the README")
    exit()

bandwidth_client = BandwidthClient(
    two_factor_auth_basic_auth_user_name=BW_USERNAME,
    two_factor_auth_basic_auth_password=BW_PASSWORD
)
auth_client = bandwidth_client.two_factor_auth_client.client

recipient_phone_number = input("Please enter your phone number in E164 format (+15554443333): ")
delivery_method = input("Select your method to receive your 2FA request. Please enter \"voice\" or \"messaging\": ")

if delivery_method == "messaging":
    from_phone = BW_NUMBER
    to_phone = recipient_phone_number
    application_id = BW_MESSAGING_APPLICATION_ID
    scope = "scope"
    digits = 6

    body = TwoFactorCodeRequestSchema(
        mfrom = from_phone,
        to = to_phone,
        application_id = application_id,
        scope = scope,
        digits = digits,
        message = "Your temporary {NAME} {SCOPE} code is {CODE}"
    )
    auth_client.create_messaging_two_factor(BW_ACCOUNT_ID, body)  

    code = input("Please enter your received code: ")

    body = TwoFactorVerifyRequestSchema(
        mfrom = from_phone,
        to = to_phone,
        application_id = application_id,
        scope = scope,
        code = code,
        digits = digits,
        expiration_time_in_minutes = 3
    )
    response = auth_client.create_verify_two_factor(BW_ACCOUNT_ID, body)

    if response.body.valid:
        print("Success!")
    else:
        print("Failure")
else:
    from_phone = BW_NUMBER
    to_phone = recipient_phone_number
    application_id = BW_VOICE_APPLICATION_ID
    scope = "scope"
    digits = 6

    body = TwoFactorCodeRequestSchema(
        mfrom = from_phone,
        to = to_phone,
        application_id = application_id,
        scope = scope,
        digits = digits,
        message = "Your temporary {NAME} {SCOPE} code is {CODE}"
    )
    auth_client.create_voice_two_factor(BW_ACCOUNT_ID, body)  

    code = input("Please enter your received code: ")

    body = TwoFactorVerifyRequestSchema(
        mfrom = from_phone,
        to = to_phone,
        application_id = application_id,
        scope = scope,
        code = code,
        digits = digits,
        expiration_time_in_minutes = 3
    )
    response = auth_client.create_verify_two_factor(BW_ACCOUNT_ID, body)

    if response.body.valid:
        print("Success!")
    else:
        print("Failure")
