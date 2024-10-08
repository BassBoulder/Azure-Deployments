
targetScope = 'managementGroup'

resource subscriptionAlias 'Microsoft.Subscription/aliases@2021-10-01' = {
  scope: tenant()
  name: 'uks-lake-001'
  properties: {
    displayName: 'uks-lake-001'
    billingScope: '<BillingScopeId>'
    workload: 'DevTest'
  }
}
