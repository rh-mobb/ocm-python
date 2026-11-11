# ClusterStatus

Detailed status of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ClusterStatus&#39; if this is a complete object or &#39;ClusterStatusLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**dns_ready** | **bool** | DNSReady from Provisioner | [optional] 
**oidc_ready** | **bool** | OIDCReady from user configuration. | [optional] 
**configuration_mode** | [**ClusterConfigurationMode**](ClusterConfigurationMode.md) |  | [optional] 
**current_compute** | **int** | Current Replicas available for a Hosted Cluster | [optional] 
**description** | **str** | Detailed description of the cluster status. | [optional] 
**limited_support_reason_count** | **int** | Limited Support Reason Count | [optional] 
**provision_error_code** | **str** | Provisioning Error Code | [optional] 
**provision_error_message** | **str** | Provisioning Error Message | [optional] 
**state** | [**ClusterState**](ClusterState.md) |  | [optional] 

## Example

```python
from ocm_client.models.cluster_status import ClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatus from a JSON string
cluster_status_instance = ClusterStatus.from_json(json)
# print the JSON string representation of the object
print(ClusterStatus.to_json())

# convert the object into a dict
cluster_status_dict = cluster_status_instance.to_dict()
# create an instance of ClusterStatus from a dict
cluster_status_from_dict = ClusterStatus.from_dict(cluster_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


