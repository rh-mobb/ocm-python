# Environment

Description of an environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backplane_url** | **str** | the backplane url for the environment | [optional] 
**last_cluster_imageset_sync** | **datetime** | last time that the cluster imageset sync worker checked for version updates | [optional] 
**last_hibernation_check** | **datetime** | last time that the hibernation worker checked for hibernating clusters | [optional] 
**last_limited_support_check** | **datetime** | last time that the worker checked for limited support clusters | [optional] 
**last_limited_support_override_check** | **datetime** | last time that the limited support override worker checked for clusters | [optional] 
**last_upgrade_available_check** | **datetime** | last time that the worker checked for available upgrades | [optional] 
**name** | **str** | environment name | [optional] 

## Example

```python
from ocm_client.models.environment import Environment

# TODO update the JSON string below
json = "{}"
# create an instance of Environment from a JSON string
environment_instance = Environment.from_json(json)
# print the JSON string representation of the object
print(Environment.to_json())

# convert the object into a dict
environment_dict = environment_instance.to_dict()
# create an instance of Environment from a dict
environment_from_dict = Environment.from_dict(environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


