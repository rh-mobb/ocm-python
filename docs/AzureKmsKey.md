# AzureKmsKey

Contains the necessary attributes to support KMS encryption key for Azure based clusters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | key_name is the name of the Azure Key Vault Key Required during creation. | [optional] 
**key_vault_name** | **str** | key_vault_name is the name of the Azure Key Vault that contains the encryption key Required during creation. | [optional] 
**key_version** | **str** | key_version is the version of the Azure Key Vault key Required during creation. | [optional] 

## Example

```python
from ocm_client.models.azure_kms_key import AzureKmsKey

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKmsKey from a JSON string
azure_kms_key_instance = AzureKmsKey.from_json(json)
# print the JSON string representation of the object
print(AzureKmsKey.to_json())

# convert the object into a dict
azure_kms_key_dict = azure_kms_key_instance.to_dict()
# create an instance of AzureKmsKey from a dict
azure_kms_key_from_dict = AzureKmsKey.from_dict(azure_kms_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


