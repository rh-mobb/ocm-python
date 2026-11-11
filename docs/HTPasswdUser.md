# HTPasswdUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for a secondary user in the _HTPasswd_ data file. | [optional] 
**hashed_password** | **str** | HTPasswd Hashed Password for a user in the _HTPasswd_ data file. The value of this field is set as-is in the _HTPasswd_ data file for the HTPasswd IDP | [optional] 
**password** | **str** | Password in plain-text for a  user in the _HTPasswd_ data file. The value of this field is hashed before setting it in the  _HTPasswd_ data file for the HTPasswd IDP | [optional] 
**username** | **str** | Username for a secondary user in the _HTPasswd_ data file. | [optional] 

## Example

```python
from ocm_client.models.ht_passwd_user import HTPasswdUser

# TODO update the JSON string below
json = "{}"
# create an instance of HTPasswdUser from a JSON string
ht_passwd_user_instance = HTPasswdUser.from_json(json)
# print the JSON string representation of the object
print(HTPasswdUser.to_json())

# convert the object into a dict
ht_passwd_user_dict = ht_passwd_user_instance.to_dict()
# create an instance of HTPasswdUser from a dict
ht_passwd_user_from_dict = HTPasswdUser.from_dict(ht_passwd_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


