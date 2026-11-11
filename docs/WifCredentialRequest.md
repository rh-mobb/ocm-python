# WifCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_ref** | [**WifSecretRef**](WifSecretRef.md) |  | [optional] 
**service_account_names** | **List[str]** |  | [optional] 

## Example

```python
from ocm_client.models.wif_credential_request import WifCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WifCredentialRequest from a JSON string
wif_credential_request_instance = WifCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(WifCredentialRequest.to_json())

# convert the object into a dict
wif_credential_request_dict = wif_credential_request_instance.to_dict()
# create an instance of WifCredentialRequest from a dict
wif_credential_request_from_dict = WifCredentialRequest.from_dict(wif_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


