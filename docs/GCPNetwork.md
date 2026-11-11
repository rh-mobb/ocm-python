# GCPNetwork

GCP Network configuration of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_name** | **str** | VPC mame used by the cluster. | [optional] 
**vpc_project_id** | **str** | The name of the host project where the shared VPC exists. | [optional] 
**compute_subnet** | **str** | Compute subnet used by the cluster. | [optional] 
**control_plane_subnet** | **str** | Control plane subnet used by the cluster. | [optional] 
**firewall_rules_id** | **str** | ID of the GCP firewall rule set associated with this cluster. | [optional] 

## Example

```python
from ocm_client.models.gcp_network import GCPNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of GCPNetwork from a JSON string
gcp_network_instance = GCPNetwork.from_json(json)
# print the JSON string representation of the object
print(GCPNetwork.to_json())

# convert the object into a dict
gcp_network_dict = gcp_network_instance.to_dict()
# create an instance of GCPNetwork from a dict
gcp_network_from_dict = GCPNetwork.from_dict(gcp_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


