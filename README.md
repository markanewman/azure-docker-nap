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
Make _sure_ you are _NOT_ running in DevContainers (F1 > Dev Containers: Reopen Folder Locally).
It will overwrite the attached container and cause VS Code to freak out.

1. Open up PowerShell
   * `crtl + shft + ~`
2. Validate _# VS Code_ step _Setup environment variables in `~/.docker/.env`_ was run
3. Create the service.
   Use `create` > `start` vs `up` so that the project will not shutdown when you exit the PowerShell window.
   ```{ps1}
   docker build -f .docker/Dockerfile -t azure_docker_nap:latest .
   docker-compose -f .docker/docker-compose.yml create
   docker-compose -f .docker/docker-compose.yml start
   ```
