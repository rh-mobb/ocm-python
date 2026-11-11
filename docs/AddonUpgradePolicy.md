# AddonUpgradePolicy

Representation of an upgrade policy that can be set for a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddonUpgradePolicy&#39; if this is a complete object or &#39;AddonUpgradePolicyLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**addon_id** | **str** | Addon ID this upgrade policy is defined for | [optional] 
**cluster_id** | **str** | Cluster ID this upgrade policy is defined for. | [optional] 
**next_run** | **datetime** | Next time the upgrade should run. | [optional] 
**schedule** | **str** | Schedule cron expression that defines automatic upgrade scheduling. | [optional] 
**schedule_type** | **str** | Schedule type can be either \&quot;manual\&quot; (single execution) or \&quot;automatic\&quot; (re-occurring). | [optional] 
**upgrade_type** | **str** | Upgrade type specify the type of the upgrade. Must be \&quot;ADDON\&quot;. | [optional] 
**version** | **str** | Version is the desired upgrade version. | [optional] 

## Example

```python
from ocm_client.models.addon_upgrade_policy import AddonUpgradePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AddonUpgradePolicy from a JSON string
addon_upgrade_policy_instance = AddonUpgradePolicy.from_json(json)
# print the JSON string representation of the object
print(AddonUpgradePolicy.to_json())

# convert the object into a dict
addon_upgrade_policy_dict = addon_upgrade_policy_instance.to_dict()
# create an instance of AddonUpgradePolicy from a dict
addon_upgrade_policy_from_dict = AddonUpgradePolicy.from_dict(addon_upgrade_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


