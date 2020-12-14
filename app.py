"""
app.py

2FA CLI sample app using Bandwidth's 2FA API
"""
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.twofactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.twofactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema

import os

try:
    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']
    ACCOUNT_ID = os.environ['ACCOUNT_ID']
    PHONE_NUMBER = os.environ['PHONE_NUMBER']
    VOICE_APPLICATION_ID = os.environ['VOICE_APPLICATION_ID']
    MESSAGING_APPLICATION_ID = os.environ['MESSAGING_APPLICATION_ID']
except:
    print("Please set the environmental variables defined in the README")
    exit()

bandwidth_client = BandwidthClient(
    two_factor_auth_basic_auth_user_name=USERNAME,
    two_factor_auth_basic_auth_password=PASSWORD
)
auth_client = bandwidth_client.two_factor_auth_client.client

recipient_phone_number = input("Please enter your phone number in E164 format (+15554443333): ")
delivery_method = input("Select your method to receive your 2FA request. Please enter \"voice\" or \"messaging\": ")

if delivery_method == "messaging":
    from_phone = PHONE_NUMBER
    to_phone = recipient_phone_number
    application_id = MESSAGING_APPLICATION_ID
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
    auth_client.create_messaging_two_factor(ACCOUNT_ID, body)  

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
    response = auth_client.create_verify_two_factor(ACCOUNT_ID, body)

    if response.body.valid:
        print("Success!")
    else:
        print("Failure")
else:
    from_phone = PHONE_NUMBER
    to_phone = recipient_phone_number
    application_id = VOICE_APPLICATION_ID
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
    auth_client.create_voice_two_factor(ACCOUNT_ID, body)  

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
    response = auth_client.create_verify_two_factor(ACCOUNT_ID, body)

    if response.body.valid:
        print("Success!")
    else:
        print("Failure")
