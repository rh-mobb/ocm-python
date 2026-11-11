# GithubIdentityProvider

Details for `github` identity providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | Optional trusted certificate authority bundle to use when making requests tot he server. | [optional] 
**client_id** | **str** | Client identifier of a registered _GitHub_ OAuth application. | [optional] 
**client_secret** | **str** | Client secret of a registered _GitHub_ OAuth application. | [optional] 
**hostname** | **str** | For _GitHub Enterprise_ you must provide the host name of your instance, such as &#x60;example.com&#x60;. This value must match the _GitHub Enterprise_ host name value in the &#x60;/setup/settings&#x60; file and cannot include a port number.  For plain _GitHub_ omit this parameter. | [optional] 
**organizations** | **List[str]** | Optional list of organizations. Cannot be used in combination with the Teams field. | [optional] 
**teams** | **List[str]** | Optional list of teams. Cannot be used in combination with the Organizations field. | [optional] 

## Example

```python
from ocm_client.models.github_identity_provider import GithubIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of GithubIdentityProvider from a JSON string
github_identity_provider_instance = GithubIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(GithubIdentityProvider.to_json())

# convert the object into a dict
github_identity_provider_dict = github_identity_provider_instance.to_dict()
# create an instance of GithubIdentityProvider from a dict
github_identity_provider_from_dict = GithubIdentityProvider.from_dict(github_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


