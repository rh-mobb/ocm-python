# AzureNodesOutboundConnectivity

The configuration of the node outbound connectivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outbound_type** | **str** | OutboundType is the type of network outbound configuration. The default and only accepted value is &#39;load_balancer&#39;. This value is immutable. | [optional] 

## Example

```python
from ocm_client.models.azure_nodes_outbound_connectivity import AzureNodesOutboundConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of AzureNodesOutboundConnectivity from a JSON string
azure_nodes_outbound_connectivity_instance = AzureNodesOutboundConnectivity.from_json(json)
# print the JSON string representation of the object
print(AzureNodesOutboundConnectivity.to_json())

# convert the object into a dict
azure_nodes_outbound_connectivity_dict = azure_nodes_outbound_connectivity_instance.to_dict()
# create an instance of AzureNodesOutboundConnectivity from a dict
azure_nodes_outbound_connectivity_from_dict = AzureNodesOutboundConnectivity.from_dict(azure_nodes_outbound_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


