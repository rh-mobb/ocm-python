# TokenClaimMappings

The claim mappings defined for users and groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**GroupsClaim**](GroupsClaim.md) |  | [optional] 
**username** | [**UsernameClaim**](UsernameClaim.md) |  | [optional] 

## Example

```python
from ocm_client.models.token_claim_mappings import TokenClaimMappings

# TODO update the JSON string below
json = "{}"
# create an instance of TokenClaimMappings from a JSON string
token_claim_mappings_instance = TokenClaimMappings.from_json(json)
# print the JSON string representation of the object
print(TokenClaimMappings.to_json())

# convert the object into a dict
token_claim_mappings_dict = token_claim_mappings_instance.to_dict()
# create an instance of TokenClaimMappings from a dict
token_claim_mappings_from_dict = TokenClaimMappings.from_dict(token_claim_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


