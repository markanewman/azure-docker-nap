targetScope = 'resourceGroup'

module container_registry 'container_registry.bicep' = {
  name: '${deployment().name}-container_registry'
  params: {}
}
