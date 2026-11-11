# GcpFirewallRuleTemplate

GCP firewall rule template definition. Templates define the set of firewall rules that will be created for a cluster. Each template has a version and one or more profiles (e.g. \"public\", \"private\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Human-readable description of this template profile. | [optional] 
**href** | **str** | Self link to the template resource. | [optional] 
**profile** | **str** | Profile name (e.g. \&quot;public\&quot;, \&quot;private\&quot;). | [optional] 
**version** | **str** | Template version identifier (e.g. \&quot;v1\&quot;). | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rule_template import GcpFirewallRuleTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRuleTemplate from a JSON string
gcp_firewall_rule_template_instance = GcpFirewallRuleTemplate.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRuleTemplate.to_json())

# convert the object into a dict
gcp_firewall_rule_template_dict = gcp_firewall_rule_template_instance.to_dict()
# create an instance of GcpFirewallRuleTemplate from a dict
gcp_firewall_rule_template_from_dict = GcpFirewallRuleTemplate.from_dict(gcp_firewall_rule_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


