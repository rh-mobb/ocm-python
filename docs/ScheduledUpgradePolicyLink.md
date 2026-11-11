# ScheduledUpgradePolicyLink

Reference to one of the three kinds of upgrade policy resource. Kind identifies which policy type it is; id and href come from the standard metadata added by the generator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ScheduledUpgradePolicyLink&#39; if this is a complete object or &#39;ScheduledUpgradePolicyLinkLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 

## Example

```python
from ocm_client.models.scheduled_upgrade_policy_link import ScheduledUpgradePolicyLink

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledUpgradePolicyLink from a JSON string
scheduled_upgrade_policy_link_instance = ScheduledUpgradePolicyLink.from_json(json)
# print the JSON string representation of the object
print(ScheduledUpgradePolicyLink.to_json())

# convert the object into a dict
scheduled_upgrade_policy_link_dict = scheduled_upgrade_policy_link_instance.to_dict()
# create an instance of ScheduledUpgradePolicyLink from a dict
scheduled_upgrade_policy_link_from_dict = ScheduledUpgradePolicyLink.from_dict(scheduled_upgrade_policy_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


