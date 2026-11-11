# LogForwarderS3Config

S3 configuration for log forwarding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The name of the S3 bucket. | [optional] 
**bucket_prefix** | **str** | The prefix to use for objects stored in the S3 bucket. | [optional] 

## Example

```python
from ocm_client.models.log_forwarder_s3_config import LogForwarderS3Config

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarderS3Config from a JSON string
log_forwarder_s3_config_instance = LogForwarderS3Config.from_json(json)
# print the JSON string representation of the object
print(LogForwarderS3Config.to_json())

# convert the object into a dict
log_forwarder_s3_config_dict = log_forwarder_s3_config_instance.to_dict()
# create an instance of LogForwarderS3Config from a dict
log_forwarder_s3_config_from_dict = LogForwarderS3Config.from_dict(log_forwarder_s3_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


