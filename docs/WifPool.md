# WifPool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_provider** | [**WifIdentityProvider**](WifIdentityProvider.md) |  | [optional] 
**pool_id** | **str** | The Id of the workload identity pool. | [optional] 
**pool_name** | **str** | The display name of the workload identity pool. | [optional] 

## Example

```python
from ocm_client.models.wif_pool import WifPool

# TODO update the JSON string below
json = "{}"
# create an instance of WifPool from a JSON string
wif_pool_instance = WifPool.from_json(json)
# print the JSON string representation of the object
print(WifPool.to_json())

# convert the object into a dict
wif_pool_dict = wif_pool_instance.to_dict()
# create an instance of WifPool from a dict
wif_pool_from_dict = WifPool.from_dict(wif_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


