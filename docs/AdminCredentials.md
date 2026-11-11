# AdminCredentials

Temporary administrator credentials generated during the installation of the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Cluster administrator password. | [optional] 
**user** | **str** | Cluster administrator user name. | [optional] 

## Example

```python
from ocm_client.models.admin_credentials import AdminCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCredentials from a JSON string
admin_credentials_instance = AdminCredentials.from_json(json)
# print the JSON string representation of the object
print(AdminCredentials.to_json())

# convert the object into a dict
admin_credentials_dict = admin_credentials_instance.to_dict()
# create an instance of AdminCredentials from a dict
admin_credentials_from_dict = AdminCredentials.from_dict(admin_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


