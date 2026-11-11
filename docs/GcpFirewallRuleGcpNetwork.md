# GcpFirewallRuleGcpNetwork

GCP network configuration for a firewall rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_cidr** | **str** | Machine CIDR block. | [optional] 
**project_id** | **str** | GCP project ID. | [optional] 
**vpc_name** | **str** | VPC network name. | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rule_gcp_network import GcpFirewallRuleGcpNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRuleGcpNetwork from a JSON string
gcp_firewall_rule_gcp_network_instance = GcpFirewallRuleGcpNetwork.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRuleGcpNetwork.to_json())

# convert the object into a dict
gcp_firewall_rule_gcp_network_dict = gcp_firewall_rule_gcp_network_instance.to_dict()
# create an instance of GcpFirewallRuleGcpNetwork from a dict
gcp_firewall_rule_gcp_network_from_dict = GcpFirewallRuleGcpNetwork.from_dict(gcp_firewall_rule_gcp_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


