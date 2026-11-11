# LDAPAttributes

LDAP attributes used to configure the LDAP identity provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[str]** | List of attributes to use as the identity. | [optional] 
**email** | **List[str]** | List of attributes to use as the mail address. | [optional] 
**name** | **List[str]** | List of attributes to use as the display name. | [optional] 
**preferred_username** | **List[str]** | List of attributes to use as the preferred user name when provisioning a user. | [optional] 

## Example

```python
from ocm_client.models.ldap_attributes import LDAPAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPAttributes from a JSON string
ldap_attributes_instance = LDAPAttributes.from_json(json)
# print the JSON string representation of the object
print(LDAPAttributes.to_json())

# convert the object into a dict
ldap_attributes_dict = ldap_attributes_instance.to_dict()
# create an instance of LDAPAttributes from a dict
ldap_attributes_from_dict = LDAPAttributes.from_dict(ldap_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


