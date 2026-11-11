# AdditionalCatalogSource

Representation of an addon catalog source object used by addon versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the additional catalog source | [optional] 
**enabled** | **bool** | Indicates is this additional catalog source is enabled for the addon | [optional] 
**image** | **str** | Image of the additional catalog source. | [optional] 
**name** | **str** | Name of the additional catalog source. | [optional] 

## Example

```python
from ocm_client.models.additional_catalog_source import AdditionalCatalogSource

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalCatalogSource from a JSON string
additional_catalog_source_instance = AdditionalCatalogSource.from_json(json)
# print the JSON string representation of the object
print(AdditionalCatalogSource.to_json())

# convert the object into a dict
additional_catalog_source_dict = additional_catalog_source_instance.to_dict()
# create an instance of AdditionalCatalogSource from a dict
additional_catalog_source_from_dict = AdditionalCatalogSource.from_dict(additional_catalog_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


