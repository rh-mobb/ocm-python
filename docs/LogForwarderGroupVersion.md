# LogForwarderGroupVersion

Represents a version of a log forwarder group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The version identifier. | [optional] 
**applications** | **List[str]** | List of applications included in this version of the group. | [optional] 

## Example

```python
from ocm_client.models.log_forwarder_group_version import LogForwarderGroupVersion

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarderGroupVersion from a JSON string
log_forwarder_group_version_instance = LogForwarderGroupVersion.from_json(json)
# print the JSON string representation of the object
print(LogForwarderGroupVersion.to_json())

# convert the object into a dict
log_forwarder_group_version_dict = log_forwarder_group_version_instance.to_dict()
# create an instance of LogForwarderGroupVersion from a dict
log_forwarder_group_version_from_dict = LogForwarderGroupVersion.from_dict(log_forwarder_group_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


