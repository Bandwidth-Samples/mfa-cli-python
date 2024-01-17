import os
import sys

import bandwidth
from bandwidth import ApiException
import click
from InquirerPy import inquirer


try:
    BW_USERNAME = os.environ['BW_USERNAME']
    BW_PASSWORD = os.environ['BW_PASSWORD']
    BW_ACCOUNT_ID = os.environ['BW_ACCOUNT_ID']
    BW_NUMBER = os.environ['BW_NUMBER']
    BW_VOICE_APPLICATION_ID = os.environ['BW_VOICE_APPLICATION_ID']
    BW_MESSAGING_APPLICATION_ID = os.environ['BW_MESSAGING_APPLICATION_ID']
except KeyError:
    print("Please set the environmental variables defined in the README")
    sys.exit(1)

bandwidth_configuration = bandwidth.Configuration(
    username=BW_USERNAME,
    password=BW_PASSWORD
)

bandwidth_api_client = bandwidth.ApiClient(bandwidth_configuration)
bandwidth_mfa_api_instance = bandwidth.MFAApi(bandwidth_api_client)


@click.command()
def send_and_verify_mfa_code():
    code_expiry_time = 3

    phone_number = inquirer.text(
        message="Please enter the phone number to receive the MFA code, in E164 format (ex: +15555555555)",
        validate=lambda x: x.startswith("+1"),
    ).execute()
    channel = inquirer.rawlist(
        message="Would you like to send via SMS or Voice",
        choices=['SMS', 'Voice'],
    ).execute()

    code_request = bandwidth.models.CodeRequest(
        var_from=BW_NUMBER,
        to=phone_number,
        application_id="",
        scope="scope",
        digits=6,
        message="Your temporary {NAME} {SCOPE} code is {CODE}",
        expiration_time_in_minutes=code_expiry_time,
    )

    match channel:
        case "SMS":
            code_request.application_id = BW_MESSAGING_APPLICATION_ID
            try:
                bandwidth_mfa_api_instance.generate_messaging_code(BW_ACCOUNT_ID, code_request)
            except ApiException as e:
                print(f"Error sending code: {e}")
                sys.exit(1)
        case "Voice":
            code_request.application_id = BW_VOICE_APPLICATION_ID
            try:
                bandwidth_mfa_api_instance.generate_voice_code(BW_ACCOUNT_ID, code_request)
            except ApiException as e:
                print(f"Error sending code: {e}")
                sys.exit(1)

    code = inquirer.text(
        message="Please enter the code you received",
    ).execute()

    verify_code_request = bandwidth.models.VerifyCodeRequest(
        to=phone_number,
        code=code,
        expirationTimeInMinutes=code_expiry_time
    )

    try:
        bandwidth_mfa_api_instance.verify_code(BW_ACCOUNT_ID, verify_code_request)
        print("Code verified")
        sys.exit(0)
    except ApiException as e:
        print(f"Error verifying code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    send_and_verify_mfa_code()
