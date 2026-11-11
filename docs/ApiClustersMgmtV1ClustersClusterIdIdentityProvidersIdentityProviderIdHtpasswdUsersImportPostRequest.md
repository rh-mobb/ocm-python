# ApiClustersMgmtV1ClustersClusterIdIdentityProvidersIdentityProviderIdHtpasswdUsersImportPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HTPasswdUser]**](HTPasswdUser.md) | List of users to add to the IDP. | [optional] 
**page** | **int** | Index of the requested page, where one corresponds to the first page. | [optional] 
**size** | **int** | Number of items contained in the returned page. | [optional] 

## Example

```python
from ocm_client.models.api_clusters_mgmt_v1_clusters_cluster_id_identity_providers_identity_provider_id_htpasswd_users_import_post_request import ApiClustersMgmtV1ClustersClusterIdIdentityProvidersIdentityProviderIdHtpasswdUsersImportPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClustersMgmtV1ClustersClusterIdIdentityProvidersIdentityProviderIdHtpasswdUsersImportPostRequest from a JSON string
api_clusters_mgmt_v1_clusters_cluster_id_identity_providers_identity_provider_id_htpasswd_users_import_post_request_instance = ApiClustersMgmtV1ClustersClusterIdIdentityProvidersIdentityProviderIdHtpasswdUsersImportPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiClustersMgmtV1ClustersClusterIdIdentityProvidersIdentityProviderIdHtpasswdUsersImportPostRequest.to_json())

# convert the object into a dict
api_clusters_mgmt_v1_clusters_cluster_id_identity_providers_identity_provider_id_htpasswd_users_import_post_request_dict = api_clusters_mgmt_v1_clusters_cluster_id_identity_providers_identity_provider_id_htpasswd_users_import_post_request_instance.to_dict()
# create an instance of ApiClustersMgmtV1ClustersClusterIdIdentityProvidersIdentityProviderIdHtpasswdUsersImportPostRequest from a dict
api_clusters_mgmt_v1_clusters_cluster_id_identity_providers_identity_provider_id_htpasswd_users_import_post_request_from_dict = ApiClustersMgmtV1ClustersClusterIdIdentityProvidersIdentityProviderIdHtpasswdUsersImportPostRequest.from_dict(api_clusters_mgmt_v1_clusters_cluster_id_identity_providers_identity_provider_id_htpasswd_users_import_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


