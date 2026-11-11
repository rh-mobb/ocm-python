# ClusterConsole

Information about the console of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the console of the cluster. | [optional] 

## Example

```python
from ocm_client.models.cluster_console import ClusterConsole

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterConsole from a JSON string
cluster_console_instance = ClusterConsole.from_json(json)
# print the JSON string representation of the object
print(ClusterConsole.to_json())

# convert the object into a dict
cluster_console_dict = cluster_console_instance.to_dict()
# create an instance of ClusterConsole from a dict
cluster_console_from_dict = ClusterConsole.from_dict(cluster_console_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


