# GcpSecurity

Google cloud platform security settings of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secure_boot** | **bool** | Determines if Shielded VM feature \&quot;Secure Boot\&quot; should be set for the nodes of the cluster. | [optional] 

## Example

```python
from ocm_client.models.gcp_security import GcpSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSecurity from a JSON string
gcp_security_instance = GcpSecurity.from_json(json)
# print the JSON string representation of the object
print(GcpSecurity.to_json())

# convert the object into a dict
gcp_security_dict = gcp_security_instance.to_dict()
# create an instance of GcpSecurity from a dict
gcp_security_from_dict = GcpSecurity.from_dict(gcp_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


