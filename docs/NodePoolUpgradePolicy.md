# NodePoolUpgradePolicy

Representation of an upgrade policy that can be set for a node pool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;NodePoolUpgradePolicy&#39; if this is a complete object or &#39;NodePoolUpgradePolicyLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cluster_id** | **str** | Cluster ID this upgrade policy for node pool is defined for. | [optional] 
**creation_timestamp** | **datetime** | Timestamp for creation of resource. | [optional] 
**enable_minor_version_upgrades** | **bool** | Indicates if minor version upgrades are allowed for automatic upgrades (for manual it&#39;s always allowed). | [optional] 
**last_update_timestamp** | **datetime** | Timestamp for last update that happened to resource. | [optional] 
**next_run** | **datetime** | Next time the upgrade should run. | [optional] 
**node_pool_id** | **str** | Node Pool ID this upgrade policy is defined for. | [optional] 
**schedule** | **str** | Schedule cron expression that defines automatic upgrade scheduling. | [optional] 
**schedule_type** | [**ScheduleType**](ScheduleType.md) |  | [optional] 
**state** | [**UpgradePolicyState**](UpgradePolicyState.md) |  | [optional] 
**upgrade_type** | [**UpgradeType**](UpgradeType.md) |  | [optional] 
**version** | **str** | Version is the desired upgrade version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


