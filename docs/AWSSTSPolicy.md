# AWSSTSPolicy

Representation of an sts policies for rosa cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | The ARN of the managed policy | [optional] 
**id** | **str** | Policy ID | [optional] 
**details** | **str** | Policy Details | [optional] 
**type** | **str** | Type of policy operator/account role | [optional] 

## Example

```python
from ocm_client.models.awssts_policy import AWSSTSPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AWSSTSPolicy from a JSON string
awssts_policy_instance = AWSSTSPolicy.from_json(json)
# print the JSON string representation of the object
print(AWSSTSPolicy.to_json())

# convert the object into a dict
awssts_policy_dict = awssts_policy_instance.to_dict()
# create an instance of AWSSTSPolicy from a dict
awssts_policy_from_dict = AWSSTSPolicy.from_dict(awssts_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


