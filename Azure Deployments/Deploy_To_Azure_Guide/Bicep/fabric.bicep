param name string = 'fabukslake'
param location string = resourceGroup().location

@allowed([
  'F2'
  'F4'
  'F8'
  'F16'
])
param skuName string = 'F2'
param skuTier string = 'Fabric'
@description('admin format: something@domain.com')
param admin array = ['viktorija.hajduk@healthnethc.onmicrosoft.com','nick.elgar@healthnethc.onmicrosoft.com']
param tagValues object = {}

 
 
resource fabricCapacities 'Microsoft.Fabric/capacities@2022-07-01-preview' = {
  name: toLower(name)
  location: location
  tags: tagValues
  sku: {
    name: skuName
    tier: skuTier
  }
  properties: {
    administration: {
      members: admin
    }
  }
}
 
output resourceId string = fabricCapacities.id
output resourceName string = fabricCapacities.name
