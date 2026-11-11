# BreakGlassCredential

Representation of a break glass credential.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;BreakGlassCredential&#39; if this is a complete object or &#39;BreakGlassCredentialLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**expiration_timestamp** | **datetime** | ExpirationTimestamp is the date and time when the credential will expire. | [optional] 
**kubeconfig** | **str** | Kubeconfig is the generated kubeconfig for this credential. It is only stored in memory | [optional] 
**revocation_timestamp** | **datetime** | RevocationTimestamp is the date and time when the credential has been revoked. | [optional] 
**status** | [**BreakGlassCredentialStatus**](BreakGlassCredentialStatus.md) |  | [optional] 
**username** | **str** | Username is the user which will be used for this credential. | [optional] 

## Example

```python
from ocm_client.models.break_glass_credential import BreakGlassCredential

# TODO update the JSON string below
json = "{}"
# create an instance of BreakGlassCredential from a JSON string
break_glass_credential_instance = BreakGlassCredential.from_json(json)
# print the JSON string representation of the object
print(BreakGlassCredential.to_json())

# convert the object into a dict
break_glass_credential_dict = break_glass_credential_instance.to_dict()
# create an instance of BreakGlassCredential from a dict
break_glass_credential_from_dict = BreakGlassCredential.from_dict(break_glass_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


