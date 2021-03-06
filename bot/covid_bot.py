## Adapted on 14-March-2021 from: https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python/11.qnamaker

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

# Add parent directory to sys.path, so that the config module is found in the module search path.
# Westra, E (2016) "Modular Programming with Python", Packt Publishing, retrieved on 28-March-2021:
#     https://www.oreilly.com/library/view/modular-programming-with/9781785884481/ch07s03.html
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
# os.path.dirname returns the path without the currentDir attached, (i.e.: the parent directory).
#    Retrieved on 28-March-2021: https://appdividend.com/2021/01/22/python-os-path-dirname-function-with-example
parentDir = os.path.dirname(currentDir)
sys.path.insert(0, parentDir)

import config


class CovidBot(ActivityHandler):
    def __init__(self, config: config.DefaultConfig):
        self.qna_maker = QnAMaker(
            # https://docs.microsoft.com/en-us/python/api/botbuilder-ai/botbuilder.ai.qna.qnamaker_endpoint.qnamakerendpoint?view=botbuilder-py-latest
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            )
        )

    # https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-send-messages?view=azure-bot-service-4.0&tabs=python
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Hello, I’m COVID-bot. "
                    "I’m here to share with you the HSE website’s current advice "
                    "on COVID-19 (as of March 2021) and how to prevent it spreading. "
                    "I’m not a Doctor though, so please contact your GP straight away "
                    "if you have any health concerns."
                )

    # https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-primitive-prompts?view=azure-bot-service-4.0&tabs=python#create-property-accessors
    async def on_message_activity(self, turn_context: TurnContext):
        # The actual call to the QnA Maker service.
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0:
            await turn_context.send_activity(MessageFactory.text(response[0].answer))
        else:
            await turn_context.send_activity("I'm sorry, I don't understand the question. Can you rephrase it, please?")
