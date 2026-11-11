# GcpFirewallRuleStatus

Status of a GCP firewall rule set, containing the rendered rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[GcpFirewallRuleSpec]**](GcpFirewallRuleSpec.md) | Rendered firewall rule specifications. | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rule_status import GcpFirewallRuleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRuleStatus from a JSON string
gcp_firewall_rule_status_instance = GcpFirewallRuleStatus.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRuleStatus.to_json())

# convert the object into a dict
gcp_firewall_rule_status_dict = gcp_firewall_rule_status_instance.to_dict()
# create an instance of GcpFirewallRuleStatus from a dict
gcp_firewall_rule_status_from_dict = GcpFirewallRuleStatus.from_dict(gcp_firewall_rule_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


