# AzureControlPlaneManagedIdentity

Represents the information associated to an Azure User-Assigned Managed Identity belonging to the Control Plane of the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The Client ID associated to the Azure User-Assigned Managed Identity. Readonly. | [optional] 
**principal_id** | **str** | The Principal ID associated to the Azure User-Assigned Identity. Readonly. | [optional] 
**resource_id** | **str** | The Azure Resource ID of the Azure User-Assigned Managed Identity. The managed identity represented must exist before creating the cluster. The Azure Resource Group Name specified as part of the Resource ID must belong to the Azure Subscription specified in &#x60;.azure.subscription_id&#x60;, and in the same Azure location as the cluster&#39;s region. The Azure Resource Group Name specified as part of the Resource ID must be a different Resource Group Name than the one specified in &#x60;.azure.managed_resource_group_name&#x60;. The Azure Resource Group Name specified as part of the Resource ID can be the same, or a different one than the one specified in &#x60;.azure.resource_group_name&#x60;. Required during creation. Immutable. | [optional] 

## Example

```python
from ocm_client.models.azure_control_plane_managed_identity import AzureControlPlaneManagedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AzureControlPlaneManagedIdentity from a JSON string
azure_control_plane_managed_identity_instance = AzureControlPlaneManagedIdentity.from_json(json)
# print the JSON string representation of the object
print(AzureControlPlaneManagedIdentity.to_json())

# convert the object into a dict
azure_control_plane_managed_identity_dict = azure_control_plane_managed_identity_instance.to_dict()
# create an instance of AzureControlPlaneManagedIdentity from a dict
azure_control_plane_managed_identity_from_dict = AzureControlPlaneManagedIdentity.from_dict(azure_control_plane_managed_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


