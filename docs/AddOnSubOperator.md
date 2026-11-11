# AddOnSubOperator

Representation of an add-on sub operator. A sub operator is an operator who's life cycle is controlled by the add-on umbrella operator. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if the sub operator is enabled for the add-on | [optional] 
**operator_name** | **str** | Name of the add-on sub operator | [optional] 
**operator_namespace** | **str** | Namespace of the add-on sub operator | [optional] 

## Example

```python
from ocm_client.models.add_on_sub_operator import AddOnSubOperator

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnSubOperator from a JSON string
add_on_sub_operator_instance = AddOnSubOperator.from_json(json)
# print the JSON string representation of the object
print(AddOnSubOperator.to_json())

# convert the object into a dict
add_on_sub_operator_dict = add_on_sub_operator_instance.to_dict()
# create an instance of AddOnSubOperator from a dict
add_on_sub_operator_from_dict = AddOnSubOperator.from_dict(add_on_sub_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


