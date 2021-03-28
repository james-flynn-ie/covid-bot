# covid-bot

COVID-Bot provides information on COVID-19 symptoms and precautions based on the Irish health service's (HSE) advice.

This application was created as coursework for the Cloud Application Development module in the Certificate in DevOps from [Munster Technological University](https://www.mtu.ie).

Covid-Bot was created using QnAMaker Natural Language Processing (NLP) Service and Azure Bot Framework v4.

## **Provided For Informational Purposes Only!**

The information provided by this chat bot is freely available on the Irish health service's website ([https://www2.hse.ie/coronavirus](https://www2.hse.ie/coronavirus/)) and was current at the time the bot was created (March, 2021). It is not a replacement for professional medical advice. **Please contact your Primary Care Physician or GP if you experience any symptoms!**

## Running with Bot Framework Emulator on localhost

Microsoft provides a tool for testing bot applications prior to deployment.

For instructions on setup, please see:
<https://docs.microsoft.com/en-us/azure/bot-service/bot-service-debug-emulator?view=azure-bot-service-4.0&tabs=python>

If you experience a 401 HTTP status code when using the Emulator please see the comments on how to resolve it in [config.py](config.py).

## Configuring Auto-Deployment of Covid-bot to Azure Bot Service

Azure Bot Service is capable of polling changes in your Bot's repository, providing a pipeline for automatically deploying changes from your main branch.

### Deployment Pre-Requirements

- Azure Subscription.
- Knowledge Base has been deployed on QnAMaker: [data/QnAMaker/README.md](data/QnAMaker/README.md)
- Azure Bot Service has been created: <https://docs.microsoft.com/en-us/azure/bot-service/abs-quickstart?view=azure-bot-service-4.0>
  - Ensure that the App Service which hosts the Bot is configured to run Python:

### Deploying Covid-bot using ARM Templates

Azure Resource Management (ARM) templates allow us to define our infrastructure as code within JSON files.

Microsoft provides an ARM template for deploying Azure Bots: [/deployment/template-with-preexisting-rg.json](/deployment/template-with-preexisting-rg.json)

To deploy the application, run the following steps:

1. Login using the account linked with your Azure subscription: `az login`
2. Set the subscription ID: `az account set --subscription <subscription_id>`
3. Create an application registration within Azure. This integrates IAM with the app: `az ad app create --display-name "displayName" --password "AtLeastSixteenCharacters_0" --available-to-other-tenants`
4. Deploy the Web App within the App Service: `az deployment group create --resource-group "<name-of-resource-group>" --template-file "<path-to-template-with-preexisting-rg.json>" --parameters appId="<app-id-from-previous-step>" appSecret="<password-from-previous-step>" botId="<id or bot-app-service-name>" newWebAppName="<bot-app-service-name>" existingAppServicePlan="<name-of-app-service-plan>" appServicePlanLocation="<region-location-name>" --name "<bot-app-service-name>"`
5. Zip the repository using your favourite archiving tool. The file `app.py` must be at the root of the ZIP file.
6. Deploy the ZIP using the following command: `az webapp deployment source config-zip --resource-group "<name-of-resource-group>" --name "<bot-app--name>" --src "path\to\file.zip"`

Please note that this deployment differs from the service deployed using the Azure portal, as it provides a 'Bot Channels Registration' rather than the Web App. Functionally, I am yet to observe a difference between them.

### Post-Deployment Steps: Set Covid-Bot environment variables

For Covid-Bot to connect with the QnAMaker service, some environment variables need to be set within App Service See [src/config.py](src/config.py).

- MicrosoftAppId
- MicrosoftAppPassword
- QnAKnowledgebaseId
- QnAEndpointKey
- QnAEndpointHostName

'MicrosoftAppId' and 'MicrosoftAppPassword' are set automatically by Azure App Service, but the other variables must be manually declared.

#### Declaring Environment Variables within Azure App Service

1. Open [QnAMaker](www.qnamaker.ai) and sign in with the account linked to your Azure Subscription.
2. Select the Knowledge Base to be used with your bot service.
3. Open the 'Settings' tab, and then note the following values under 'Deployment details':
   - Knowledge Base Id
   - Endpoint Key
   - Endpoint Host Name

4. Open Azure Portal, and navigate to the Azure App Service which is hosting the Bot Framework Service.
5. Select 'Configuration', and then select the 'Application Settings' tab.
6. Select 'New application setting', and then enter the QnA environment variable names along with the values gathered in Step 3:
   - name: `QnAKnowledgebaseId` , value: \<Knowledge Base Id\>
   - name: `QnAEndpointKey`, value: \<Endpoint Key\>
   - name: `QnAEndpointHostName`, value \<Endpoint Host Name\>
   ![img](img\add-app-service-env-vars.PNG)

7. Select Save, once all environment variables have been set.
   ![img](img\save-app-service-env-vars.PNG)

### Deployment Steps

1. Open the Azure Portal, and navigate to the Azure Bot Service.
2. Select 'Deployment Center' from the left-hand menu.
3. Select the Settings tab, and then select Source: GitHub.
4. Change the provider to use 'App Service Build Service' (Kudu), to automatically deploy each commit to a specified branch.
5. Authorize GitHub, using your GitHub account credentials.
6. Select the following values:
   - *Organization*: your GitHub account name.
   - *Repository*: The repo name where your Bot code is stored.
   - *Branch*: The branch from which the code will be deployed (typically 'main').
   ![img](/img/app-service-deployment-center-settings.PNG)
7. Push a commit, or merge a PR, into the specified branch to see the app being deployed.
8. Open the 'Logs' tab within Deployment Center to view the deployment history.

### Add Channels to Azure Bot Service

Azure Bot Framework refers to connections to user interface applications as 'Channels'.

A number of handlers are provided by Azure to connect the bot with platforms such as FaceBook, Twitter, Microsoft Teams, Twillio (SMS) and many others.

For more information on connecting Covid-bot with any of these channels, please read: <https://docs.microsoft.com/en-us/azure/bot-service/bot-service-manage-channels?view=azure-bot-service-4.0>

*Copyright (c) James Flynn 2021.*
