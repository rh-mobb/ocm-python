# AzureNodePoolImage

Specifies the Azure Marketplace image to use for the Nodes of the Node Pool. When specified, the provided image is used instead of the default RHCOS image. All four fields must be provided together. Optional during creation. Immutable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | SKU specifies an instance of an offer, such as a major release of a distribution. | [optional] 
**offer** | **str** | Offer specifies the name of a group of related images created by the publisher. | [optional] 
**publisher** | **str** | Publisher is the name of the organization that created the image. | [optional] 
**version** | **str** | Version specifies the version of an image SKU. | [optional] 

## Example

```python
from ocm_client.models.azure_node_pool_image import AzureNodePoolImage

# TODO update the JSON string below
json = "{}"
# create an instance of AzureNodePoolImage from a JSON string
azure_node_pool_image_instance = AzureNodePoolImage.from_json(json)
# print the JSON string representation of the object
print(AzureNodePoolImage.to_json())

# convert the object into a dict
azure_node_pool_image_dict = azure_node_pool_image_instance.to_dict()
# create an instance of AzureNodePoolImage from a dict
azure_node_pool_image_from_dict = AzureNodePoolImage.from_dict(azure_node_pool_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


