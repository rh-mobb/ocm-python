# AddOnInstallationParameter

Representation of an add-on installation parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddOnInstallationParameter&#39; if this is a complete object or &#39;AddOnInstallationParameterLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**value** | **str** | Value of the parameter. | [optional] 

## Example

```python
from ocm_client.models.add_on_installation_parameter import AddOnInstallationParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnInstallationParameter from a JSON string
add_on_installation_parameter_instance = AddOnInstallationParameter.from_json(json)
# print the JSON string representation of the object
print(AddOnInstallationParameter.to_json())

# convert the object into a dict
add_on_installation_parameter_dict = add_on_installation_parameter_instance.to_dict()
# create an instance of AddOnInstallationParameter from a dict
add_on_installation_parameter_from_dict = AddOnInstallationParameter.from_dict(add_on_installation_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


