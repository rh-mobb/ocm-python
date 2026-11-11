# SdnToOvnClusterMigration

Details for `SdnToOvn` cluster migrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**join_ipv4** | **str** | The IP address range to use for the internalJoinSubnet parameter of OVN-Kubernetes upon migration. | [optional] 
**masquerade_ipv4** | **str** | The IP address range to us for the internalMasqueradeSubnet parameter of OVN-Kubernetes upon migration. | [optional] 
**transit_ipv4** | **str** | The IP address range to use for the internalTransSwitchSubnet parameter of OVN-Kubernetes upon migration. | [optional] 

## Example

```python
from ocm_client.models.sdn_to_ovn_cluster_migration import SdnToOvnClusterMigration

# TODO update the JSON string below
json = "{}"
# create an instance of SdnToOvnClusterMigration from a JSON string
sdn_to_ovn_cluster_migration_instance = SdnToOvnClusterMigration.from_json(json)
# print the JSON string representation of the object
print(SdnToOvnClusterMigration.to_json())

# convert the object into a dict
sdn_to_ovn_cluster_migration_dict = sdn_to_ovn_cluster_migration_instance.to_dict()
# create an instance of SdnToOvnClusterMigration from a dict
sdn_to_ovn_cluster_migration_from_dict = SdnToOvnClusterMigration.from_dict(sdn_to_ovn_cluster_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


