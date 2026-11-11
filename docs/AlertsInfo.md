# AlertsInfo

Provides information about the alerts firing on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[AlertInfo]**](AlertInfo.md) |  | [optional] 

## Example

```python
from ocm_client.models.alerts_info import AlertsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsInfo from a JSON string
alerts_info_instance = AlertsInfo.from_json(json)
# print the JSON string representation of the object
print(AlertsInfo.to_json())

# convert the object into a dict
alerts_info_dict = alerts_info_instance.to_dict()
# create an instance of AlertsInfo from a dict
alerts_info_from_dict = AlertsInfo.from_dict(alerts_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


