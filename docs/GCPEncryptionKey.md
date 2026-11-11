# GCPEncryptionKey

GCP Encryption Key for CCS clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_service_account** | **str** | Service account used to access the KMS key | [optional] 
**key_location** | **str** | Location of the encryption key ring | [optional] 
**key_name** | **str** | Name of the encryption key | [optional] 
**key_ring** | **str** | Name of the key ring the encryption key is located on | [optional] 

## Example

```python
from ocm_client.models.gcp_encryption_key import GCPEncryptionKey

# TODO update the JSON string below
json = "{}"
# create an instance of GCPEncryptionKey from a JSON string
gcp_encryption_key_instance = GCPEncryptionKey.from_json(json)
# print the JSON string representation of the object
print(GCPEncryptionKey.to_json())

# convert the object into a dict
gcp_encryption_key_dict = gcp_encryption_key_instance.to_dict()
# create an instance of GCPEncryptionKey from a dict
gcp_encryption_key_from_dict = GCPEncryptionKey.from_dict(gcp_encryption_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


