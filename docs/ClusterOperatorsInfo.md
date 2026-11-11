# ClusterOperatorsInfo

Provides detailed information about the operators installed on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operators** | [**List[ClusterOperatorInfo]**](ClusterOperatorInfo.md) |  | [optional] 

## Example

```python
from ocm_client.models.cluster_operators_info import ClusterOperatorsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperatorsInfo from a JSON string
cluster_operators_info_instance = ClusterOperatorsInfo.from_json(json)
# print the JSON string representation of the object
print(ClusterOperatorsInfo.to_json())

# convert the object into a dict
cluster_operators_info_dict = cluster_operators_info_instance.to_dict()
# create an instance of ClusterOperatorsInfo from a dict
cluster_operators_info_from_dict = ClusterOperatorsInfo.from_dict(cluster_operators_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


