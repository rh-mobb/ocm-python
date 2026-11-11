# OidcThumbprintInput

Contains the necessary attributes to fetch an OIDC Configuration thumbprint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | ClusterId is the for the cluster used, exclusive from OidcConfigId. | [optional] 
**oidc_config_id** | **str** | OidcConfigId is the ID for the oidc config used, exclusive from ClusterId. | [optional] 

## Example

```python
from ocm_client.models.oidc_thumbprint_input import OidcThumbprintInput

# TODO update the JSON string below
json = "{}"
# create an instance of OidcThumbprintInput from a JSON string
oidc_thumbprint_input_instance = OidcThumbprintInput.from_json(json)
# print the JSON string representation of the object
print(OidcThumbprintInput.to_json())

# convert the object into a dict
oidc_thumbprint_input_dict = oidc_thumbprint_input_instance.to_dict()
# create an instance of OidcThumbprintInput from a dict
oidc_thumbprint_input_from_dict = OidcThumbprintInput.from_dict(oidc_thumbprint_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


