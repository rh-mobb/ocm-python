# ClusterLink

Definition of a cluster link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | HREF for the cluster, filled in response. | [optional] 
**id** | **str** | The cluster&#39;s ID. | [optional] 

## Example

```python
from ocm_client.models.cluster_link import ClusterLink

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLink from a JSON string
cluster_link_instance = ClusterLink.from_json(json)
# print the JSON string representation of the object
print(ClusterLink.to_json())

# convert the object into a dict
cluster_link_dict = cluster_link_instance.to_dict()
# create an instance of ClusterLink from a dict
cluster_link_from_dict = ClusterLink.from_dict(cluster_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


