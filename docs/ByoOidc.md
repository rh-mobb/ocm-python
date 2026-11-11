# ByoOidc

ByoOidc configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Boolean flag indicating if the cluster should be creating using _ByoOidc_.  By default this is &#x60;false&#x60;.  To enable it the cluster needs to be ROSA cluster and the organization of the user needs to have the &#x60;byo-oidc&#x60; feature toggle enabled. | [optional] 

## Example

```python
from ocm_client.models.byo_oidc import ByoOidc

# TODO update the JSON string below
json = "{}"
# create an instance of ByoOidc from a JSON string
byo_oidc_instance = ByoOidc.from_json(json)
# print the JSON string representation of the object
print(ByoOidc.to_json())

# convert the object into a dict
byo_oidc_dict = byo_oidc_instance.to_dict()
# create an instance of ByoOidc from a dict
byo_oidc_from_dict = ByoOidc.from_dict(byo_oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


