# Event

Representation of a trackable event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **Dict[str, str]** | Body of the event to track the details of the tracking event as Key value pair | [optional] 
**key** | **str** | Key of the event to be tracked. This key should start with an uppercase letter followed by alphanumeric characters or underscores. The entire key needs to be smaller than 64 characters. | [optional] 

## Example

```python
from ocm_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


