# GcpFirewallRulesStatusEntry

Status of an individual GCP firewall rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured_correctly** | **bool** | Whether the firewall rule is configured correctly. | [optional] 
**description** | **str** | Description of each firewall rule | [optional] 
**exists** | **bool** | Whether the firewall rule exists in GCP. | [optional] 
**name** | **str** | Name of the firewall rule in GCP. | [optional] 

## Example

```python
from ocm_client.models.gcp_firewall_rules_status_entry import GcpFirewallRulesStatusEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GcpFirewallRulesStatusEntry from a JSON string
gcp_firewall_rules_status_entry_instance = GcpFirewallRulesStatusEntry.from_json(json)
# print the JSON string representation of the object
print(GcpFirewallRulesStatusEntry.to_json())

# convert the object into a dict
gcp_firewall_rules_status_entry_dict = gcp_firewall_rules_status_entry_instance.to_dict()
# create an instance of GcpFirewallRulesStatusEntry from a dict
gcp_firewall_rules_status_entry_from_dict = GcpFirewallRulesStatusEntry.from_dict(gcp_firewall_rules_status_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


