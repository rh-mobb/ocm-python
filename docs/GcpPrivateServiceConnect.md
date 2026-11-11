# GcpPrivateServiceConnect

Google cloud platform private service connect configuration of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_attachment_subnet** | **str** | The name of the subnet where the PSC service attachment is created | [optional] 

## Example

```python
from ocm_client.models.gcp_private_service_connect import GcpPrivateServiceConnect

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPrivateServiceConnect from a JSON string
gcp_private_service_connect_instance = GcpPrivateServiceConnect.from_json(json)
# print the JSON string representation of the object
print(GcpPrivateServiceConnect.to_json())

# convert the object into a dict
gcp_private_service_connect_dict = gcp_private_service_connect_instance.to_dict()
# create an instance of GcpPrivateServiceConnect from a dict
gcp_private_service_connect_from_dict = GcpPrivateServiceConnect.from_dict(gcp_private_service_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


