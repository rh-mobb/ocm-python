# AddOnParameterOption

Representation of an add-on parameter option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the add-on parameter option. | [optional] 
**rank** | **int** | Rank of option to be used in cases where editable direction should be restricted. | [optional] 
**requirements** | [**List[AddOnRequirement]**](AddOnRequirement.md) | List of add-on requirements for this parameter option. | [optional] 
**value** | **str** | Value of the add-on parameter option. | [optional] 

## Example

```python
from ocm_client.models.add_on_parameter_option import AddOnParameterOption

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnParameterOption from a JSON string
add_on_parameter_option_instance = AddOnParameterOption.from_json(json)
# print the JSON string representation of the object
print(AddOnParameterOption.to_json())

# convert the object into a dict
add_on_parameter_option_dict = add_on_parameter_option_instance.to_dict()
# create an instance of AddOnParameterOption from a dict
add_on_parameter_option_from_dict = AddOnParameterOption.from_dict(add_on_parameter_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


