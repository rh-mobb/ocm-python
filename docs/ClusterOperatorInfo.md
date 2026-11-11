# ClusterOperatorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**ClusterOperatorState**](ClusterOperatorState.md) |  | [optional] 
**name** | **str** | Name of the operator. | [optional] 
**reason** | **str** | Extra detail on condition, if available.  Empty string if unknown. | [optional] 
**time** | **datetime** | Time when the sample was obtained, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format. | [optional] 
**version** | **str** | Current version of the operator.  Empty string if unknown. | [optional] 

## Example

```python
from ocm_client.models.cluster_operator_info import ClusterOperatorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperatorInfo from a JSON string
cluster_operator_info_instance = ClusterOperatorInfo.from_json(json)
# print the JSON string representation of the object
print(ClusterOperatorInfo.to_json())

# convert the object into a dict
cluster_operator_info_dict = cluster_operator_info_instance.to_dict()
# create an instance of ClusterOperatorInfo from a dict
cluster_operator_info_from_dict = ClusterOperatorInfo.from_dict(cluster_operator_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


