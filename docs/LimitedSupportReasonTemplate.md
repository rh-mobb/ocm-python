# LimitedSupportReasonTemplate

A template for cluster limited support reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;LimitedSupportReasonTemplate&#39; if this is a complete object or &#39;LimitedSupportReasonTemplateLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**details** | **str** | A detailed description of the reason. | [optional] 
**summary** | **str** | Summary of the reason. | [optional] 

## Example

```python
from ocm_client.models.limited_support_reason_template import LimitedSupportReasonTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedSupportReasonTemplate from a JSON string
limited_support_reason_template_instance = LimitedSupportReasonTemplate.from_json(json)
# print the JSON string representation of the object
print(LimitedSupportReasonTemplate.to_json())

# convert the object into a dict
limited_support_reason_template_dict = limited_support_reason_template_instance.to_dict()
# create an instance of LimitedSupportReasonTemplate from a dict
limited_support_reason_template_from_dict = LimitedSupportReasonTemplate.from_dict(limited_support_reason_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


