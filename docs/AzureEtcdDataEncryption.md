# AzureEtcdDataEncryption

Contains the necessary attributes to support data encryption for Azure based clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_managed** | [**AzureEtcdDataEncryptionCustomerManaged**](AzureEtcdDataEncryptionCustomerManaged.md) |  | [optional] 
**key_management_mode** | **str** | The key management strategy used for the encryption key that encrypts the etcd data. Accepted values are: \&quot;customer_managed\&quot;, \&quot;platform_managed\&quot;. By default, \&quot;platform_managed\&quot; is used. Currently only \&quot;customer_managed\&quot; mode is supported. | [optional] 

## Example

```python
from ocm_client.models.azure_etcd_data_encryption import AzureEtcdDataEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of AzureEtcdDataEncryption from a JSON string
azure_etcd_data_encryption_instance = AzureEtcdDataEncryption.from_json(json)
# print the JSON string representation of the object
print(AzureEtcdDataEncryption.to_json())

# convert the object into a dict
azure_etcd_data_encryption_dict = azure_etcd_data_encryption_instance.to_dict()
# create an instance of AzureEtcdDataEncryption from a dict
azure_etcd_data_encryption_from_dict = AzureEtcdDataEncryption.from_dict(azure_etcd_data_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


