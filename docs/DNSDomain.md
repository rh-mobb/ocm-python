# DNSDomain

Contains the properties of a DNS domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;DNSDomain&#39; if this is a complete object or &#39;DNSDomainLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cloud_provider** | [**DnsCloudProvider**](DnsCloudProvider.md) |  | [optional] 
**cluster** | [**ClusterLink**](ClusterLink.md) |  | [optional] 
**cluster_arch** | [**ClusterArchitecture**](ClusterArchitecture.md) |  | [optional] 
**gcp** | [**GcpDnsDomain**](GcpDnsDomain.md) |  | [optional] 
**organization** | [**OrganizationLink**](OrganizationLink.md) |  | [optional] 
**reserved_at_timestamp** | **datetime** | Date and time when the DNS domain was reserved. | [optional] 
**user_defined** | **bool** | Indicates if this dns domain is user defined. | [optional] 

## Example

```python
from ocm_client.models.dns_domain import DNSDomain

# TODO update the JSON string below
json = "{}"
# create an instance of DNSDomain from a JSON string
dns_domain_instance = DNSDomain.from_json(json)
# print the JSON string representation of the object
print(DNSDomain.to_json())

# convert the object into a dict
dns_domain_dict = dns_domain_instance.to_dict()
# create an instance of DNSDomain from a dict
dns_domain_from_dict = DNSDomain.from_dict(dns_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


