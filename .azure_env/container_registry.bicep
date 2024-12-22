targetScope = 'resourceGroup'

param name string = uniqueString(resourceGroup().id)
param location string = resourceGroup().location
param sku string = 'Basic'

resource registry 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: name
  location: location
  sku: {
    name: sku
  }
  properties: {
    adminUserEnabled: true
  }
}
