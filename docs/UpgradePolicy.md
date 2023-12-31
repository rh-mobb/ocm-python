# UpgradePolicy

Representation of an upgrade policy that can be set for a cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;UpgradePolicy&#39; if this is a complete object or &#39;UpgradePolicyLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cluster_id** | **str** | Cluster ID this upgrade policy is defined for. | [optional] 
**enable_minor_version_upgrades** | **bool** | Indicates if minor version upgrades are allowed for automatic upgrades (for manual it&#39;s always allowed). | [optional] 
**next_run** | **datetime** | Next time the upgrade should run. | [optional] 
**schedule** | **str** | Schedule cron expression that defines automatic upgrade scheduling. | [optional] 
**schedule_type** | [**ScheduleType**](ScheduleType.md) |  | [optional] 
**upgrade_type** | [**UpgradeType**](UpgradeType.md) |  | [optional] 
**version** | **str** | Version is the desired upgrade version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


