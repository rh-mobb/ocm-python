# AzureNodePool

Representation of azure node pool specific parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_size** | **str** | The Azure Virtual Machine size identifier used for the Nodes of the Node Pool. Availability of VM sizes are dependent on the Azure Location of the parent Cluster. Required during creation. | [optional] 
**encryption_at_host** | [**AzureNodePoolEncryptionAtHost**](AzureNodePoolEncryptionAtHost.md) |  | [optional] 
**image** | [**AzureNodePoolImage**](AzureNodePoolImage.md) |  | [optional] 
**os_disk** | [**AzureNodePoolOsDisk**](AzureNodePoolOsDisk.md) |  | [optional] 
**resource_name** | **str** | ResourceName is the Azure Resource Name of the NodePool. ResourceName must be within the Azure Resource Group Name of the parent Cluster it belongs to. ResourceName must be located in the same Azure Location as the parent Cluster it belongs to. ResourceName must be located in the same Azure Subscription as the parent Cluster it belongs to. ResourceName must belong to the same Microsoft Entra Tenant ID as the parent Cluster it belongs to. Required during creation. Immutable. | [optional] 

## Example

```python
from ocm_client.models.azure_node_pool import AzureNodePool

# TODO update the JSON string below
json = "{}"
# create an instance of AzureNodePool from a JSON string
azure_node_pool_instance = AzureNodePool.from_json(json)
# print the JSON string representation of the object
print(AzureNodePool.to_json())

# convert the object into a dict
azure_node_pool_dict = azure_node_pool_instance.to_dict()
# create an instance of AzureNodePool from a dict
azure_node_pool_from_dict = AzureNodePool.from_dict(azure_node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


