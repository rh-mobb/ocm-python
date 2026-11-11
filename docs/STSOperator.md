# STSOperator

Representation of an sts operator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_version** | **str** | Maximum ocp version supported | [optional] 
**min_version** | **str** | Minimum ocp version supported | [optional] 
**name** | **str** | Operator Name | [optional] 
**namespace** | **str** | Operator Namespace | [optional] 
**service_accounts** | **List[str]** | Service Accounts | [optional] 

## Example

```python
from ocm_client.models.sts_operator import STSOperator

# TODO update the JSON string below
json = "{}"
# create an instance of STSOperator from a JSON string
sts_operator_instance = STSOperator.from_json(json)
# print the JSON string representation of the object
print(STSOperator.to_json())

# convert the object into a dict
sts_operator_dict = sts_operator_instance.to_dict()
# create an instance of STSOperator from a dict
sts_operator_from_dict = STSOperator.from_dict(sts_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


