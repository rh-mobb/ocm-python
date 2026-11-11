# WifIdentityProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_audiences** | **List[str]** |  | [optional] 
**identity_provider_id** | **str** |  | [optional] 
**issuer_url** | **str** |  | [optional] 
**jwks** | **str** |  | [optional] 

## Example

```python
from ocm_client.models.wif_identity_provider import WifIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of WifIdentityProvider from a JSON string
wif_identity_provider_instance = WifIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(WifIdentityProvider.to_json())

# convert the object into a dict
wif_identity_provider_dict = wif_identity_provider_instance.to_dict()
# create an instance of WifIdentityProvider from a dict
wif_identity_provider_from_dict = WifIdentityProvider.from_dict(wif_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


