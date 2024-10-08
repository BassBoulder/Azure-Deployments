
targetScope = 'tenant'

//Create Management Group
resource mg 'Microsoft.Management/managementGroups@2023-04-01' = {
  name: 'mg-uks-lake'
}
