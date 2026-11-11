# Azure

Microsoft Azure settings of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etcd_encryption** | [**AzureEtcdEncryption**](AzureEtcdEncryption.md) |  | [optional] 
**managed_resource_group_name** | **str** | The desired name of the Azure Resource Group where the Azure Resources related to the cluster are created. It must not previously exist. The Azure Resource Group is created with the given value, within the Azure Subscription &#x60;subscription_id&#x60; of the cluster. &#x60;managed_resource_group_name&#x60; cannot be equal to the value of &#x60;managed_resource_group&#x60;. &#x60;managed_resource_group_name&#x60; is located in the same Azure location as the cluster&#39;s region. Not to be confused with &#x60;resource_group_name&#x60;, which is the Azure Resource Group Name where the own Azure Resource associated to the cluster resides. Required during creation. Immutable. | [optional] 
**network_security_group_resource_id** | **str** | The Azure Resource ID of a pre-existing Azure Network Security Group. The Network Security Group specified in network_security_group_resource_id must already be associated to the Azure Subnet &#x60;subnet_resource_id&#x60;. It is the Azure Network Security Group associated to the cluster&#39;s subnet specified in &#x60;subnet_resource_id&#x60;. &#x60;network_security_group_resource_id&#x60; must be located in the same Azure location as the cluster&#39;s region. The Azure Subscription specified as part of &#x60;network_security_group_resource_id&#x60; must be located in the same Azure Subscription as &#x60;subscription_id&#x60;. The Azure Resource Group Name specified as part of &#x60;network_security_group_resource_id&#x60; must belong to the Azure Subscription &#x60;subscription_id&#x60;, and in the same Azure location as the cluster&#39;s region. The Azure Resource Group Name specified as part of &#x60;network_security_group_resource_id&#x60; must be a different Resource Group Name than the one specified in &#x60;managed_resource_group_name&#x60;. The Azure Resource Group Name specified as part of &#x60;network_security_group_resource_id&#x60; can be the same, or a different one than the one specified in &#x60;resource_group_name&#x60;. Required during creation. Immutable. | [optional] 
**nodes_outbound_connectivity** | [**AzureNodesOutboundConnectivity**](AzureNodesOutboundConnectivity.md) |  | [optional] 
**operators_authentication** | [**AzureOperatorsAuthentication**](AzureOperatorsAuthentication.md) |  | [optional] 
**resource_group_name** | **str** | The Azure Resource Group Name of the cluster. It must be a pre-existing Azure Resource Group and it must exist within the Azure Subscription &#x60;subscription_id&#x60; of the cluster. &#x60;resource_group_name&#x60; is located in the same Azure location as the cluster&#39;s region. Required during creation. Immutable. | [optional] 
**resource_name** | **str** | The Azure Resource Name of the cluster. It must be within the Azure Resource Group Name &#x60;resource_group_name&#x60;. &#x60;resource_name&#x60; is located in the same Azure location as the cluster&#39;s region. Required during creation. Immutable. | [optional] 
**subnet_resource_id** | **str** | The Azure Resource ID of a pre-existing Azure Subnet. It is an Azure Subnet used for the Data Plane of the cluster. &#x60;subnet_resource_id&#x60; must be located in the same Azure location as the cluster&#39;s region. The Azure Subscription specified as part of the &#x60;subnet_resource_id&#x60; must be located in the same Azure Subscription as &#x60;subscription_id&#x60;. The Azure Resource Group Name specified as part of &#x60;subnet_resource_id&#x60; must belong to the Azure Subscription &#x60;subscription_id&#x60;, and in the same Azure location as the cluster&#39;s region. The Azure Resource Group Name specified as part of &#x60;subnet_resource_id&#x60; must be a different Resource Group Name than the one specified in &#x60;managed_resource_group_name&#x60;. The Azure Resource Group Name specified as part of the &#x60;subnet_resource_id&#x60; can be the same, or a different one than the one specified in &#x60;resource_group_name&#x60;. Required during creation. Immutable. | [optional] 
**subscription_id** | **str** | The Azure Subscription ID associated with the cluster. It must belong to the Microsoft Entra Tenant ID &#x60;tenant_id&#x60;. Required during creation. Immutable. | [optional] 
**tenant_id** | **str** | The Microsoft Entra Tenant ID where the cluster belongs. Required during creation. Immutable. | [optional] 

## Example

```python
from ocm_client.models.azure import Azure

# TODO update the JSON string below
json = "{}"
# create an instance of Azure from a JSON string
azure_instance = Azure.from_json(json)
# print the JSON string representation of the object
print(Azure.to_json())

# convert the object into a dict
azure_dict = azure_instance.to_dict()
# create an instance of Azure from a dict
azure_from_dict = Azure.from_dict(azure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


