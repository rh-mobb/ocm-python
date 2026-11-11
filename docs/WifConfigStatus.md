# WifConfigStatus

Configuration status of a WifConfig.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured** | **bool** | Indicates the current status of the WifConfig resource configuration. - &#x60;false&#x60;: The WifConfig resource has a user configuration error. - &#x60;true&#x60;: The resources associated with the WifConfig object are properly configured and operational at the time of the check. | [optional] 
**description** | **str** | Provides additional information about the WifConfig resource status. - When &#x60;Configured&#x60; is &#x60;false&#x60;, this field contains details about the user configuration error. - When &#x60;Configured&#x60; is &#x60;true&#x60;, this field may be empty or contain optional notes about the configuration. | [optional] 

## Example

```python
from ocm_client.models.wif_config_status import WifConfigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WifConfigStatus from a JSON string
wif_config_status_instance = WifConfigStatus.from_json(json)
# print the JSON string representation of the object
print(WifConfigStatus.to_json())

# convert the object into a dict
wif_config_status_dict = wif_config_status_instance.to_dict()
# create an instance of WifConfigStatus from a dict
wif_config_status_from_dict = WifConfigStatus.from_dict(wif_config_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


