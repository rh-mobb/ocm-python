# AzureNodePoolEncryptionAtHost

AzureNodePoolEncryptionAtHost defines the encryption setting for Encryption At Host. If not specified, Encryption at Host is not enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State indicates whether Encryption At Host is enabled. When enabled, it enhances Azure Disk Storage Server-Side Encryption to ensure that all temporary disks and disk caches are encrypted at rest and flow encrypted to the Storage clusters. Accepted values are: \&quot;disabled\&quot; or \&quot;enabled\&quot;. If not specified, its value is \&quot;disabled\&quot;, which indicates Encryption At Host is disabled. Immutable. | [optional] 

## Example

```python
from ocm_client.models.azure_node_pool_encryption_at_host import AzureNodePoolEncryptionAtHost

# TODO update the JSON string below
json = "{}"
# create an instance of AzureNodePoolEncryptionAtHost from a JSON string
azure_node_pool_encryption_at_host_instance = AzureNodePoolEncryptionAtHost.from_json(json)
# print the JSON string representation of the object
print(AzureNodePoolEncryptionAtHost.to_json())

# convert the object into a dict
azure_node_pool_encryption_at_host_dict = azure_node_pool_encryption_at_host_instance.to_dict()
# create an instance of AzureNodePoolEncryptionAtHost from a dict
azure_node_pool_encryption_at_host_from_dict = AzureNodePoolEncryptionAtHost.from_dict(azure_node_pool_encryption_at_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


