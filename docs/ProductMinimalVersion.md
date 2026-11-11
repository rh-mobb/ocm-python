# ProductMinimalVersion

Representation of a product minimal version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ProductMinimalVersion&#39; if this is a complete object or &#39;ProductMinimalVersionLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**rosa_cli** | **str** | The ROSA CLI minimal version. | [optional] 
**start_date** | **datetime** | The start date for this minimal version. | [optional] 

## Example

```python
from ocm_client.models.product_minimal_version import ProductMinimalVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMinimalVersion from a JSON string
product_minimal_version_instance = ProductMinimalVersion.from_json(json)
# print the JSON string representation of the object
print(ProductMinimalVersion.to_json())

# convert the object into a dict
product_minimal_version_dict = product_minimal_version_instance.to_dict()
# create an instance of ProductMinimalVersion from a dict
product_minimal_version_from_dict = ProductMinimalVersion.from_dict(product_minimal_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


