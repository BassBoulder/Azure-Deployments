targetScope = 'subscription'

param location string = 'uksouth'

// Create Resource Group
resource rg 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-uks-lake-001'
  managedBy: 'mg-uks-lake'
  location: location
}
