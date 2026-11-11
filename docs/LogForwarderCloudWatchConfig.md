# LogForwarderCloudWatchConfig

CloudWatch configuration for log forwarding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_distribution_role_arn** | **str** | The ARN of the IAM role for log distribution. | [optional] 
**log_group_name** | **str** | The name of the CloudWatch log group. | [optional] 

## Example

```python
from ocm_client.models.log_forwarder_cloud_watch_config import LogForwarderCloudWatchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarderCloudWatchConfig from a JSON string
log_forwarder_cloud_watch_config_instance = LogForwarderCloudWatchConfig.from_json(json)
# print the JSON string representation of the object
print(LogForwarderCloudWatchConfig.to_json())

# convert the object into a dict
log_forwarder_cloud_watch_config_dict = log_forwarder_cloud_watch_config_instance.to_dict()
# create an instance of LogForwarderCloudWatchConfig from a dict
log_forwarder_cloud_watch_config_from_dict = LogForwarderCloudWatchConfig.from_dict(log_forwarder_cloud_watch_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


