# AwsAutoNode

AWS provider configuration settings when using AutoNode on a ROSA HCP Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_arn** | **str** | The AWS ARN of the IAM Role that has the permissions required for the AutoNode controller. The role must exist prior to enabling AutoNode on the cluster. | [optional] 

## Example

```python
from ocm_client.models.aws_auto_node import AwsAutoNode

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAutoNode from a JSON string
aws_auto_node_instance = AwsAutoNode.from_json(json)
# print the JSON string representation of the object
print(AwsAutoNode.to_json())

# convert the object into a dict
aws_auto_node_dict = aws_auto_node_instance.to_dict()
# create an instance of AwsAutoNode from a dict
aws_auto_node_from_dict = AwsAutoNode.from_dict(aws_auto_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


