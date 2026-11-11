# KeyRing

Description of a cloud provider key ring.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;KeyRing&#39; if this is a complete object or &#39;KeyRingLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**name** | **str** | Name of the key ring. | [optional] 

## Example

```python
from ocm_client.models.key_ring import KeyRing

# TODO update the JSON string below
json = "{}"
# create an instance of KeyRing from a JSON string
key_ring_instance = KeyRing.from_json(json)
# print the JSON string representation of the object
print(KeyRing.to_json())

# convert the object into a dict
key_ring_dict = key_ring_instance.to_dict()
# create an instance of KeyRing from a dict
key_ring_from_dict = KeyRing.from_dict(key_ring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


