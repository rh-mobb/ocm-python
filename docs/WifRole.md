# WifRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | [optional] 
**predefined** | **bool** |  | [optional] 
**resource_bindings** | [**List[WifResourceBinding]**](WifResourceBinding.md) |  | [optional] 
**role_id** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.wif_role import WifRole

# TODO update the JSON string below
json = "{}"
# create an instance of WifRole from a JSON string
wif_role_instance = WifRole.from_json(json)
# print the JSON string representation of the object
print(WifRole.to_json())

# convert the object into a dict
wif_role_dict = wif_role_instance.to_dict()
# create an instance of WifRole from a dict
wif_role_from_dict = WifRole.from_dict(wif_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


