# GroupsClaim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim** | **str** | The claim used in the token. | [optional] 
**prefix** | **str** | A prefix contatenated in the claim (Optional). | [optional] 

## Example

```python
from ocm_client.models.groups_claim import GroupsClaim

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsClaim from a JSON string
groups_claim_instance = GroupsClaim.from_json(json)
# print the JSON string representation of the object
print(GroupsClaim.to_json())

# convert the object into a dict
groups_claim_dict = groups_claim_instance.to_dict()
# create an instance of GroupsClaim from a dict
groups_claim_from_dict = GroupsClaim.from_dict(groups_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


