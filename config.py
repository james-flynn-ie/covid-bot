#!/usr/bin/env python3
# Adapted on 14-March-2021 from: https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python/11.qnamaker

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    # Check that mandatory env vars are set, raise error if not set.
    MANDATORY_ENVIRONMENT_VARIABLES = ["MicrosoftAppId", "MicrosoftAppPassword", "QnAKnowledgebaseId", "QnAEndpointKey", "QnAEndpointHostName"]

    # Use this list instead, if you experience 401 status code from Bot Emulator (See comment block below for more information).
    #MANDATORY_ENVIRONMENT_VARIABLES = ["QnAKnowledgebaseId", "QnAEndpointKey", "QnAEndpointHostName"]

    for environmentVariable in MANDATORY_ENVIRONMENT_VARIABLES:
        if environmentVariable not in os.environ:
            raise EnvironmentError("Covid-Bot failed to start due to missing environment variable. Please set a value for \"{}\".".format(environmentVariable))

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    ##
    #  If you experience 401 HTTP status code when running with Bot Emulator locally, disable Auth.
    #  Comment out APP_ID and APP_PASSWORD above, and replace with the value, None.
    #  You'll also need to remove "MicrosoftAppId", "MicrosoftAppPassword" from MANDATORY_ENVIRONMENT_VARIABLES above.
    #
    #  IMPORTANT: For security reasons, don't deploy with no authentication on Azure!
    #  https://docs.microsoft.com/en-us/azure/bot-service/bot-service-troubleshoot-authentication-problems?view=azure-bot-service-4.0&tabs=python
    ##
    #APP_ID = None
    #APP_PASSWORD = None

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "")
