# AwsEtcdEncryption

Contains the necessary attributes to support etcd encryption for AWS based clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_arn** | **str** | ARN of the KMS to be used for the etcd encryption | [optional] 

## Example

```python
from ocm_client.models.aws_etcd_encryption import AwsEtcdEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of AwsEtcdEncryption from a JSON string
aws_etcd_encryption_instance = AwsEtcdEncryption.from_json(json)
# print the JSON string representation of the object
print(AwsEtcdEncryption.to_json())

# convert the object into a dict
aws_etcd_encryption_dict = aws_etcd_encryption_instance.to_dict()
# create an instance of AwsEtcdEncryption from a dict
aws_etcd_encryption_from_dict = AwsEtcdEncryption.from_dict(aws_etcd_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


