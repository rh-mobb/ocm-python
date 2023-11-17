# ClusterAutoscaler

Cluster-wide autoscaling configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ClusterAutoscaler&#39; if this is a complete object or &#39;ClusterAutoscalerLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**balance_similar_node_groups** | **bool** | BalanceSimilarNodeGroups enables/disables the &#x60;--balance-similar-node-groups&#x60; cluster-autoscaler feature. This feature will automatically identify node groups with the same instance type and the same set of labels and try to keep the respective sizes of those node groups balanced. | [optional] 
**balancing_ignored_labels** | **list[str]** | This option specifies labels that cluster autoscaler should ignore when considering node group similarity. For example, if you have nodes with \&quot;topology.ebs.csi.aws.com/zone\&quot; label, you can add name of this label here to prevent cluster autoscaler from splitting nodes into different node groups based on its value. | [optional] 
**ignore_daemonsets_utilization** | **bool** | Should CA ignore DaemonSet pods when calculating resource utilization for scaling down. false by default. | [optional] 
**log_verbosity** | **int** | Sets the autoscaler log level. Default value is 1, level 4 is recommended for DEBUGGING and level 6 will enable almost everything. | [optional] 
**max_node_provision_time** | **str** | Maximum time CA waits for node to be provisioned. | [optional] 
**max_pod_grace_period** | **int** | Gives pods graceful termination time before scaling down. | [optional] 
**pod_priority_threshold** | **int** | To allow users to schedule \&quot;best-effort\&quot; pods, which shouldn&#39;t trigger Cluster Autoscaler actions, but only run when there are spare resources available, More info: https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption. | [optional] 
**resource_limits** | [**AutoscalerResourceLimits**](AutoscalerResourceLimits.md) |  | [optional] 
**scale_down** | [**AutoscalerScaleDownConfig**](AutoscalerScaleDownConfig.md) |  | [optional] 
**skip_nodes_with_local_storage** | **bool** | Enables/Disables &#x60;--skip-nodes-with-local-storage&#x60; CA feature flag. If true cluster autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir or HostPath. true by default at autoscaler. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


