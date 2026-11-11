# LimitedSupportReason

A reason that a cluster is in limited support.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;LimitedSupportReason&#39; if this is a complete object or &#39;LimitedSupportReasonLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**creation_timestamp** | **datetime** | The time the reason was detected. | [optional] 
**details** | **str** | URL with a link to a detailed description of the reason. | [optional] 
**detection_type** | [**DetectionType**](DetectionType.md) |  | [optional] 
**override** | [**LimitedSupportReasonOverride**](LimitedSupportReasonOverride.md) |  | [optional] 
**summary** | **str** | Summary of the reason. | [optional] 
**template** | [**LimitedSupportReasonTemplate**](LimitedSupportReasonTemplate.md) |  | [optional] 

## Example

```python
from ocm_client.models.limited_support_reason import LimitedSupportReason

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedSupportReason from a JSON string
limited_support_reason_instance = LimitedSupportReason.from_json(json)
# print the JSON string representation of the object
print(LimitedSupportReason.to_json())

# convert the object into a dict
limited_support_reason_dict = limited_support_reason_instance.to_dict()
# create an instance of LimitedSupportReason from a dict
limited_support_reason_from_dict = LimitedSupportReason.from_dict(limited_support_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


