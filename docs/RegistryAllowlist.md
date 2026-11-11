# RegistryAllowlist

RegistryAllowlist represents a single registry allowlist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;RegistryAllowlist&#39; if this is a complete object or &#39;RegistryAllowlistLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cloud_provider** | [**CloudProvider**](CloudProvider.md) |  | [optional] 
**creation_timestamp** | **datetime** | CreationTimestamp is the date and time when the allow list has been created. | [optional] 
**registries** | **List[str]** | Registries is the list of registries contained in this Allowlist. | [optional] 

## Example

```python
from ocm_client.models.registry_allowlist import RegistryAllowlist

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryAllowlist from a JSON string
registry_allowlist_instance = RegistryAllowlist.from_json(json)
# print the JSON string representation of the object
print(RegistryAllowlist.to_json())

# convert the object into a dict
registry_allowlist_dict = registry_allowlist_instance.to_dict()
# create an instance of RegistryAllowlist from a dict
registry_allowlist_from_dict = RegistryAllowlist.from_dict(registry_allowlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


