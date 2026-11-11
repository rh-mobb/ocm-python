# TrustedIp

Representation of a trusted ip address in clusterdeployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;TrustedIp&#39; if this is a complete object or &#39;TrustedIpLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**enabled** | **bool** | The boolean set to show if the ip is enabled. | [optional] 

## Example

```python
from ocm_client.models.trusted_ip import TrustedIp

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedIp from a JSON string
trusted_ip_instance = TrustedIp.from_json(json)
# print the JSON string representation of the object
print(TrustedIp.to_json())

# convert the object into a dict
trusted_ip_dict = trusted_ip_instance.to_dict()
# create an instance of TrustedIp from a dict
trusted_ip_from_dict = TrustedIp.from_dict(trusted_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


