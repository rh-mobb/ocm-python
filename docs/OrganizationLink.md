# OrganizationLink

Definition of an organization link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | HREF for the Organization, filled in response. | [optional] 
**id** | **str** | The organization&#39;s ID. | [optional] 

## Example

```python
from ocm_client.models.organization_link import OrganizationLink

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLink from a JSON string
organization_link_instance = OrganizationLink.from_json(json)
# print the JSON string representation of the object
print(OrganizationLink.to_json())

# convert the object into a dict
organization_link_dict = organization_link_instance.to_dict()
# create an instance of OrganizationLink from a dict
organization_link_from_dict = OrganizationLink.from_dict(organization_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


