# GitlabIdentityProvider

Details for `gitlab` identity providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | Optional trusted certificate authority bundle to use when making requests tot he server. | [optional] 
**url** | **str** | URL of the _GitLab_ instance. | [optional] 
**client_id** | **str** | Client identifier of a registered _GitLab_ OAuth application. | [optional] 
**client_secret** | **str** | Client secret issued by _GitLab_. | [optional] 

## Example

```python
from ocm_client.models.gitlab_identity_provider import GitlabIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of GitlabIdentityProvider from a JSON string
gitlab_identity_provider_instance = GitlabIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(GitlabIdentityProvider.to_json())

# convert the object into a dict
gitlab_identity_provider_dict = gitlab_identity_provider_instance.to_dict()
# create an instance of GitlabIdentityProvider from a dict
gitlab_identity_provider_from_dict = GitlabIdentityProvider.from_dict(gitlab_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


