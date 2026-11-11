# GCPMachinePool

Representation of gcp machine pool specific parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secure_boot** | **bool** | Determines whether the Shielded VM&#39;s SecureBoot feature should be enabled for the nodes of the machine pool. If SecureBoot is not specified, the value of this attribute will remain unspecified and the SecureBoot&#39;s value specified in the &#x60;.gcp.security.secure_boot&#x60; attribute of the parent Cluster will be the one applied to the nodes of the machine pool. Immutable. | [optional] 

## Example

```python
from ocm_client.models.gcp_machine_pool import GCPMachinePool

# TODO update the JSON string below
json = "{}"
# create an instance of GCPMachinePool from a JSON string
gcp_machine_pool_instance = GCPMachinePool.from_json(json)
# print the JSON string representation of the object
print(GCPMachinePool.to_json())

# convert the object into a dict
gcp_machine_pool_dict = gcp_machine_pool_instance.to_dict()
# create an instance of GCPMachinePool from a dict
gcp_machine_pool_from_dict = GCPMachinePool.from_dict(gcp_machine_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


