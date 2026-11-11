# LimitedSupportReasonOverride

Representation of the limited support reason override.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;LimitedSupportReasonOverride&#39; if this is a complete object or &#39;LimitedSupportReasonOverrideLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**enabled** | **bool** | Indicates if the override is enabled | [optional] 

## Example

```python
from ocm_client.models.limited_support_reason_override import LimitedSupportReasonOverride

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedSupportReasonOverride from a JSON string
limited_support_reason_override_instance = LimitedSupportReasonOverride.from_json(json)
# print the JSON string representation of the object
print(LimitedSupportReasonOverride.to_json())

# convert the object into a dict
limited_support_reason_override_dict = limited_support_reason_override_instance.to_dict()
# create an instance of LimitedSupportReasonOverride from a dict
limited_support_reason_override_from_dict = LimitedSupportReasonOverride.from_dict(limited_support_reason_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


