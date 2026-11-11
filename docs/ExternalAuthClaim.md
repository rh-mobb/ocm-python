# ExternalAuthClaim

The claims and validation rules used in the configuration of the external authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**TokenClaimMappings**](TokenClaimMappings.md) |  | [optional] 
**validation_rules** | [**List[TokenClaimValidationRule]**](TokenClaimValidationRule.md) | ValidationRules are rules that are applied to validate token claims to authenticate users. | [optional] 

## Example

```python
from ocm_client.models.external_auth_claim import ExternalAuthClaim

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAuthClaim from a JSON string
external_auth_claim_instance = ExternalAuthClaim.from_json(json)
# print the JSON string representation of the object
print(ExternalAuthClaim.to_json())

# convert the object into a dict
external_auth_claim_dict = external_auth_claim_instance.to_dict()
# create an instance of ExternalAuthClaim from a dict
external_auth_claim_from_dict = ExternalAuthClaim.from_dict(external_auth_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


