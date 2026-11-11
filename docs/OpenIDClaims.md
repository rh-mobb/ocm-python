# OpenIDClaims

_OpenID_ identity provider claims.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **List[str]** | List of claims to use as the mail address. | [optional] 
**groups** | **List[str]** | List of claims to use as the group name. | [optional] 
**name** | **List[str]** | List of claims to use as the display name. | [optional] 
**preferred_username** | **List[str]** | List of claims to use as the preferred user name when provisioning a user. | [optional] 

## Example

```python
from ocm_client.models.open_id_claims import OpenIDClaims

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIDClaims from a JSON string
open_id_claims_instance = OpenIDClaims.from_json(json)
# print the JSON string representation of the object
print(OpenIDClaims.to_json())

# convert the object into a dict
open_id_claims_dict = open_id_claims_instance.to_dict()
# create an instance of OpenIDClaims from a dict
open_id_claims_from_dict = OpenIDClaims.from_dict(open_id_claims_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


