# GcpFirewallRuleSpec

A single rendered GCP firewall rule specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | [**List[GcpFirewallRuleAllowed]**](GcpFirewallRuleAllowed.md) | Allowed protocols and ports. | [optional] 
**direction** | **str** | Direction of traffic (INGRESS or EGRESS). | [optional] 
**name** | **str** | Name of the firewall rule. | [optional] 
**network** | **str** | GCP network URL. | [optional] 
**priority** | **int** | Priority of the rule (0-65535). | [optional] 
**source_ranges** | **List[str]** | Source IP CIDR ranges. | [optional] 
**source_service_accounts** | **List[str]** | Source service accounts. | [optional] 
**target_service_accounts** | **List[str]** | Target service accounts. | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rule_spec import GcpFirewallRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRuleSpec from a JSON string
gcp_firewall_rule_spec_instance = GcpFirewallRuleSpec.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRuleSpec.to_json())

# convert the object into a dict
gcp_firewall_rule_spec_dict = gcp_firewall_rule_spec_instance.to_dict()
# create an instance of GcpFirewallRuleSpec from a dict
gcp_firewall_rule_spec_from_dict = GcpFirewallRuleSpec.from_dict(gcp_firewall_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


