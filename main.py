import os
import re
import sys

import bandwidth

try:
    BW_ACCOUNT_ID = os.environ['BW_ACCOUNT_ID']
    BW_CLIENT_ID = os.environ['BW_CLIENT_ID']
    BW_CLIENT_SECRET = os.environ['BW_CLIENT_SECRET']
    BW_NUMBER = os.environ['BW_NUMBER']
    BW_VOICE_APPLICATION_ID = os.environ['BW_VOICE_APPLICATION_ID']
    BW_MESSAGING_APPLICATION_ID = os.environ['BW_MESSAGING_APPLICATION_ID']
except KeyError as e:
    print(f"Please set the environmental variables defined in the README\n\n{e}")
    sys.exit(1)

bandwidth_configuration = bandwidth.Configuration(
    client_id=BW_CLIENT_ID,
    client_secret=BW_CLIENT_SECRET
)

bandwidth_api_client = bandwidth.ApiClient(bandwidth_configuration)
bandwidth_mfa_api_instance = bandwidth.MFAApi(bandwidth_api_client)

E164_PATTERN = re.compile(r"^\+[1-9]\d{1,14}$")
SCOPE = "sample"


def prompt(text: str) -> str:
    try:
        return input(text).strip()
    except EOFError:
        sys.exit(1)


def main():
    phone_number = prompt("Enter the phone number to send the code to (E.164, e.g. +15554443333): ")
    if not E164_PATTERN.match(phone_number):
        print("Phone number must be in E.164 format, e.g. +15554443333", file=sys.stderr)
        sys.exit(1)

    method = prompt("Send the code by messaging or voice? [messaging]: ").lower() or "messaging"
    if method not in ("messaging", "voice"):
        print("Method must be messaging or voice", file=sys.stderr)
        sys.exit(1)

    print(f"Sending a code by {method} to {phone_number}")
    try:
        code_request = bandwidth.models.CodeRequest(
            to=phone_number,
            var_from=BW_NUMBER,
            application_id=BW_VOICE_APPLICATION_ID if method == "voice" else BW_MESSAGING_APPLICATION_ID,
            scope=SCOPE,
            message="Your temporary {NAME} {SCOPE} code is {CODE}",
            digits=6
        )
        if method == "voice":
            bandwidth_mfa_api_instance.generate_voice_code(BW_ACCOUNT_ID, code_request)
        else:
            bandwidth_mfa_api_instance.generate_messaging_code(BW_ACCOUNT_ID, code_request)
    except Exception as e:
        print(f"Failed to send code: {e}", file=sys.stderr)
        sys.exit(1)

    code = prompt("Enter the code you received: ")
    try:
        verify_request = bandwidth.models.VerifyCodeRequest(
            to=phone_number,
            scope=SCOPE,
            expiration_time_in_minutes=3,
            code=code
        )
        valid = bandwidth_mfa_api_instance.verify_code(BW_ACCOUNT_ID, verify_request).valid
    except Exception as e:
        print(f"Failed to verify code: {e}", file=sys.stderr)
        sys.exit(1)

    print("Code verified" if valid else "Code not verified")
    sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()
