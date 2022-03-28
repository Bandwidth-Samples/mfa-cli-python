# Multi-Factor Auth CLI

<a href="https://dev.bandwidth.com/docs/mfa">
  <img src="./icon-mfa.svg" title="Multi-Factor Auth About Page" alt="Multi-Factor Auth About Page"/>
</a>

 # Table of Contents

* [Description](#description)
* [Pre-Requisites](#pre-requisites)
* [Running the Application](#running-the-application)
* [Environmental Variables](#environmental-variables)

# Description

This app allows you to enter your phone number in E164 format to receive a multi-factor auth code either by voice or sms. After entering your phone number and selecting the mfa method, you will receive a text message or phone call with your authentication code. Entering this code in the final prompt will allow you to verify the code. Note that you will need separate applications for voice and messaging depending on which method you would like to use. More information about the application setup can be found in the [Pre-Requisites](#pre-requisites) section.

This app also demonstrates basic API Error handling. By entering an invalid code (e.g. 1), you will receive a `400 Bad Request` from the API, which is handled by the `except` statement at the end of the app.

# Pre-Requisites

In order to use the Bandwidth API users need to set up the appropriate application at the [Bandwidth Dashboard](https://dashboard.bandwidth.com/) and create API tokens.

To create an application log into the [Bandwidth Dashboard](https://dashboard.bandwidth.com/) and navigate to the `Applications` tab.  Fill out the **New Application** form selecting the service (Messaging or Voice) that the application will be used for.

For more information about API credentials see our [Account Credentials](https://dev.bandwidth.com/docs/account/credentials) page.

# Running the Application

Use the following command to run the application:

```sh
python main.py
```

# Environmental Variables

The sample app uses the below environmental variables.

```sh
BW_ACCOUNT_ID                        # Your Bandwidth Account Id
BW_USERNAME                          # Your Bandwidth API Username
BW_PASSWORD                          # Your Bandwidth API Password
BW_NUMBER                            # The Bandwidth phone number involved with this application
BW_VOICE_APPLICATION_ID              # Your Voice Application Id created in the dashboard
BW_MESSAGING_APPLICATION_ID          # Your Messaging Application Id created in the dashboard
```
