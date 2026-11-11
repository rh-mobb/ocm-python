# GcpFirewallRulesStatus

Status of GCP firewall rules verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the current status. | [optional] 
**kind** | **str** | Kind is the resource type identifier. | [optional] 
**rules** | [**List[GcpFirewallRulesStatusEntry]**](GcpFirewallRulesStatusEntry.md) | Individual firewall rule status entries. | [optional] 
**state** | **str** | Overall state of the firewall rules (e.g. \&quot;ready\&quot;, \&quot;incomplete\&quot;, \&quot;not_found\&quot;). | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rules_status import GcpFirewallRulesStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRulesStatus from a JSON string
gcp_firewall_rules_status_instance = GcpFirewallRulesStatus.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRulesStatus.to_json())

# convert the object into a dict
gcp_firewall_rules_status_dict = gcp_firewall_rules_status_instance.to_dict()
# create an instance of GcpFirewallRulesStatus from a dict
gcp_firewall_rules_status_from_dict = GcpFirewallRulesStatus.from_dict(gcp_firewall_rules_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


