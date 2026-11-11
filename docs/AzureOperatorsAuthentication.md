# AzureOperatorsAuthentication

The configuration that the operators of the cluster have to authenticate to Azure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_identities** | [**AzureOperatorsAuthenticationManagedIdentities**](AzureOperatorsAuthenticationManagedIdentities.md) |  | [optional] 

## Example

```python
from ocm_client.models.azure_operators_authentication import AzureOperatorsAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of AzureOperatorsAuthentication from a JSON string
azure_operators_authentication_instance = AzureOperatorsAuthentication.from_json(json)
# print the JSON string representation of the object
print(AzureOperatorsAuthentication.to_json())

# convert the object into a dict
azure_operators_authentication_dict = azure_operators_authentication_instance.to_dict()
# create an instance of AzureOperatorsAuthentication from a dict
azure_operators_authentication_from_dict = AzureOperatorsAuthentication.from_dict(azure_operators_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


