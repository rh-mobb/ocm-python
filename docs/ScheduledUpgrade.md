# ScheduledUpgrade

Representation of one upgrade scheduled somewhere in the fleet, regardless of which kind of upgrade policy scheduled it. Read-only; the authoritative resource is linked from 'policy'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ScheduledUpgrade&#39; if this is a complete object or &#39;ScheduledUpgradeLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cluster** | [**Cluster**](Cluster.md) |  | [optional] 
**created_at** | **datetime** | Creation timestamp. Not tracked for &#39;OSD&#39; upgrades (null for those). | [optional] 
**next_run** | **datetime** | Next time the upgrade should run. | [optional] 
**node_pool** | [**NodePool**](NodePool.md) |  | [optional] 
**policy** | [**ScheduledUpgradePolicyLink**](ScheduledUpgradePolicyLink.md) |  | [optional] 
**schedule_type** | [**ScheduleType**](ScheduleType.md) |  | [optional] 
**state** | [**UpgradePolicyState**](UpgradePolicyState.md) |  | [optional] 
**type** | [**UpgradeType**](UpgradeType.md) |  | [optional] 
**updated_at** | **datetime** | Last update timestamp. Not tracked for &#39;OSD&#39; upgrades (null for those). | [optional] 
**version** | **str** | Desired upgrade version. | [optional] 

## Example

```python
from ocm_client.models.scheduled_upgrade import ScheduledUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledUpgrade from a JSON string
scheduled_upgrade_instance = ScheduledUpgrade.from_json(json)
# print the JSON string representation of the object
print(ScheduledUpgrade.to_json())

# convert the object into a dict
scheduled_upgrade_dict = scheduled_upgrade_instance.to_dict()
# create an instance of ScheduledUpgrade from a dict
scheduled_upgrade_from_dict = ScheduledUpgrade.from_dict(scheduled_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


