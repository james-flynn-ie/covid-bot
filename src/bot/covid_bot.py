# Adapted  on 14-March-2021 from: https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python/11.qnamaker

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

from config import DefaultConfig


class CovidBot(ActivityHandler):
    def __init__(self, config: DefaultConfig):
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            )
        )

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

    async def on_message_activity(self, turn_context: TurnContext):
        # The actual call to the QnA Maker service.
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0:
            await turn_context.send_activity(MessageFactory.text(response[0].answer))
        else:
            await turn_context.send_activity("I'm sorry, I don't understand the question. Can you rephrase it, please?")
