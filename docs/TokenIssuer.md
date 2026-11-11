# TokenIssuer

Representation of a token issuer used in an external authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | Certificate bundle to use to validate server certificates for the configured URL. | [optional] 
**url** | **str** | URL is the serving URL of the token issuer. It must be a valid url and use the &#39;https&#39; scheme. This is required. | [optional] 
**audiences** | **List[str]** | Audiences is an array of audiences that the token was issued for. Valid tokens must include at least one of these values in their \&quot;aud\&quot; claim. Must have at least one audience and a maximum of ten. Any clients defined for this external authentication must have their id included here. | [optional] 

## Example

```python
from ocm_client.models.token_issuer import TokenIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of TokenIssuer from a JSON string
token_issuer_instance = TokenIssuer.from_json(json)
# print the JSON string representation of the object
print(TokenIssuer.to_json())

# convert the object into a dict
token_issuer_dict = token_issuer_instance.to_dict()
# create an instance of TokenIssuer from a dict
token_issuer_from_dict = TokenIssuer.from_dict(token_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


