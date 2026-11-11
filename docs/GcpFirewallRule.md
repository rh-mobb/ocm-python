# GcpFirewallRule

GCP firewall rule configuration for BYO (Bring Your Own) firewall workflow. These are organization-level resources that can be created before cluster provisioning and reused after cluster deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;GcpFirewallRule&#39; if this is a complete object or &#39;GcpFirewallRuleLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**gcp_network** | [**GcpFirewallRuleGcpNetwork**](GcpFirewallRuleGcpNetwork.md) |  | [optional] 
**name** | **str** | Firewall rule name (unique per organization). | [optional] 
**organization** | [**OrganizationLink**](OrganizationLink.md) |  | [optional] 
**profile** | **str** | Profile type (e.g. \&quot;public\&quot;, \&quot;private\&quot;). | [optional] 
**status** | [**GcpFirewallRuleStatus**](GcpFirewallRuleStatus.md) |  | [optional] 
**template** | [**GcpFirewallRuleTemplateRef**](GcpFirewallRuleTemplateRef.md) |  | [optional] 
**wif_config** | [**WifConfig**](WifConfig.md) |  | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rule import GcpFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRule from a JSON string
gcp_firewall_rule_instance = GcpFirewallRule.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRule.to_json())

# convert the object into a dict
gcp_firewall_rule_dict = gcp_firewall_rule_instance.to_dict()
# create an instance of GcpFirewallRule from a dict
gcp_firewall_rule_from_dict = GcpFirewallRule.from_dict(gcp_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


