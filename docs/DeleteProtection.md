# DeleteProtection

DeleteProtection configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Boolean flag indicating if the cluster should be be using _DeleteProtection_.  By default this is &#x60;false&#x60;.  To enable it a SREP needs to patch the value through OCM API | [optional] 

## Example

```python
from ocm_client.models.delete_protection import DeleteProtection

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProtection from a JSON string
delete_protection_instance = DeleteProtection.from_json(json)
# print the JSON string representation of the object
print(DeleteProtection.to_json())

# convert the object into a dict
delete_protection_dict = delete_protection_instance.to_dict()
# create an instance of DeleteProtection from a dict
delete_protection_from_dict = DeleteProtection.from_dict(delete_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


