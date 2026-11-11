# ClusterImageRegistry

ClusterImageRegistry represents the configuration for the cluster's internal image registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State indicates whether the image registry is enabled. Unless explicitly set, the image registry is enabled by default. This setting is immutable and cannot be changed after the cluster is created. Valid values: \&quot;enabled\&quot;, \&quot;disabled\&quot;. | [optional] 

## Example

```python
from ocm_client.models.cluster_image_registry import ClusterImageRegistry

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterImageRegistry from a JSON string
cluster_image_registry_instance = ClusterImageRegistry.from_json(json)
# print the JSON string representation of the object
print(ClusterImageRegistry.to_json())

# convert the object into a dict
cluster_image_registry_dict = cluster_image_registry_instance.to_dict()
# create an instance of ClusterImageRegistry from a dict
cluster_image_registry_from_dict = ClusterImageRegistry.from_dict(cluster_image_registry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


