# ClusterCredentials

Credentials of the a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ClusterCredentials&#39; if this is a complete object or &#39;ClusterCredentialsLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**kubeconfig** | **str** | Administrator _kubeconfig_ file for the cluster. | [optional] 

## Example

```python
from ocm_client.models.cluster_credentials import ClusterCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCredentials from a JSON string
cluster_credentials_instance = ClusterCredentials.from_json(json)
# print the JSON string representation of the object
print(ClusterCredentials.to_json())

# convert the object into a dict
cluster_credentials_dict = cluster_credentials_instance.to_dict()
# create an instance of ClusterCredentials from a dict
cluster_credentials_from_dict = ClusterCredentials.from_dict(cluster_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


