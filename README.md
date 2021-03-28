# covid-bot

COVID-Bot provides information on COVID-19 symptoms and precautions based on the Irish health service's (HSE) advice.

This application was created as coursework for the Cloud Application Development module in the Certificate in DevOps from [Munster Technological University](https://www.mtu.ie).

Covid-Bot was created using QnAMaker Natural Language Processing (NLP) Service and Azure Bot Framework v4.

## **Provided For Informational Purposes Only**

The information provided by this chat bot is freely available on the Irish health service's website ([https://www2.hse.ie/coronavirus](https://www2.hse.ie/coronavirus/)) and was current at the time the bot was created (March, 2021). It is not a replacement for professional medical advice. **Please contact your Primary Care Physician or GP if you experience any symptoms!**

## Configure Auto-Deployment of Covid-bot to Azure Bot Service

Azure Bot Service is capable of polling changes from your Bot's repository and deploying them.

### Deployment Pre-Requirements

- Azure Subscription.
- QnAMaker service has been deployed: <data/QnAMaker/README.md>
- Azure Bot Service has been created: <https://docs.microsoft.com/en-us/azure/bot-service/abs-quickstart?view=azure-bot-service-4.0>

### Deployment Steps

1. Open the Azure Portal, and navigate to the Azure Bot Service.
2. Select 'Deployment Center' from the left-hand menu.
3. Select the Settings tab, and then select Source: GitHub.
4. Change the provider to use 'App Service Build Service' (Kudu), to automatically deploy each commit to a specified branch.
5. Authorize GitHub, using your GitHub account credentials.
6. Select the following values:
   - *Organization*: your GitHub account name.
   - *Repository*: The repo name where your Bot code is stored.
   - *Branch* The branch from which the code will be deployed (typically 'main').
   ![img](/img/app-service-deployment-center-settings.PNG)
7. Push a commit, or merge a PR, into the specified branch to see the app being deployed.
8. Open the 'Logs' tab within Deployment Center to view the deployment history.

*Copyright (c) James Flynn 2021.*
