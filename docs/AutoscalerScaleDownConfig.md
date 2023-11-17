# AutoscalerScaleDownConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_after_add** | **str** | How long after scale up that scale down evaluation resumes. | [optional] 
**delay_after_delete** | **str** | How long after node deletion that scale down evaluation resumes, defaults to scan-interval. | [optional] 
**delay_after_failure** | **str** | How long after scale down failure that scale down evaluation resumes. | [optional] 
**enabled** | **bool** | Should cluster-autoscaler scale down the cluster. | [optional] 
**unneeded_time** | **str** | How long a node should be unneeded before it is eligible for scale down. | [optional] 
**utilization_threshold** | **str** | Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


