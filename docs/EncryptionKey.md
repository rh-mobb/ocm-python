# EncryptionKey

Description of a cloud provider encryption key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;EncryptionKey&#39; if this is a complete object or &#39;EncryptionKeyLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**name** | **str** | Name of the encryption key. | [optional] 

## Example

```python
from ocm_client.models.encryption_key import EncryptionKey

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKey from a JSON string
encryption_key_instance = EncryptionKey.from_json(json)
# print the JSON string representation of the object
print(EncryptionKey.to_json())

# convert the object into a dict
encryption_key_dict = encryption_key_instance.to_dict()
# create an instance of EncryptionKey from a dict
encryption_key_from_dict = EncryptionKey.from_dict(encryption_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


