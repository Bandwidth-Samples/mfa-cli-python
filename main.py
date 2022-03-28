import os
import re

# TODO: Needs to be changed when the SDK becomes python package.
import sys
sys.path.insert(0, 'C:/Users/ckoegel/Documents/sdks/bandwidth_python')
import bandwidth_python
from bandwidth_python.api.mfa_api import MFAApi
from bandwidth_python.model.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth_python.model.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth_python.exceptions import ApiException
# ---------------------------------------------------


BW_ACCOUNT_ID = os.environ.get('BW_ACCOUNT_ID')
BW_USERNAME = os.environ.get('BW_USERNAME')
BW_PASSWORD = os.environ.get('BW_PASSWORD')
BW_NUMBER = os.environ.get('BW_NUMBER')
BW_VOICE_APPLICATION_ID = os.environ.get('BW_VOICE_APPLICATION_ID')
BW_MESSAGING_APPLICATION_ID = os.environ.get('BW_MESSAGING_APPLICATION_ID')


configuration = bandwidth_python.Configuration(     # TODO:  # Configure HTTP basic authorization: httpBasic
    username=BW_USERNAME,
    password=BW_PASSWORD
)


api_client = bandwidth_python.ApiClient(configuration)  # TODO: package name
mfa_api_instance = MFAApi(api_client) # TODO: package name

recipient_phone_number = input("\nPlease enter your phone number in E164 format (+19195551234): ")
while True:
    if re.match(r"^\+[1-9]\d{4,14}$", recipient_phone_number):
        break
    else:
        recipient_phone_number = input("Invalid phone number. Please enter your phone number in E164 format (+19195551234): ")



delivery_method = input("\nPlease select your MFA method.\nEnter 0 for voice or 1 for messaging: ")
while True:
    if re.match(r"^[0-1]$", delivery_method):
        break
    else:
        delivery_method = input("Invalid selection. Enter 0 for voice or 1 for messaging: ")


if bool(int(delivery_method)):

    body = TwoFactorCodeRequestSchema(
        _from = BW_NUMBER,
        to = recipient_phone_number,
        application_id = BW_MESSAGING_APPLICATION_ID,
        scope = "scope",
        digits = 6.0,
        message = "Your temporary {NAME} {SCOPE} code is {CODE}"
    )
    mfa_api_instance.messaging_two_factor(BW_ACCOUNT_ID, body)  

    code = input("\nPlease enter your received code: ")

    body = TwoFactorVerifyRequestSchema(
        to = recipient_phone_number,
        application_id = BW_MESSAGING_APPLICATION_ID,
        scope = "scope",
        code = code,
        expiration_time_in_minutes = 3.0
    )
else:
    body = TwoFactorCodeRequestSchema(
        _from = BW_NUMBER,
        to = recipient_phone_number,
        application_id = BW_VOICE_APPLICATION_ID,
        scope = "scope",
        digits = 6.0,
        message = "Your temporary {NAME} {SCOPE} code is {CODE}"
    )
    mfa_api_instance.voice_two_factor(BW_ACCOUNT_ID, body)  

    code = input("\nPlease enter your received code: ")

    body = TwoFactorVerifyRequestSchema(
        to = recipient_phone_number,
        application_id = BW_VOICE_APPLICATION_ID,
        scope = "scope",
        code = code,
        expiration_time_in_minutes = 3.0
    )

try:
    response = mfa_api_instance.verify_two_factor(BW_ACCOUNT_ID, body)

    if response.valid:
        print("Success!")
    else:
        print("Incorrect Code")

except ApiException as e:
    print(e)


   