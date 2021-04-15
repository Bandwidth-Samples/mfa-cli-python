# 2FA CLI Python 
<a href="http://dev.bandwidth.com"><img src="https://s3.amazonaws.com/bwdemos/BW-VMP.png"/></a>
</div>

 # Table of Contents

<!-- TOC -->

- [2FA CLI Python](#2fa-cli-python)
- [Description](#description)
- [Bandwidth](#bandwidth)
- [Environmental Variables](#environmental-variables)
- [Development Environment Setup](#development-environment-setup)
- [Run The App](#run-the-app)

<!-- /TOC -->

# Description
A small CLI sample app that creates a 2FA code request, and a 2FA code validation request via Bandwidth's 2FA API

# Bandwidth

In order to use the Bandwidth 2FA API, users need to have their applications setup. Please reach out to your account manager to set this up. 

For more information about API credentials see [here](https://dev.bandwidth.com/guides/accountCredentials.html#top)

# Environmental Variables
The sample app uses the below environmental variables.
```java
BW_ACCOUNT_ID                 // Your Bandwidth Account Id
BW_USERNAME                   // Your Bandwidth API Token
BW_PASSWORD                   // Your Bandwidth API Secret
BW_NUMBER               // Your The Bandwidth Phone Number
BW_VOICE_APPLICATION_ID       // Your Voice Application Id created in the dashboard
BW_MESSAGING_APPLICATION_ID   // Your Messaging Application Id created in the dashboard
```

# Development Environment Setup

```
pip install -r requirements.txt
```

# Run The App

```
python app.py
```
