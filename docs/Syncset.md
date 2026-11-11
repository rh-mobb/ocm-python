# Syncset

Representation of a syncset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;Syncset&#39; if this is a complete object or &#39;SyncsetLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**resources** | **List[object]** | List of k8s objects to configure for the cluster. | [optional] 

## Example

```python
from ocm_client.models.syncset import Syncset

# TODO update the JSON string below
json = "{}"
# create an instance of Syncset from a JSON string
syncset_instance = Syncset.from_json(json)
# print the JSON string representation of the object
print(Syncset.to_json())

# convert the object into a dict
syncset_dict = syncset_instance.to_dict()
# create an instance of Syncset from a dict
syncset_from_dict = Syncset.from_dict(syncset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


