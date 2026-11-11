# LogForwarderGroupVersions

Represents a log forwarder group versions configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether this group is available for use for log forwarding. | [optional] 
**name** | **str** | The name of the log forwarder group. | [optional] 
**versions** | [**List[LogForwarderGroupVersion]**](LogForwarderGroupVersion.md) | List of available versions for this group. | [optional] 

## Example

```python
from ocm_client.models.log_forwarder_group_versions import LogForwarderGroupVersions

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarderGroupVersions from a JSON string
log_forwarder_group_versions_instance = LogForwarderGroupVersions.from_json(json)
# print the JSON string representation of the object
print(LogForwarderGroupVersions.to_json())

# convert the object into a dict
log_forwarder_group_versions_dict = log_forwarder_group_versions_instance.to_dict()
# create an instance of LogForwarderGroupVersions from a dict
log_forwarder_group_versions_from_dict = LogForwarderGroupVersions.from_dict(log_forwarder_group_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


