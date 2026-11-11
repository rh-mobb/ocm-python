# AzureNodePoolOsDisk

Defines the configuration of a Node Pool's OS disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persistence** | **str** | Specifies the OS Disk persistence for the OS Disks of the Nodes in the Node Pool. Valid values are: * persistent * ephemeral If not specified, Persistent OS Disks are used. | [optional] 
**size_gibibytes** | **int** | The size in GiB to assign to the OS disks of the Nodes in the Node Pool. The property is the number of bytes x 1024^3. If not specified, OS disk size is 64 GiB. | [optional] 
**sse_encryption_set_resource_id** | **str** | The Azure Resource ID of a pre-existing Azure Disk Encryption Set (DES). When provided, Server-Side Encryption (SSE) on the OS Disks of the Nodes of the Node Pool is performed using the provided Disk Encryption Set. It must be located in the same Azure location as the parent Cluster.   It must be located in the same Azure Subscription as the parent Cluster. The Azure Resource Group Name specified as part of it must be a different resource group name than the one specified in the parent Cluster&#39;s &#x60;managed_resource_group_name&#x60;. The Azure Resource Group Name specified as part of it can be the same, or a different one than the one specified in the parent Cluster&#39;s &#x60;resource_group_name&#x60;. If not specified, Server-Side Encryption (SSE) on the OS Disks of the Nodes of the Node Pool  is performed with platform managed keys. | [optional] 
**storage_account_type** | **str** | The disk storage account type to use for the OS disks of the Nodes in the Node Pool. Valid values are: * Standard_LRS: HDD * StandardSSD_LRS: Standard SSD * Premium_LRS: Premium SDD * UltraSSD_LRS: Ultra SDD  If not specified, &#x60;Premium_LRS&#x60; is used. | [optional] 

## Example

```python
from ocm_client.models.azure_node_pool_os_disk import AzureNodePoolOsDisk

# TODO update the JSON string below
json = "{}"
# create an instance of AzureNodePoolOsDisk from a JSON string
azure_node_pool_os_disk_instance = AzureNodePoolOsDisk.from_json(json)
# print the JSON string representation of the object
print(AzureNodePoolOsDisk.to_json())

# convert the object into a dict
azure_node_pool_os_disk_dict = azure_node_pool_os_disk_instance.to_dict()
# create an instance of AzureNodePoolOsDisk from a dict
azure_node_pool_os_disk_from_dict = AzureNodePoolOsDisk.from_dict(azure_node_pool_os_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


