# ManagedService

Contains the necessary attributes to support role-based authentication on AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the cluster belongs to a managed service This should only be set by the \&quot;Managed Service\&quot; service. clusters with this set can only be modified by the \&quot;Managed Service\&quot; service. | [optional] 

## Example

```python
from ocm_client.models.managed_service import ManagedService

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedService from a JSON string
managed_service_instance = ManagedService.from_json(json)
# print the JSON string representation of the object
print(ManagedService.to_json())

# convert the object into a dict
managed_service_dict = managed_service_instance.to_dict()
# create an instance of ManagedService from a dict
managed_service_from_dict = ManagedService.from_dict(managed_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


