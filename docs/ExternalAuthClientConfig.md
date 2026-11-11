# ExternalAuthClientConfig

ExternalAuthClientConfig contains configuration for the platform's clients that need to request tokens from the issuer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the OIDC client from the OIDC provider. This is required. Must be at least one character length. | [optional] 
**component** | [**ClientComponent**](ClientComponent.md) |  | [optional] 
**extra_scopes** | **List[str]** | ExtraScopes is an optional set of scopes to request tokens with. | [optional] 
**secret** | **str** | The secret of the OIDC client from the OIDC provider. The client is considered &#39;public&#39; if no secret is specified. Otherwise, it is considered as a &#39;confidential&#39; client. This can only be used for an external authentication provider belonging to a ROSA HCP cluster. | [optional] 
**type** | [**ExternalAuthClientType**](ExternalAuthClientType.md) |  | [optional] 

## Example

```python
from ocm_client.models.external_auth_client_config import ExternalAuthClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAuthClientConfig from a JSON string
external_auth_client_config_instance = ExternalAuthClientConfig.from_json(json)
# print the JSON string representation of the object
print(ExternalAuthClientConfig.to_json())

# convert the object into a dict
external_auth_client_config_dict = external_auth_client_config_instance.to_dict()
# create an instance of ExternalAuthClientConfig from a dict
external_auth_client_config_from_dict = ExternalAuthClientConfig.from_dict(external_auth_client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


