# AzureOperatorsAuthenticationManagedIdentities

Represents the information related to Azure User-Assigned managed identities needed to perform Operators authentication based on Azure User-Assigned Managed Identities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane_operators_managed_identities** | [**Dict[str, AzureControlPlaneManagedIdentity]**](AzureControlPlaneManagedIdentity.md) | The set of Azure User-Assigned Managed Identities leveraged for the Control Plane operators of the cluster. The set of required managed identities is dependent on the Cluster&#39;s OpenShift version. Immutable | [optional] 
**data_plane_operators_managed_identities** | [**Dict[str, AzureDataPlaneManagedIdentity]**](AzureDataPlaneManagedIdentity.md) | The set of Azure User-Assigned Managed Identities leveraged for the Data Plane operators of the cluster. The set of required managed identities is dependent on the Cluster&#39;s OpenShift version. Immutable. | [optional] 
**managed_identities_data_plane_identity_url** | **str** | The Managed Identities Data Plane Identity URL associated with the cluster. It is the URL that will be used to communicate with the Managed Identities Resource Provider (MI RP). Required during creation. Immutable. | [optional] 
**service_managed_identity** | [**AzureServiceManagedIdentity**](AzureServiceManagedIdentity.md) |  | [optional] 

## Example

```python
from ocm_client.models.azure_operators_authentication_managed_identities import AzureOperatorsAuthenticationManagedIdentities

# TODO update the JSON string below
json = "{}"
# create an instance of AzureOperatorsAuthenticationManagedIdentities from a JSON string
azure_operators_authentication_managed_identities_instance = AzureOperatorsAuthenticationManagedIdentities.from_json(json)
# print the JSON string representation of the object
print(AzureOperatorsAuthenticationManagedIdentities.to_json())

# convert the object into a dict
azure_operators_authentication_managed_identities_dict = azure_operators_authentication_managed_identities_instance.to_dict()
# create an instance of AzureOperatorsAuthenticationManagedIdentities from a dict
azure_operators_authentication_managed_identities_from_dict = AzureOperatorsAuthenticationManagedIdentities.from_dict(azure_operators_authentication_managed_identities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


