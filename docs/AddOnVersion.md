# AddOnVersion

Representation of an add-on version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddOnVersion&#39; if this is a complete object or &#39;AddOnVersionLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**additional_catalog_sources** | [**List[AdditionalCatalogSource]**](AdditionalCatalogSource.md) | Additional catalog sources associated with this addon version | [optional] 
**available_upgrades** | **List[str]** | AvailableUpgrades is the list of versions this version can be upgraded to. | [optional] 
**channel** | **str** | The specific addon catalog source channel of packages | [optional] 
**config** | [**AddOnConfig**](AddOnConfig.md) |  | [optional] 
**enabled** | **bool** | Indicates if this add-on version can be added to clusters. | [optional] 
**package_image** | **str** | The package image for this addon version | [optional] 
**parameters** | [**List[AddOnParameter]**](AddOnParameter.md) | List of parameters for this add-on version. | [optional] 
**pull_secret_name** | **str** | The pull secret name used for this addon version. | [optional] 
**requirements** | [**List[AddOnRequirement]**](AddOnRequirement.md) | List of requirements for this add-on version. | [optional] 
**source_image** | **str** | The catalog source image for this add-on version. | [optional] 
**sub_operators** | [**List[AddOnSubOperator]**](AddOnSubOperator.md) | List of sub operators for this add-on version. | [optional] 

## Example

```python
from ocm_client.models.add_on_version import AddOnVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnVersion from a JSON string
add_on_version_instance = AddOnVersion.from_json(json)
# print the JSON string representation of the object
print(AddOnVersion.to_json())

# convert the object into a dict
add_on_version_dict = add_on_version_instance.to_dict()
# create an instance of AddOnVersion from a dict
add_on_version_from_dict = AddOnVersion.from_dict(add_on_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


