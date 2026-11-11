# STSCredentialRequest

Representation of an credRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of CredRequest | [optional] 
**operator** | [**STSOperator**](STSOperator.md) |  | [optional] 

## Example

```python
from ocm_client.models.sts_credential_request import STSCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of STSCredentialRequest from a JSON string
sts_credential_request_instance = STSCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(STSCredentialRequest.to_json())

# convert the object into a dict
sts_credential_request_dict = sts_credential_request_instance.to_dict()
# create an instance of STSCredentialRequest from a dict
sts_credential_request_from_dict = STSCredentialRequest.from_dict(sts_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


