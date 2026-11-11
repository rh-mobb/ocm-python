# NamespaceSelector

Representation of a NamespaceSelector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key value | [optional] 
**values** | **List[str]** | One or more values associated to the Key | [optional] 

## Example

```python
from ocm_client.models.namespace_selector import NamespaceSelector

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceSelector from a JSON string
namespace_selector_instance = NamespaceSelector.from_json(json)
# print the JSON string representation of the object
print(NamespaceSelector.to_json())

# convert the object into a dict
namespace_selector_dict = namespace_selector_instance.to_dict()
# create an instance of NamespaceSelector from a dict
namespace_selector_from_dict = NamespaceSelector.from_dict(namespace_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


