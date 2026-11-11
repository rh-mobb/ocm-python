# CIDRBlockAccess

Describes the CIDR Block access policy to the Kubernetes API server. Currently, only supported for ARO-HCP based clusters. The default policy mode is \"allow_all\" that is, all access is allowed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | [**CIDRBlockAllowAccess**](CIDRBlockAllowAccess.md) |  | [optional] 

## Example

```python
from ocm_client.models.cidr_block_access import CIDRBlockAccess

# TODO update the JSON string below
json = "{}"
# create an instance of CIDRBlockAccess from a JSON string
cidr_block_access_instance = CIDRBlockAccess.from_json(json)
# print the JSON string representation of the object
print(CIDRBlockAccess.to_json())

# convert the object into a dict
cidr_block_access_dict = cidr_block_access_instance.to_dict()
# create an instance of CIDRBlockAccess from a dict
cidr_block_access_from_dict = CIDRBlockAccess.from_dict(cidr_block_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


