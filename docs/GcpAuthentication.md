# GcpAuthentication

Google cloud platform authentication method of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Self link | [optional] 
**id** | **str** | Unique identifier of the object | [optional] 
**kind** | **str** | Indicates the type of this object | [optional] 

## Example

```python
from ocm_client.models.gcp_authentication import GcpAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of GcpAuthentication from a JSON string
gcp_authentication_instance = GcpAuthentication.from_json(json)
# print the JSON string representation of the object
print(GcpAuthentication.to_json())

# convert the object into a dict
gcp_authentication_dict = gcp_authentication_instance.to_dict()
# create an instance of GcpAuthentication from a dict
gcp_authentication_from_dict = GcpAuthentication.from_dict(gcp_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


