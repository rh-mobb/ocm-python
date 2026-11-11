# NetworkVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider_data** | [**CloudProviderData**](CloudProviderData.md) |  | [optional] 
**cluster_id** | **str** | Cluster ID needed to execute the network verification. | [optional] 
**items** | [**List[SubnetNetworkVerification]**](SubnetNetworkVerification.md) | Details about each subnet network verification. | [optional] 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**total** | **int** | Amount of network verifier executions started. | [optional] 

## Example

```python
from ocm_client.models.network_verification import NetworkVerification

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkVerification from a JSON string
network_verification_instance = NetworkVerification.from_json(json)
# print the JSON string representation of the object
print(NetworkVerification.to_json())

# convert the object into a dict
network_verification_dict = network_verification_instance.to_dict()
# create an instance of NetworkVerification from a dict
network_verification_from_dict = NetworkVerification.from_dict(network_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


