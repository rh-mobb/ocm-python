# AWSBackupConfig

Backup configuration for AWS clusters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_bucket** | **str** | Name of the S3 bucket used to save the backup | [optional] 
**access_shared_role_arn** | **str** | ARN of the role used in the Disaster Recovery (DR) account to manipulate backups for deleted clusters | [optional] 
**account_id** | **str** | ID of the AWS Disaster Recovery (DR) account | [optional] 
**identity_provider_arn** | **str** | ARN of the identity provider created in the Disaster Recovery (DR) account for the Management Cluster | [optional] 
**management_cluster** | **str** | Name of the management cluster the backup config refers to | [optional] 
**role_arn** | **str** | ARN of the role used by the CS Trusted Account to gain access to the Disaster Recovery (DR) account | [optional] 

## Example

```python
from ocm_client.models.aws_backup_config import AWSBackupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AWSBackupConfig from a JSON string
aws_backup_config_instance = AWSBackupConfig.from_json(json)
# print the JSON string representation of the object
print(AWSBackupConfig.to_json())

# convert the object into a dict
aws_backup_config_dict = aws_backup_config_instance.to_dict()
# create an instance of AWSBackupConfig from a dict
aws_backup_config_from_dict = AWSBackupConfig.from_dict(aws_backup_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


