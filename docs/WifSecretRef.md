# WifSecretRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.wif_secret_ref import WifSecretRef

# TODO update the JSON string below
json = "{}"
# create an instance of WifSecretRef from a JSON string
wif_secret_ref_instance = WifSecretRef.from_json(json)
# print the JSON string representation of the object
print(WifSecretRef.to_json())

# convert the object into a dict
wif_secret_ref_dict = wif_secret_ref_instance.to_dict()
# create an instance of WifSecretRef from a dict
wif_secret_ref_from_dict = WifSecretRef.from_dict(wif_secret_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


