# TokenClaimValidationRule

The rule that is applied to validate token claims to authenticate users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim** | **str** | Claim is a name of a required claim. | [optional] 
**required_value** | **str** | RequiredValue is the required value for the claim. | [optional] 

## Example

```python
from ocm_client.models.token_claim_validation_rule import TokenClaimValidationRule

# TODO update the JSON string below
json = "{}"
# create an instance of TokenClaimValidationRule from a JSON string
token_claim_validation_rule_instance = TokenClaimValidationRule.from_json(json)
# print the JSON string representation of the object
print(TokenClaimValidationRule.to_json())

# convert the object into a dict
token_claim_validation_rule_dict = token_claim_validation_rule_instance.to_dict()
# create an instance of TokenClaimValidationRule from a dict
token_claim_validation_rule_from_dict = TokenClaimValidationRule.from_dict(token_claim_validation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


