# GCP

Google cloud platform settings of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_uri** | **str** | GCP authentication uri | [optional] 
**auth_provider_x509_cert_url** | **str** | GCP Authentication provider x509 certificate url | [optional] 
**authentication** | [**GcpAuthentication**](GcpAuthentication.md) |  | [optional] 
**client_id** | **str** | GCP client identifier | [optional] 
**client_x509_cert_url** | **str** | GCP client x509 certificate url | [optional] 
**client_email** | **str** | GCP client email | [optional] 
**private_key** | **str** | GCP private key | [optional] 
**private_key_id** | **str** | GCP private key identifier | [optional] 
**private_service_connect** | [**GcpPrivateServiceConnect**](GcpPrivateServiceConnect.md) |  | [optional] 
**project_id** | **str** | GCP project identifier. | [optional] 
**security** | [**GcpSecurity**](GcpSecurity.md) |  | [optional] 
**token_uri** | **str** | GCP token uri | [optional] 
**type** | **str** | GCP the type of the service the key belongs to | [optional] 

## Example

```python
from ocm_client.models.gcp import GCP

# TODO update the JSON string below
json = "{}"
# create an instance of GCP from a JSON string
gcp_instance = GCP.from_json(json)
# print the JSON string representation of the object
print(GCP.to_json())

# convert the object into a dict
gcp_dict = gcp_instance.to_dict()
# create an instance of GCP from a dict
gcp_from_dict = GCP.from_dict(gcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


