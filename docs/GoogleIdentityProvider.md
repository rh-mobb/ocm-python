# GoogleIdentityProvider

Details for `google` identity providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client identifier of a registered _Google_ project. | [optional] 
**client_secret** | **str** | Client secret issued by _Google_. | [optional] 
**hosted_domain** | **str** | Optional hosted domain to restrict sign-in accounts to. | [optional] 

## Example

```python
from ocm_client.models.google_identity_provider import GoogleIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleIdentityProvider from a JSON string
google_identity_provider_instance = GoogleIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(GoogleIdentityProvider.to_json())

# convert the object into a dict
google_identity_provider_dict = google_identity_provider_instance.to_dict()
# create an instance of GoogleIdentityProvider from a dict
google_identity_provider_from_dict = GoogleIdentityProvider.from_dict(google_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


