# AWSShard

Config for AWS provision shards

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecr_repository_urls** | **List[str]** | ECR repository URLs of the provision shard | [optional] 
**backup_configs** | [**List[AWSBackupConfig]**](AWSBackupConfig.md) | Backup configurations for the provision shard | [optional] 

## Example

```python
from ocm_client.models.aws_shard import AWSShard

# TODO update the JSON string below
json = "{}"
# create an instance of AWSShard from a JSON string
aws_shard_instance = AWSShard.from_json(json)
# print the JSON string representation of the object
print(AWSShard.to_json())

# convert the object into a dict
aws_shard_dict = aws_shard_instance.to_dict()
# create an instance of AWSShard from a dict
aws_shard_from_dict = AWSShard.from_dict(aws_shard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


