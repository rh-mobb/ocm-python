# AlertInfo

Provides information about a single alert firing on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The alert name. Multiple alerts with same name are possible. | [optional] 
**severity** | [**AlertSeverity**](AlertSeverity.md) |  | [optional] 

## Example

```python
from ocm_client.models.alert_info import AlertInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlertInfo from a JSON string
alert_info_instance = AlertInfo.from_json(json)
# print the JSON string representation of the object
print(AlertInfo.to_json())

# convert the object into a dict
alert_info_dict = alert_info_instance.to_dict()
# create an instance of AlertInfo from a dict
alert_info_from_dict = AlertInfo.from_dict(alert_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


