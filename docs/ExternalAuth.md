# ExternalAuth

Representation of an external authentication provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ExternalAuth&#39; if this is a complete object or &#39;ExternalAuthLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**claim** | [**ExternalAuthClaim**](ExternalAuthClaim.md) |  | [optional] 
**clients** | [**List[ExternalAuthClientConfig]**](ExternalAuthClientConfig.md) | The list of the platform&#39;s clients that need to request tokens from the issuer. | [optional] 
**issuer** | [**TokenIssuer**](TokenIssuer.md) |  | [optional] 
**status** | [**ExternalAuthStatus**](ExternalAuthStatus.md) |  | [optional] 

## Example

```python
from ocm_client.models.external_auth import ExternalAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAuth from a JSON string
external_auth_instance = ExternalAuth.from_json(json)
# print the JSON string representation of the object
print(ExternalAuth.to_json())

# convert the object into a dict
external_auth_dict = external_auth_instance.to_dict()
# create an instance of ExternalAuth from a dict
external_auth_from_dict = ExternalAuth.from_dict(external_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


