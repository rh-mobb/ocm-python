# AzureEtcdEncryption

Contains the necessary attributes to support etcd encryption for Azure based clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_encryption** | [**AzureEtcdDataEncryption**](AzureEtcdDataEncryption.md) |  | [optional] 

## Example

```python
from ocm_client.models.azure_etcd_encryption import AzureEtcdEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of AzureEtcdEncryption from a JSON string
azure_etcd_encryption_instance = AzureEtcdEncryption.from_json(json)
# print the JSON string representation of the object
print(AzureEtcdEncryption.to_json())

# convert the object into a dict
azure_etcd_encryption_dict = azure_etcd_encryption_instance.to_dict()
# create an instance of AzureEtcdEncryption from a dict
azure_etcd_encryption_from_dict = AzureEtcdEncryption.from_dict(azure_etcd_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


