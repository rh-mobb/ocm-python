# ControlPlane

Representation of a Control Plane

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | [**Backup**](Backup.md) |  | [optional] 
**log_forwarders** | [**List[LogForwarder]**](LogForwarder.md) | Control plane log forwarders configuration. This can be set during cluster creation to configure control plane log forwarders. | [optional] 

## Example

```python
from ocm_client.models.control_plane import ControlPlane

# TODO update the JSON string below
json = "{}"
# create an instance of ControlPlane from a JSON string
control_plane_instance = ControlPlane.from_json(json)
# print the JSON string representation of the object
print(ControlPlane.to_json())

# convert the object into a dict
control_plane_dict = control_plane_instance.to_dict()
# create an instance of ControlPlane from a dict
control_plane_from_dict = ControlPlane.from_dict(control_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


