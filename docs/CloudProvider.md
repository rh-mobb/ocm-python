# CloudProvider

Cloud provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;CloudProvider&#39; if this is a complete object or &#39;CloudProviderLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**display_name** | **str** | Name of the cloud provider for display purposes. It can contain any characters, including spaces. | [optional] 
**name** | **str** | Human friendly identifier of the cloud provider, for example &#x60;aws&#x60;. | [optional] 
**regions** | [**List[CloudRegion]**](CloudRegion.md) | (optional) Provider&#39;s regions - only included when listing providers with &#x60;fetchRegions&#x3D;true&#x60;. | [optional] 

## Example

```python
from ocm_client.models.cloud_provider import CloudProvider

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProvider from a JSON string
cloud_provider_instance = CloudProvider.from_json(json)
# print the JSON string representation of the object
print(CloudProvider.to_json())

# convert the object into a dict
cloud_provider_dict = cloud_provider_instance.to_dict()
# create an instance of CloudProvider from a dict
cloud_provider_from_dict = CloudProvider.from_dict(cloud_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


