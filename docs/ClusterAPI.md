# ClusterAPI

Information about the API of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_block_access** | [**CIDRBlockAccess**](CIDRBlockAccess.md) |  | [optional] 
**url** | **str** | The URL of the API server of the cluster. | [optional] 
**listening** | [**ListeningMethod**](ListeningMethod.md) |  | [optional] 

## Example

```python
from ocm_client.models.cluster_api import ClusterAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAPI from a JSON string
cluster_api_instance = ClusterAPI.from_json(json)
# print the JSON string representation of the object
print(ClusterAPI.to_json())

# convert the object into a dict
cluster_api_dict = cluster_api_instance.to_dict()
# create an instance of ClusterAPI from a dict
cluster_api_from_dict = ClusterAPI.from_dict(cluster_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


