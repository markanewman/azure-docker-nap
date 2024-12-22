Test docker project: read >> nap >> write

# VS Code

I use DevContainers to allow a consistent development experience and to keep my desktop clean.

1. Navigate to the project folder's parent
2. Open the project in VS Code
   * Right click > context menu > Open withCode
3. Setup environment variables in `~/.docker/.env`
   ```
   DATA_VOLUME=c:/data/personal
   ```
4. Switch to _dev containers_
   * F1 > Dev Containers: Rebuild and Reopen in Containers
   * Scaffolding file: `~/.devcontainer/devcontainer.json`
5. Start the debugger
   * `F5`
   * Scaffolding file: `~/.vscode/launch.json`
   * The debugging session is happening inside the dev container

# Local deploy

Testing in VS code is necessary, but not sufficient.
Make _sure_ you _are NOT_ running in DevContainers (F1 > Dev Containers: Reopen Folder Locally).
It will overwrite the attached container and cause VS Code to freak out.

1. Open up PowerShell
   * `ctrl + shft + ~`
2. Validate _# VS Code_ step _Setup environment variables in `~/.docker/.env`_ was run
3. Create the service.
   Use `create` > `start` vs `up` so that the project will not shutdown when you exit the PowerShell window.
   ```{ps1}
   docker build -f .docker/Dockerfile -t azure_docker_nap:latest .
   docker-compose -f .docker/docker-compose.yml create
   docker-compose -f .docker/docker-compose.yml start
   ```

# Azure deploy

I use Bicep to deploy IoC.
Make _sure_ you _ARE_ running in DevContainers.
All the tools are already added.

1. Open up a VS Code terminal
   * `ctrl + shft + ~`
2. Login to Azure
   ```{bash}
   az login
   ```
3. Create the resource group and add in all the shared resources
   ```{bash}
   resource_group=HappyFunTime
   az group create -l eastus2 -n $resource_group
   az deployment group create --resource-group $resource_group --template-file .azure_env/main.bicep
   ```
4. Push the image to the Azure repository.
   ```{bash}
   acr_name=$(az acr list --resource-group $resource_group --query [0].name | cut -d'"' -f 2)
   az acr build --registry $acr_name -f .docker/Dockerfile -t azure_docker_nap:latest .
   ```