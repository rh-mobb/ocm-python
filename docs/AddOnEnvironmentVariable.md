# AddOnEnvironmentVariable

Representation of an add-on env object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddOnEnvironmentVariable&#39; if this is a complete object or &#39;AddOnEnvironmentVariableLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**name** | **str** | Name of the env object. | [optional] 
**value** | **str** | Value of the env object. | [optional] 

## Example

```python
from ocm_client.models.add_on_environment_variable import AddOnEnvironmentVariable

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnEnvironmentVariable from a JSON string
add_on_environment_variable_instance = AddOnEnvironmentVariable.from_json(json)
# print the JSON string representation of the object
print(AddOnEnvironmentVariable.to_json())

# convert the object into a dict
add_on_environment_variable_dict = add_on_environment_variable_instance.to_dict()
# create an instance of AddOnEnvironmentVariable from a dict
add_on_environment_variable_from_dict = AddOnEnvironmentVariable.from_dict(add_on_environment_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


