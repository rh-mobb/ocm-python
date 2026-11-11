# ProductTechnologyPreview

Representation of a product technology preview.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ProductTechnologyPreview&#39; if this is a complete object or &#39;ProductTechnologyPreviewLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**additional_text** | **str** | Message associated with this technology preview. | [optional] 
**end_date** | **datetime** | The end date for this technology preview. | [optional] 
**start_date** | **datetime** | The start date for this technology preview. | [optional] 

## Example

```python
from ocm_client.models.product_technology_preview import ProductTechnologyPreview

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTechnologyPreview from a JSON string
product_technology_preview_instance = ProductTechnologyPreview.from_json(json)
# print the JSON string representation of the object
print(ProductTechnologyPreview.to_json())

# convert the object into a dict
product_technology_preview_dict = product_technology_preview_instance.to_dict()
# create an instance of ProductTechnologyPreview from a dict
product_technology_preview_from_dict = ProductTechnologyPreview.from_dict(product_technology_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


