# GcpDnsDomain

GcpDnsDomain represents configuration for Google Cloud Platform DNS domain settings used in cluster DNS configuration for GCP-hosted clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_prefix** | **str** | DomainPrefix specifies the DNS domain prefix that will be used for cluster DNS resolution. This prefix is combined with the base domain to form the full DNS domain for the cluster. | [optional] 
**network_id** | **str** | NetworkId is the GCP VPC Network identifier where the DNS configuration will be applied. | [optional] 
**project_id** | **str** | ProjectId is the Google Cloud Platform project identifier where the DNS zone is hosted. | [optional] 

## Example

```python
from ocm_client.models.gcp_dns_domain import GcpDnsDomain

# TODO update the JSON string below
json = "{}"
# create an instance of GcpDnsDomain from a JSON string
gcp_dns_domain_instance = GcpDnsDomain.from_json(json)
# print the JSON string representation of the object
print(GcpDnsDomain.to_json())

# convert the object into a dict
gcp_dns_domain_dict = gcp_dns_domain_instance.to_dict()
# create an instance of GcpDnsDomain from a dict
gcp_dns_domain_from_dict = GcpDnsDomain.from_dict(gcp_dns_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


