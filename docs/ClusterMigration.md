# ClusterMigration

Representation of a cluster migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ClusterMigration&#39; if this is a complete object or &#39;ClusterMigrationLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**cluster_id** | **str** | Internal cluster ID. | [optional] 
**creation_timestamp** | **datetime** | Date and time when the cluster migration was initially created, using the format defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt). | [optional] 
**sdn_to_ovn** | [**SdnToOvnClusterMigration**](SdnToOvnClusterMigration.md) |  | [optional] 
**state** | [**ClusterMigrationState**](ClusterMigrationState.md) |  | [optional] 
**type** | [**ClusterMigrationType**](ClusterMigrationType.md) |  | [optional] 
**updated_timestamp** | **datetime** | Date and time when the cluster migration was last updated, using the format defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt). | [optional] 

## Example

```python
from ocm_client.models.cluster_migration import ClusterMigration

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMigration from a JSON string
cluster_migration_instance = ClusterMigration.from_json(json)
# print the JSON string representation of the object
print(ClusterMigration.to_json())

# convert the object into a dict
cluster_migration_dict = cluster_migration_instance.to_dict()
# create an instance of ClusterMigration from a dict
cluster_migration_from_dict = ClusterMigration.from_dict(cluster_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


