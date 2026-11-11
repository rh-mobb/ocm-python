# Subnetwork

AWS subnetwork object to be used while installing a cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_block** | **str** | The CIDR Block of the subnet. | [optional] 
**availability_zone** | **str** | The availability zone to which the subnet is related. | [optional] 
**name** | **str** | Name of the subnet according to its &#x60;Name&#x60; tag on AWS. | [optional] 
**public** | **bool** | Whether or not it is a public subnet. | [optional] 
**red_hat_managed** | **bool** | If the resource is RH managed. | [optional] 
**subnet_id** | **str** | The subnet ID to be used while installing a cluster. | [optional] 

## Example

```python
from ocm_client.models.subnetwork import Subnetwork

# TODO update the JSON string below
json = "{}"
# create an instance of Subnetwork from a JSON string
subnetwork_instance = Subnetwork.from_json(json)
# print the JSON string representation of the object
print(Subnetwork.to_json())

# convert the object into a dict
subnetwork_dict = subnetwork_instance.to_dict()
# create an instance of Subnetwork from a dict
subnetwork_from_dict = Subnetwork.from_dict(subnetwork_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


