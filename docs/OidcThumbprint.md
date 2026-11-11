# OidcThumbprint

Contains the necessary attributes to support oidc configuration thumbprint operations such as fetching/creation of a thumbprint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | HREF for the oidc config thumbprint, filled in response. | [optional] 
**cluster_id** | **str** | ClusterId is the for the cluster used, filled in response. | [optional] 
**kind** | **str** | Kind is the resource type, filled in response. | [optional] 
**oidc_config_id** | **str** | OidcConfigId is the ID for the oidc config used, filled in response. | [optional] 
**thumbprint** | **str** | Thumbprint is the thumbprint itself, filled in response. | [optional] 

## Example

```python
from ocm_client.models.oidc_thumbprint import OidcThumbprint

# TODO update the JSON string below
json = "{}"
# create an instance of OidcThumbprint from a JSON string
oidc_thumbprint_instance = OidcThumbprint.from_json(json)
# print the JSON string representation of the object
print(OidcThumbprint.to_json())

# convert the object into a dict
oidc_thumbprint_dict = oidc_thumbprint_instance.to_dict()
# create an instance of OidcThumbprint from a dict
oidc_thumbprint_from_dict = OidcThumbprint.from_dict(oidc_thumbprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


