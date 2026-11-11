# AzureKmsEncryption

Contains the necessary attributes to support KMS encryption for Azure based clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_key** | [**AzureKmsKey**](AzureKmsKey.md) |  | [optional] 

## Example

```python
from ocm_client.models.azure_kms_encryption import AzureKmsEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKmsEncryption from a JSON string
azure_kms_encryption_instance = AzureKmsEncryption.from_json(json)
# print the JSON string representation of the object
print(AzureKmsEncryption.to_json())

# convert the object into a dict
azure_kms_encryption_dict = azure_kms_encryption_instance.to_dict()
# create an instance of AzureKmsEncryption from a dict
azure_kms_encryption_from_dict = AzureKmsEncryption.from_dict(azure_kms_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


