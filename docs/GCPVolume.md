# GCPVolume

Holds settings for an GCP storage volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Volume size in Gib. | [optional] 

## Example

```python
from ocm_client.models.gcp_volume import GCPVolume

# TODO update the JSON string below
json = "{}"
# create an instance of GCPVolume from a JSON string
gcp_volume_instance = GCPVolume.from_json(json)
# print the JSON string representation of the object
print(GCPVolume.to_json())

# convert the object into a dict
gcp_volume_dict = gcp_volume_instance.to_dict()
# create an instance of GCPVolume from a dict
gcp_volume_from_dict = GCPVolume.from_dict(gcp_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


