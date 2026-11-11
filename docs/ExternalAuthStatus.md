# ExternalAuthStatus

Representation of the status of an external authentication provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A descriptive message providing additional context about the current  state of the external authentication provider. | [optional] 
**state** | [**ExternalAuthState**](ExternalAuthState.md) |  | [optional] 

## Example

```python
from ocm_client.models.external_auth_status import ExternalAuthStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAuthStatus from a JSON string
external_auth_status_instance = ExternalAuthStatus.from_json(json)
# print the JSON string representation of the object
print(ExternalAuthStatus.to_json())

# convert the object into a dict
external_auth_status_dict = external_auth_status_instance.to_dict()
# create an instance of ExternalAuthStatus from a dict
external_auth_status_from_dict = ExternalAuthStatus.from_dict(external_auth_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


