# GCPFlavour

Specification for different classes of nodes inside a flavour.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_instance_type** | **str** | GCP default instance type for the worker volume.  User can be overridden specifying in the cluster itself a type for compute node. | [optional] 
**infra_instance_type** | **str** | GCP default instance type for the infra volume. | [optional] 
**infra_volume** | [**GCPVolume**](GCPVolume.md) |  | [optional] 
**master_instance_type** | **str** | GCP default instance type for the master volume. | [optional] 
**master_volume** | [**GCPVolume**](GCPVolume.md) |  | [optional] 
**worker_volume** | [**GCPVolume**](GCPVolume.md) |  | [optional] 

## Example

```python
from ocm_client.models.gcp_flavour import GCPFlavour

# TODO update the JSON string below
json = "{}"
# create an instance of GCPFlavour from a JSON string
gcp_flavour_instance = GCPFlavour.from_json(json)
# print the JSON string representation of the object
print(GCPFlavour.to_json())

# convert the object into a dict
gcp_flavour_dict = gcp_flavour_instance.to_dict()
# create an instance of GCPFlavour from a dict
gcp_flavour_from_dict = GCPFlavour.from_dict(gcp_flavour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


