# UsernameClaim

The username claim mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim** | **str** | The claim used in the token. | [optional] 
**prefix** | **str** | A prefix contatenated in the claim (Optional). | [optional] 
**prefix_policy** | **str** | PrefixPolicy specifies how a prefix should apply.  By default, claims other than &#x60;email&#x60; will be prefixed with the issuer URL to prevent naming clashes with other plugins.  Set to \&quot;NoPrefix\&quot; to disable prefixing.  If a prefix is defined, this will be set to &#39;Prefix&#39; by default. | [optional] 

## Example

```python
from ocm_client.models.username_claim import UsernameClaim

# TODO update the JSON string below
json = "{}"
# create an instance of UsernameClaim from a JSON string
username_claim_instance = UsernameClaim.from_json(json)
# print the JSON string representation of the object
print(UsernameClaim.to_json())

# convert the object into a dict
username_claim_dict = username_claim_instance.to_dict()
# create an instance of UsernameClaim from a dict
username_claim_from_dict = UsernameClaim.from_dict(username_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


