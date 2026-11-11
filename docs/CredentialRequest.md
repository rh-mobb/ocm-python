# CredentialRequest

Contains the necessary attributes to allow each operator to access the necessary AWS resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credentials secret used to access cloud resources | [optional] 
**namespace** | **str** | Namespace where the credentials secret lives in the cluster | [optional] 
**policy_permissions** | **List[str]** | List of policy permissions needed to access cloud resources | [optional] 
**service_account** | **str** | Service account name to use when authenticating | [optional] 

## Example

```python
from ocm_client.models.credential_request import CredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialRequest from a JSON string
credential_request_instance = CredentialRequest.from_json(json)
# print the JSON string representation of the object
print(CredentialRequest.to_json())

# convert the object into a dict
credential_request_dict = credential_request_instance.to_dict()
# create an instance of CredentialRequest from a dict
credential_request_from_dict = CredentialRequest.from_dict(credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


