# OperatorIAMRole

Contains the necessary attributes to allow each operator to access the necessary AWS resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Randomly-generated ID to identify the operator role | [optional] 
**name** | **str** | Name of the credentials secret used to access cloud resources | [optional] 
**namespace** | **str** | Namespace where the credentials secret lives in the cluster | [optional] 
**role_arn** | **str** | Role to assume when accessing AWS resources | [optional] 
**service_account** | **str** | Service account name to use when authenticating | [optional] 

## Example

```python
from ocm_client.models.operator_iam_role import OperatorIAMRole

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorIAMRole from a JSON string
operator_iam_role_instance = OperatorIAMRole.from_json(json)
# print the JSON string representation of the object
print(OperatorIAMRole.to_json())

# convert the object into a dict
operator_iam_role_dict = operator_iam_role_instance.to_dict()
# create an instance of OperatorIAMRole from a dict
operator_iam_role_from_dict = OperatorIAMRole.from_dict(operator_iam_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


