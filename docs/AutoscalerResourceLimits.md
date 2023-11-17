# AutoscalerResourceLimits

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpus** | [**list[AutoscalerResourceLimitsGPULimit]**](AutoscalerResourceLimitsGPULimit.md) | Minimum and maximum number of different GPUs in cluster, in the format &lt;gpu_type&gt;:&lt;min&gt;:&lt;max&gt;. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times. | [optional] 
**cores** | [**ResourceRange**](ResourceRange.md) |  | [optional] 
**max_nodes_total** | **int** | Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number. | [optional] 
**memory** | [**ResourceRange**](ResourceRange.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


