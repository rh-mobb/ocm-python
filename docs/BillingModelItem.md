# BillingModelItem

BillingModelItem represents a billing model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;BillingModelItem&#39; if this is a complete object or &#39;BillingModelItemLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**billing_model_type** | **str** | BillingModelType is the type of the BillingModel. e.g. standard, marketplace. | [optional] 
**description** | **str** | Single line description of the billing model. | [optional] 
**display_name** | **str** | User friendly display name of the billing model. | [optional] 
**marketplace** | **str** | Indicates the marketplace of the billing model. e.g. gcp, aws, etc. | [optional] 

## Example

```python
from ocm_client.models.billing_model_item import BillingModelItem

# TODO update the JSON string below
json = "{}"
# create an instance of BillingModelItem from a JSON string
billing_model_item_instance = BillingModelItem.from_json(json)
# print the JSON string representation of the object
print(BillingModelItem.to_json())

# convert the object into a dict
billing_model_item_dict = billing_model_item_instance.to_dict()
# create an instance of BillingModelItem from a dict
billing_model_item_from_dict = BillingModelItem.from_dict(billing_model_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


