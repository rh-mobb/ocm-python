# MachinePool

Representation of a machine pool in a cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;MachinePool&#39; if this is a complete object or &#39;MachinePoolLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**aws** | [**AWSMachinePool**](AWSMachinePool.md) |  | [optional] 
**autoscaling** | [**MachinePoolAutoscaling**](MachinePoolAutoscaling.md) |  | [optional] 
**availability_zones** | **list[str]** | The availability zones upon which the nodes are created. | [optional] 
**instance_type** | **str** | The instance type of Nodes to create. | [optional] 
**labels** | **dict(str, str)** | The labels set on the Nodes created. | [optional] 
**replicas** | **int** | The number of Machines (and Nodes) to create. Replicas and autoscaling cannot be used together. | [optional] 
**root_volume** | [**RootVolume**](RootVolume.md) |  | [optional] 
**security_group_filters** | [**list[MachinePoolSecurityGroupFilter]**](MachinePoolSecurityGroupFilter.md) | List of security groups to be applied to MachinePool (Optional) | [optional] 
**subnets** | **list[str]** | The subnets upon which the nodes are created. | [optional] 
**taints** | [**list[Taint]**](Taint.md) | The taints set on the Nodes created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


