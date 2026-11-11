# LogForwarderStatus

Represents the status of a log forwarder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A descriptive message providing additional context about the current state of the log forwarder. | [optional] 
**resolved_applications** | **List[str]** | The list of applications that are resolved for log forwarding, including the explicitly specified applications and any default applications. | [optional] 
**state** | **str** | The current state of the log forwarder. | [optional] 

## Example

```python
from ocm_client.models.log_forwarder_status import LogForwarderStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarderStatus from a JSON string
log_forwarder_status_instance = LogForwarderStatus.from_json(json)
# print the JSON string representation of the object
print(LogForwarderStatus.to_json())

# convert the object into a dict
log_forwarder_status_dict = log_forwarder_status_instance.to_dict()
# create an instance of LogForwarderStatus from a dict
log_forwarder_status_from_dict = LogForwarderStatus.from_dict(log_forwarder_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


