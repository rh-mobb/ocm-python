# WifServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_method** | [**WifAccessMethod**](WifAccessMethod.md) |  | [optional] 
**credential_request** | [**WifCredentialRequest**](WifCredentialRequest.md) |  | [optional] 
**osd_role** | **str** |  | [optional] 
**roles** | [**List[WifRole]**](WifRole.md) |  | [optional] 
**service_account_id** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.wif_service_account import WifServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of WifServiceAccount from a JSON string
wif_service_account_instance = WifServiceAccount.from_json(json)
# print the JSON string representation of the object
print(WifServiceAccount.to_json())

# convert the object into a dict
wif_service_account_dict = wif_service_account_instance.to_dict()
# create an instance of WifServiceAccount from a dict
wif_service_account_from_dict = WifServiceAccount.from_dict(wif_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


