# CloudProviderData

Description of a cloud provider data used for cloud provider inquiries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**AWS**](AWS.md) |  | [optional] 
**gcp** | [**GCP**](GCP.md) |  | [optional] 
**availability_zones** | **List[str]** | Availability zone | [optional] 
**key_location** | **str** | Key location | [optional] 
**key_ring_name** | **str** | Key ring name | [optional] 
**region** | [**CloudRegion**](CloudRegion.md) |  | [optional] 
**subnets** | **List[str]** | Subnets | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**vpc_ids** | **List[str]** | VPC ids | [optional] 

## Example

```python
from ocm_client.models.cloud_provider_data import CloudProviderData

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProviderData from a JSON string
cloud_provider_data_instance = CloudProviderData.from_json(json)
# print the JSON string representation of the object
print(CloudProviderData.to_json())

# convert the object into a dict
cloud_provider_data_dict = cloud_provider_data_instance.to_dict()
# create an instance of CloudProviderData from a dict
cloud_provider_data_from_dict = CloudProviderData.from_dict(cloud_provider_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


