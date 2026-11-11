# LogForwarderApplication

Represents an application that can be configured for log forwarding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether this application is available for use for log forwarding. | [optional] 
**name** | **str** | The name of the application. | [optional] 

## Example

```python
from ocm_client.models.log_forwarder_application import LogForwarderApplication

# TODO update the JSON string below
json = "{}"
# create an instance of LogForwarderApplication from a JSON string
log_forwarder_application_instance = LogForwarderApplication.from_json(json)
# print the JSON string representation of the object
print(LogForwarderApplication.to_json())

# convert the object into a dict
log_forwarder_application_dict = log_forwarder_application_instance.to_dict()
# create an instance of LogForwarderApplication from a dict
log_forwarder_application_from_dict = LogForwarderApplication.from_dict(log_forwarder_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


