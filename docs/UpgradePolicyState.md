# UpgradePolicyState

Representation of an upgrade policy state that that is set for a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;UpgradePolicyState&#39; if this is a complete object or &#39;UpgradePolicyStateLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**description** | **str** | Description of the state. | [optional] 
**value** | [**UpgradePolicyStateValue**](UpgradePolicyStateValue.md) |  | [optional] 

## Example

```python
from ocm_client.models.upgrade_policy_state import UpgradePolicyState

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradePolicyState from a JSON string
upgrade_policy_state_instance = UpgradePolicyState.from_json(json)
# print the JSON string representation of the object
print(UpgradePolicyState.to_json())

# convert the object into a dict
upgrade_policy_state_dict = upgrade_policy_state_instance.to_dict()
# create an instance of UpgradePolicyState from a dict
upgrade_policy_state_from_dict = UpgradePolicyState.from_dict(upgrade_policy_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


