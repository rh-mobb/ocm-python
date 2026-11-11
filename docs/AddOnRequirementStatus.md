# AddOnRequirementStatus

Representation of an add-on requirement status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_msgs** | **List[str]** | Error messages detailing reasons for unfulfilled requirements. | [optional] 
**fulfilled** | **bool** | Indicates if this requirement is fulfilled. | [optional] 

## Example

```python
from ocm_client.models.add_on_requirement_status import AddOnRequirementStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnRequirementStatus from a JSON string
add_on_requirement_status_instance = AddOnRequirementStatus.from_json(json)
# print the JSON string representation of the object
print(AddOnRequirementStatus.to_json())

# convert the object into a dict
add_on_requirement_status_dict = add_on_requirement_status_instance.to_dict()
# create an instance of AddOnRequirementStatus from a dict
add_on_requirement_status_from_dict = AddOnRequirementStatus.from_dict(add_on_requirement_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


