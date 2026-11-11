# NodesInfo

Provides information about the nodes in the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[NodeInfo]**](NodeInfo.md) |  | [optional] 

## Example

```python
from ocm_client.models.nodes_info import NodesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NodesInfo from a JSON string
nodes_info_instance = NodesInfo.from_json(json)
# print the JSON string representation of the object
print(NodesInfo.to_json())

# convert the object into a dict
nodes_info_dict = nodes_info_instance.to_dict()
# create an instance of NodesInfo from a dict
nodes_info_from_dict = NodesInfo.from_dict(nodes_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


