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

This app creates a simple CLI tool used to create and verify multi-factor auth codes using Bandwidth's Multi-Factor Auth API. The app will prompt the user for their phone number, followed by their preferred method of code delivery; either messaging or voice. The app will then text or call the phone number provided with a 6 digit MFA code that the user can enter back into the CLI to verify.

# Pre-Requisites

In order to use the Bandwidth API users need to set up the appropriate application at the [Bandwidth Dashboard](https://dashboard.bandwidth.com/) and create API tokens.

To create an application log into the [Bandwidth Dashboard](https://dashboard.bandwidth.com/) and navigate to the `Applications` tab.  Fill out the **New Application** form selecting the service (Messaging or Voice) that the application will be used for.  All Bandwidth services require publicly accessible Callback URLs, for more information on how to set one up see [Callback URLs](#callback-urls).

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
BW_ACCOUNT_ID                 # Your Bandwidth Account Id
BW_USERNAME                   # Your Bandwidth API Token
BW_PASSWORD                   # Your Bandwidth API Secret
BW_NUMBER                     # Your The Bandwidth Phone Number
BW_VOICE_APPLICATION_ID       # Your Voice Application Id created in the dashboard
BW_MESSAGING_APPLICATION_ID   # Your Messaging Application Id created in the dashboard
```
