# GcpFirewallRuleAllowed

Allowed protocol and ports for a GCP firewall rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_protocol** | **str** | IP protocol (e.g. \&quot;tcp\&quot;, \&quot;udp\&quot;, \&quot;icmp\&quot;). | [optional] 
**ports** | **List[str]** | Ports to allow (e.g. \&quot;6443\&quot;, \&quot;10250\&quot;). | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rule_allowed import GcpFirewallRuleAllowed

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRuleAllowed from a JSON string
gcp_firewall_rule_allowed_instance = GcpFirewallRuleAllowed.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRuleAllowed.to_json())

# convert the object into a dict
gcp_firewall_rule_allowed_dict = gcp_firewall_rule_allowed_instance.to_dict()
# create an instance of GcpFirewallRuleAllowed from a dict
gcp_firewall_rule_allowed_from_dict = GcpFirewallRuleAllowed.from_dict(gcp_firewall_rule_allowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


