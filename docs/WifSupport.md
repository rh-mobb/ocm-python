# WifSupport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal** | **str** |  | [optional] 
**roles** | [**List[WifRole]**](WifRole.md) |  | [optional] 

## Example

```python
from ocm_client.models.wif_support import WifSupport

# TODO update the JSON string below
json = "{}"
# create an instance of WifSupport from a JSON string
wif_support_instance = WifSupport.from_json(json)
# print the JSON string representation of the object
print(WifSupport.to_json())

# convert the object into a dict
wif_support_dict = wif_support_instance.to_dict()
# create an instance of WifSupport from a dict
wif_support_from_dict = WifSupport.from_dict(wif_support_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


