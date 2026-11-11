# ClusterDeployment

Representation of a clusterdeployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ClusterDeployment&#39; if this is a complete object or &#39;ClusterDeploymentLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**content** | **object** | Content of the clusterdeployment. | [optional] 

## Example

```python
from ocm_client.models.cluster_deployment import ClusterDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeployment from a JSON string
cluster_deployment_instance = ClusterDeployment.from_json(json)
# print the JSON string representation of the object
print(ClusterDeployment.to_json())

# convert the object into a dict
cluster_deployment_dict = cluster_deployment_instance.to_dict()
# create an instance of ClusterDeployment from a dict
cluster_deployment_from_dict = ClusterDeployment.from_dict(cluster_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


