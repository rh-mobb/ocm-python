# AddOnNamespace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddOnNamespace&#39; if this is a complete object or &#39;AddOnNamespaceLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**annotations** | **Dict[str, str]** | Annotations to be applied to this namespace. | [optional] 
**labels** | **Dict[str, str]** | Labels to be applied to this namespace. | [optional] 
**name** | **str** | Name of the namespace. | [optional] 

## Example

```python
from ocm_client.models.add_on_namespace import AddOnNamespace

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnNamespace from a JSON string
add_on_namespace_instance = AddOnNamespace.from_json(json)
# print the JSON string representation of the object
print(AddOnNamespace.to_json())

# convert the object into a dict
add_on_namespace_dict = add_on_namespace_instance.to_dict()
# create an instance of AddOnNamespace from a dict
add_on_namespace_from_dict = AddOnNamespace.from_dict(add_on_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


