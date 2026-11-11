# LogForwarder

Representation of a log forwarder configuration for a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;LogForwarder&#39; if this is a complete object or &#39;LogForwarderLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**s3** | [**LogForwarderS3Config**](LogForwarderS3Config.md) |  | [optional] 
**applications** | **List[str]** | List of additional applications to forward logs for. | [optional] 
**cloudwatch** | [**LogForwarderCloudWatchConfig**](LogForwarderCloudWatchConfig.md) |  | [optional] 
**cluster_id** | **str** | Identifier of the cluster. | [optional] 
**groups** | [**List[LogForwarderGroup]**](LogForwarderGroup.md) | List of log forwarder groups. | [optional] 
**status** | [**LogForwarderStatus**](LogForwarderStatus.md) |  | [optional] 

## Example

```python
from ocm_client.models.log_forwarder import LogForwarder

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarder from a JSON string
log_forwarder_instance = LogForwarder.from_json(json)
# print the JSON string representation of the object
print(LogForwarder.to_json())

# convert the object into a dict
log_forwarder_dict = log_forwarder_instance.to_dict()
# create an instance of LogForwarder from a dict
log_forwarder_from_dict = LogForwarder.from_dict(log_forwarder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


