# QnAMaker KB Files

This folder contains exported Knowledge Base (KB) files for [QnAMaker](www.qnamaker.ai).

## What is QnAMaker

QnAMaker is a Natural Language Processing service which returns static information in response to questions inputted by a user. When integrated with Azure Bot Framework, it allows us to create conversational applications including chat bots and social media apps. 

For more information on QnAMaker, please see: [https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/)

## Importing a QnAMaker KB .TSV File

### Pre-Requisites

- Ensure a QnAMaker Resource in Azure Cognitive Services exists.

### Import .TSV File Steps

1. Go to [https://www.qnamaker.ai/Create](https://www.qnamaker.ai/Create) and login with your Azure user account.
2. Follow the steps outlined on the page, selecting the subscription and QnAMaker Resource names.
3. Give your KB a name.
4. Select `Enable multi-turn extraction from URLs, .pdf or .docx files`.
5. Select `Add File`, and then open the TSV file to be uploaded.
6. (Optional) Select `chit-chat` for responses to 'small talk questions'. Note that this can sometimes interfere with the KB search results and return incorrect answers.
7. Select `Create your KB`.

### What format does the .TSV file information present?

The .TSV format contains the following header values:

`Question	Answer	Source	Metadata	SuggestedQuestions	IsContextOnly	Prompts	QnaId`
