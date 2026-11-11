# SubnetNetworkVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;SubnetNetworkVerification&#39; if this is a complete object or &#39;SubnetNetworkVerificationLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**details** | **List[str]** | Slice of failures that happened during a subnet network verification. | [optional] 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**state** | **str** | State of the subnet network verification. | [optional] 
**tags** | **Dict[str, str]** | Tags supplied to the network verifier for this subnet. | [optional] 

## Example

```python
from ocm_client.models.subnet_network_verification import SubnetNetworkVerification

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetNetworkVerification from a JSON string
subnet_network_verification_instance = SubnetNetworkVerification.from_json(json)
# print the JSON string representation of the object
print(SubnetNetworkVerification.to_json())

# convert the object into a dict
subnet_network_verification_dict = subnet_network_verification_instance.to_dict()
# create an instance of SubnetNetworkVerification from a dict
subnet_network_verification_from_dict = SubnetNetworkVerification.from_dict(subnet_network_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


