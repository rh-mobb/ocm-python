# InflightCheck

Representation of check running before the cluster is provisioned.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;InflightCheck&#39; if this is a complete object or &#39;InflightCheckLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**details** | [**object**](.md) | Details regarding the state of the inflight check. | [optional] 
**ended_at** | **datetime** | The time the check finished running. | [optional] 
**name** | **str** | The name of the inflight check. | [optional] 
**restarts** | **int** | The number of times the inflight check restarted. | [optional] 
**started_at** | **datetime** | The time the check started running. | [optional] 
**state** | [**InflightCheckState**](InflightCheckState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


