# HTPasswdIdentityProvider

Details for `htpasswd` identity providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password to be used in the _HTPasswd_ data file. | [optional] 
**username** | **str** | Username to be used in the _HTPasswd_ data file. | [optional] 
**users** | [**List[HTPasswdUser]**](HTPasswdUser.md) | Link to the collection of _HTPasswd_ users. | [optional] 

## Example

```python
from ocm_client.models.ht_passwd_identity_provider import HTPasswdIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of HTPasswdIdentityProvider from a JSON string
ht_passwd_identity_provider_instance = HTPasswdIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(HTPasswdIdentityProvider.to_json())

# convert the object into a dict
ht_passwd_identity_provider_dict = ht_passwd_identity_provider_instance.to_dict()
# create an instance of HTPasswdIdentityProvider from a dict
ht_passwd_identity_provider_from_dict = HTPasswdIdentityProvider.from_dict(ht_passwd_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


