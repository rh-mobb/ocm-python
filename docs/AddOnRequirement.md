# AddOnRequirement

Representation of an add-on requirement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the add-on requirement. | [optional] 
**data** | **Dict[str, object]** | Data for the add-on requirement. | [optional] 
**enabled** | **bool** | Indicates if this requirement is enabled for the add-on. | [optional] 
**resource** | **str** | Type of resource of the add-on requirement. | [optional] 
**status** | [**AddOnRequirementStatus**](AddOnRequirementStatus.md) |  | [optional] 

## Example

```python
from ocm_client.models.add_on_requirement import AddOnRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnRequirement from a JSON string
add_on_requirement_instance = AddOnRequirement.from_json(json)
# print the JSON string representation of the object
print(AddOnRequirement.to_json())

# convert the object into a dict
add_on_requirement_dict = add_on_requirement_instance.to_dict()
# create an instance of AddOnRequirement from a dict
add_on_requirement_from_dict = AddOnRequirement.from_dict(add_on_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


