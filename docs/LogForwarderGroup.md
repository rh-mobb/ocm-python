# LogForwarderGroup

Represents a log forwarder group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the log forwarder group. | [optional] 
**version** | **str** | The version of the log forwarder group. | [optional] 

## Example

```python
from ocm_client.models.log_forwarder_group import LogForwarderGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarderGroup from a JSON string
log_forwarder_group_instance = LogForwarderGroup.from_json(json)
# print the JSON string representation of the object
print(LogForwarderGroup.to_json())

# convert the object into a dict
log_forwarder_group_dict = log_forwarder_group_instance.to_dict()
# create an instance of LogForwarderGroup from a dict
log_forwarder_group_from_dict = LogForwarderGroup.from_dict(log_forwarder_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


