# ExternalAuthState

Representation of the state of an external authentication provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_timestamp** | **datetime** | The date and time when the external authentication provider state was last updated. | [optional] 
**value** | **str** | A string value representing the external authentication provider&#39;s current state. | [optional] 

## Example

```python
from ocm_client.models.external_auth_state import ExternalAuthState

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAuthState from a JSON string
external_auth_state_instance = ExternalAuthState.from_json(json)
# print the JSON string representation of the object
print(ExternalAuthState.to_json())

# convert the object into a dict
external_auth_state_dict = external_auth_state_instance.to_dict()
# create an instance of ExternalAuthState from a dict
external_auth_state_from_dict = ExternalAuthState.from_dict(external_auth_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


