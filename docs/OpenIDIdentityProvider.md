# OpenIDIdentityProvider

Details for `openid` identity providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | Certificate bunde to use to validate server certificates for the configured URL. | [optional] 
**claims** | [**OpenIDClaims**](OpenIDClaims.md) |  | [optional] 
**client_id** | **str** | Identifier of a client registered with the _OpenID_ provider. | [optional] 
**client_secret** | **str** | Client secret. | [optional] 
**extra_authorize_parameters** | **Dict[str, str]** | Optional map of extra parameters to add to the authorization token request. | [optional] 
**extra_scopes** | **List[str]** | Optional list of scopes to request, in addition to the &#x60;openid&#x60; scope, during the authorization token request. | [optional] 
**issuer** | **str** | The URL that the OpenID Provider asserts as the Issuer Identifier | [optional] 

## Example

```python
from ocm_client.models.open_id_identity_provider import OpenIDIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIDIdentityProvider from a JSON string
open_id_identity_provider_instance = OpenIDIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(OpenIDIdentityProvider.to_json())

# convert the object into a dict
open_id_identity_provider_dict = open_id_identity_provider_instance.to_dict()
# create an instance of OpenIDIdentityProvider from a dict
open_id_identity_provider_from_dict = OpenIDIdentityProvider.from_dict(open_id_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


