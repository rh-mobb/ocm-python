# WifResourceBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.wif_resource_binding import WifResourceBinding

# TODO update the JSON string below
json = "{}"
# create an instance of WifResourceBinding from a JSON string
wif_resource_binding_instance = WifResourceBinding.from_json(json)
# print the JSON string representation of the object
print(WifResourceBinding.to_json())

# convert the object into a dict
wif_resource_binding_dict = wif_resource_binding_instance.to_dict()
# create an instance of WifResourceBinding from a dict
wif_resource_binding_from_dict = WifResourceBinding.from_dict(wif_resource_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


