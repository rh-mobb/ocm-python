# Manifest

Representation of a manifestwork.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;Manifest&#39; if this is a complete object or &#39;ManifestLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**creation_timestamp** | **datetime** | Date and time when the manifest got created in OCM database. | [optional] 
**live_resource** | **object** | Transient value to represent the underlying live resource. | [optional] 
**spec** | **object** | Spec of Manifest Work object from open cluster management For more info please check https://open-cluster-management.io/concepts/manifestwork. | [optional] 
**updated_timestamp** | **datetime** | Date and time when the manifest got updated in OCM database. | [optional] 
**workloads** | **List[object]** | List of k8s objects to deploy on a hosted cluster. | [optional] 

## Example

```python
from ocm_client.models.manifest import Manifest

# TODO update the JSON string below
json = "{}"
# create an instance of Manifest from a JSON string
manifest_instance = Manifest.from_json(json)
# print the JSON string representation of the object
print(Manifest.to_json())

# convert the object into a dict
manifest_dict = manifest_instance.to_dict()
# create an instance of Manifest from a dict
manifest_from_dict = Manifest.from_dict(manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


