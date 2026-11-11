# GcpFirewallRuleTemplateRef

Template version and profile reference for a firewall rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Self link to the template resource. | [optional] 
**version** | **str** | Template version identifier. | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rule_template_ref import GcpFirewallRuleTemplateRef

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRuleTemplateRef from a JSON string
gcp_firewall_rule_template_ref_instance = GcpFirewallRuleTemplateRef.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRuleTemplateRef.to_json())

# convert the object into a dict
gcp_firewall_rule_template_ref_dict = gcp_firewall_rule_template_ref_instance.to_dict()
# create an instance of GcpFirewallRuleTemplateRef from a dict
gcp_firewall_rule_template_ref_from_dict = GcpFirewallRuleTemplateRef.from_dict(gcp_firewall_rule_template_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


