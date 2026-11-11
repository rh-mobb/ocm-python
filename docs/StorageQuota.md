# StorageQuota

Representation of a storage quota 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Unit of storage | [optional] 
**value** | **float** | Numerical value | [optional] 

## Example

```python
from ocm_client.models.storage_quota import StorageQuota

# TODO update the JSON string below
json = "{}"
# create an instance of StorageQuota from a JSON string
storage_quota_instance = StorageQuota.from_json(json)
# print the JSON string representation of the object
print(StorageQuota.to_json())

# convert the object into a dict
storage_quota_dict = storage_quota_instance.to_dict()
# create an instance of StorageQuota from a dict
storage_quota_from_dict = StorageQuota.from_dict(storage_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


