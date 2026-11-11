# ExternalAuthConfig

Represents an external authentication configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ExternalAuthConfig&#39; if this is a complete object or &#39;ExternalAuthConfigLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**enabled** | **bool** | Boolean flag indicating if the cluster should use an external authentication configuration for ROSA HCP clusters.  By default this is false.  To enable it the cluster needs to be ROSA HCP cluster and the organization of the user needs to have the &#x60;external-authentication&#x60; feature toggle enabled.  For ARO HCP clusters, use the \&quot;State\&quot; property to enable/disable this feature instead. | [optional] 
**external_auths** | [**List[ExternalAuth]**](ExternalAuth.md) | A list of external authentication providers configured for the cluster.  Only one external authentication provider can be configured. | [optional] 
**state** | [**ExternalAuthConfigState**](ExternalAuthConfigState.md) |  | [optional] 

## Example

```python
from ocm_client.models.external_auth_config import ExternalAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAuthConfig from a JSON string
external_auth_config_instance = ExternalAuthConfig.from_json(json)
# print the JSON string representation of the object
print(ExternalAuthConfig.to_json())

# convert the object into a dict
external_auth_config_dict = external_auth_config_instance.to_dict()
# create an instance of ExternalAuthConfig from a dict
external_auth_config_from_dict = ExternalAuthConfig.from_dict(external_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


