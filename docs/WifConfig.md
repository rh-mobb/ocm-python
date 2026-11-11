# WifConfig

Definition of an wif_config resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;WifConfig&#39; if this is a complete object or &#39;WifConfigLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**display_name** | **str** | The name OCM clients will display for this wif_config. | [optional] 
**gcp** | [**WifGcp**](WifGcp.md) |  | [optional] 
**organization** | [**OrganizationLink**](OrganizationLink.md) |  | [optional] 
**wif_templates** | **List[str]** | Wif template(s) used to configure IAM resources | [optional] 

## Example

```python
from ocm_client.models.wif_config import WifConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WifConfig from a JSON string
wif_config_instance = WifConfig.from_json(json)
# print the JSON string representation of the object
print(WifConfig.to_json())

# convert the object into a dict
wif_config_dict = wif_config_instance.to_dict()
# create an instance of WifConfig from a dict
wif_config_from_dict = WifConfig.from_dict(wif_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


