# AzureEtcdDataEncryptionCustomerManaged

Contains the necessary attributes to support etcd data encryption with customer managed keys for Azure based clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_type** | **str** | The encryption type used. Accepted values are: \&quot;kms\&quot;. By default, \&quot;kms\&quot; is used. | [optional] 
**kms** | [**AzureKmsEncryption**](AzureKmsEncryption.md) |  | [optional] 

## Example

```python
from ocm_client.models.azure_etcd_data_encryption_customer_managed import AzureEtcdDataEncryptionCustomerManaged

# TODO update the JSON string below
json = "{}"
# create an instance of AzureEtcdDataEncryptionCustomerManaged from a JSON string
azure_etcd_data_encryption_customer_managed_instance = AzureEtcdDataEncryptionCustomerManaged.from_json(json)
# print the JSON string representation of the object
print(AzureEtcdDataEncryptionCustomerManaged.to_json())

# convert the object into a dict
azure_etcd_data_encryption_customer_managed_dict = azure_etcd_data_encryption_customer_managed_instance.to_dict()
# create an instance of AzureEtcdDataEncryptionCustomerManaged from a dict
azure_etcd_data_encryption_customer_managed_from_dict = AzureEtcdDataEncryptionCustomerManaged.from_dict(azure_etcd_data_encryption_customer_managed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


