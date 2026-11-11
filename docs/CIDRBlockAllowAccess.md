# CIDRBlockAllowAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | There are two modes: \&quot;allow_all\&quot; and \&quot;allow_list\&quot;; if \&quot;allow_list\&quot; is provided than a non-empty &#39;values&#39; list must be provided. Otherwise, if \&quot;allow_all\&quot; is provided then &#39;values&#39; list should be omitted. | [optional] 
**values** | **List[str]** | The &#39;values&#39; list should contain a CIDR block list (An IPV4 address range in the format &#x60;&lt;ipv4_address&gt;/&lt;network_mask&gt;&#x60;).  The maximum number of CIDR blocks supported is 500. The CIDR blocks should be non-overlapping and valid. The value \&quot;0.0.0.0/0\&quot; is not considered a valid value, as the user can use \&quot;allow_all\&quot; mode to indicate this behavior. The values should not contain the set of Private IP address ranges. | [optional] 

## Example

```python
from ocm_client.models.cidr_block_allow_access import CIDRBlockAllowAccess

# TODO update the JSON string below
json = "{}"
# create an instance of CIDRBlockAllowAccess from a JSON string
cidr_block_allow_access_instance = CIDRBlockAllowAccess.from_json(json)
# print the JSON string representation of the object
print(CIDRBlockAllowAccess.to_json())

# convert the object into a dict
cidr_block_allow_access_dict = cidr_block_allow_access_instance.to_dict()
# create an instance of CIDRBlockAllowAccess from a dict
cidr_block_allow_access_from_dict = CIDRBlockAllowAccess.from_dict(cidr_block_allow_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


