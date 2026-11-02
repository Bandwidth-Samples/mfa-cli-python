# Multi-Factor Auth CLI

<a href="https://dev.bandwidth.com/docs/mfa/">
  <img src="./icon-mfa.svg" title="Multi-Factor Auth About Page" alt="Multi-Factor Auth About Page"/>
</a>

# Table of Contents

* [Description](#description)
* [Pre-Requisites](#pre-requisites)
* [Running the Application](#running-the-application)
* [Environmental Variables](#environmental-variables)

# Description

This sample app is a command line tool that sends and verifies multi-factor auth codes using Bandwidth's Multi-Factor Auth API.

The app asks for a phone number in E.164 format and whether to send the code by `messaging` or `voice` (`messaging` if left blank). It then texts or calls that number with a 6 digit code, asks you to enter the code, and checks it. The app exits with status `0` if the code is verified and `1` otherwise.

# Pre-Requisites

In order to use the Bandwidth API users need to set up the appropriate applications at the [Bandwidth Dashboard](https://dashboard.bandwidth.com/) and create API tokens.

This app needs two applications, one for each delivery method. To create an application log into the [Bandwidth Dashboard](https://dashboard.bandwidth.com/) and navigate to the `Applications` tab. Fill out the **New Application** form once selecting Messaging, and once selecting Voice. This app doesn't receive any callbacks, so the callback URLs can be left as placeholders.

For more information about API credentials see our [Account Credentials](https://dev.bandwidth.com/docs/account/credentials) page.

# Running the Application

To install the required packages for this app, run the command:

```sh
pip install -r requirements.txt
```

Use the following command to run the application:

```sh
python main.py
```

# Environmental Variables

The sample app uses the below environmental variables.

```sh
BW_ACCOUNT_ID                        # Your Bandwidth Account Id
BW_CLIENT_ID                         # Your Bandwidth API OAuth Client Id
BW_CLIENT_SECRET                     # Your Bandwidth API OAuth Client Secret
BW_NUMBER                            # The Bandwidth phone number the code is sent from
BW_VOICE_APPLICATION_ID              # Your Voice Application Id created in the dashboard
BW_MESSAGING_APPLICATION_ID          # Your Messaging Application Id created in the dashboard
```
