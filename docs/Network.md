# Network

Network configuration of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_prefix** | **int** | Network host prefix which is defaulted to &#x60;23&#x60; if not specified. | [optional] 
**machine_cidr** | **str** | IP address block from which to assign machine IP addresses, for example &#x60;10.0.0.0/16&#x60;. | [optional] 
**pod_cidr** | **str** | IP address block from which to assign pod IP addresses, for example &#x60;10.128.0.0/14&#x60;. | [optional] 
**service_cidr** | **str** | IP address block from which to assign service IP addresses, for example &#x60;172.30.0.0/16&#x60;. | [optional] 
**type** | **str** | The main controller responsible for rendering the core networking components. | [optional] 

## Example

```python
from ocm_client.models.network import Network

# TODO update the JSON string below
json = "{}"
# create an instance of Network from a JSON string
network_instance = Network.from_json(json)
# print the JSON string representation of the object
print(Network.to_json())

# convert the object into a dict
network_dict = network_instance.to_dict()
# create an instance of Network from a dict
network_from_dict = Network.from_dict(network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


