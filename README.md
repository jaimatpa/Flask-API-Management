# flask_6_api_management

## Flask-based RESTful API 
- I created the file `app_basic.py` which houses code for a home page and a hello page. Once you enter `python app_basic.py` in the terminal, and click the provided link, you are redirected to the home page. The home page returns the response "Hello from my Flask API Endpoint Server", and the hello page returns the message of 'Hello <first and last name inputted in the url> in capital letters. One can get to the hello page by entering `hello?name=write_a_name_here&lastname=write_a_last_name_here`. To test this, I write my first name after "name=" and my last name after "lastname=", as seen in the screenshot in the `Screenshots` folder.
- In the `app_flasgger.py` file, I included the hello page and response in the code. 

## Azure API deployment 
1. The first step in the Azure API deployment is to download, install Azure CLI, and connect your Google Cloud Shell to your Azure account. 
   - [Documentation for further help or understanding](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
 - In your Google Cloud Shell terminal type the command `curl -sL https://aka InstallAzureCLIDeb | sudo bash` to install Azure CLI
 - To test the installaation type `az` into the terminal and hit enter
 - After that login `az login --use-device-code`
     - a link will appear and copy the authentication code it provides, click the link,         provide the code and sign into your Azure account.
2. In the terminal, install the Azure Core Tools package `sudo apt-get install azure-       functions-core-tools-4`
    - [Following this tutorial](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=linux%2Cbash%2Cazure-cli&pivots=python-mode-decorators)
3. Ensure you are in the right directly, if not utilize the command `cd` to go into the right one, and run the command `func init LocalFunctionProj --python -m V2`
  - go into the project folder that was created by the previous command, to achieve this     utilize this command `cd LocalFunctionProj`.
4. In the folder, there is a `function_app.py` file that was created, replace the contents of the file with this code:
```
import azure.functions as func
    
app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")
```
4. Open the file `local.settings.json` and ensure that next to `AzureWebJobsFeatureFlags` has the value of `EnableWorkerIndexing` and update the `AzureWebJobsStorage` to:  `"AzureWebJobsStorage": "UseDevelopmentStorage=true"`
5. Run the function locally by `func start`
   - The terminal will look like this: ![image](https://github.com/amnasyed1/flask_6_api_management/assets/123895397/23e2267f-9a19-4a62-a88a-fc7829ce5480)
   - click the link, and edit the URL so it looks like `http://localhost:7071/api/HttpExample?name=write_your_name_here`
6. Create Azure resouces for your function to deploy the application:
 - Create a resource group: `az group create --name <name of your resource group> --location <REGION>`. [Use this link to fnd your region](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/#geographies). For instance, if you are in the Eastern part of the United States, input `eastus`.
 - Create a storage account: `az storage account create --name <STORAGE_NAME> --location <REGION> --resource-group <resource group name> --sku Standard_LRS`
 - Create the function app in Azure: `az functionapp create --resource-group <resource group name> --consumption-plan-location westeurope --runtime python --runtime-version 3.9 --functions-version 4 --name <APP_NAME> --os-type linux --storage-account <STORAGE_NAME>`
7. To deploy the function project to azure `func azure functionapp publish <APP_NAME>`
   - Once completed, your terminal will look similar to this: ![image](https://github.com/amnasyed1/flask_6_api_management/assets/123895397/9a7ef2bb-2693-430e-85a3-f26bfa763047)
   - Click the link and your app is successfully deployed.

## OpenAPI Specification
- The `app_flasgger.py` file details the code utilizd.
- To open swagger, in the terminal run `python app_flasgger.py`, then click the URL, and afer `cloudshell.dev/` add `apidocs`, as you can see in the screenshot in the screenshots folder. Click the `GET` button and the parameters, response code and descriptions will appear (also can be seen in the screenshots in the screenshots folder).
## Challenges Encounntered
- The first issue I encountered was running the `func init LocalFunctionProj --python -m V2` command. I followed the tutorial but i did not realize in the terminal, I was not in any directory. When I was up to the "create and acticate a virtual environment" section of the tutorial I followed it and it led me to using .venv, I then ran the `func init` command like that and it created all my files into my root directory. Then i had to use the command `mv <file name> flask_6_api_management` to retrieve every file and move it into the rigt directory. I then deleted all the files I moved to ensure no great mistakes were made due to the mass movement of files or if something had not moved properly. After that, I went into the right directory by utilizing the command `cd` and then ran the `func init` again, and all the files were produced in the right place.
- Everything else worked smoothly, except for when I reached deployment. I successfully recieved all the comments in the terminal that my app sucessfully deployed, however when I clicked the link from the terminal, this came up: ![image](https://github.com/amnasyed1/flask_6_api_management/assets/123895397/8bbd76af-85df-44e7-8084-b89bcb606c57)
I then went to the Azure website and went into `App Services` clicked on my the app name to check if everything was correct and running properly. I clicked the URL link provided and this appeared: ![image](https://github.com/amnasyed1/flask_6_api_management/assets/123895397/d41c9c4f-a67b-4674-a658-2251b2c07bff)
After that I scrolled down to the `Functions` and clicked `HTTPExample` which brought me to this: ![image](https://github.com/amnasyed1/flask_6_api_management/assets/123895397/294031b7-ee29-4e5b-9e31-ba02b9a251fe)
I then clicked `Get URL function`, copied the default(functionkey)url and pasted it to a  new tab and it worked! ![image](https://github.com/amnasyed1/flask_6_api_management/assets/123895397/928a51d9-9c4c-4c3b-8a27-c612eb8894a0)


