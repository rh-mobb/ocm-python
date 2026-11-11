# ClusterMigrationState

Representation of a cluster migration state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A longer description of the current state of the cluster migration. | [optional] 
**value** | [**ClusterMigrationStateValue**](ClusterMigrationStateValue.md) |  | [optional] 

## Example

```python
from ocm_client.models.cluster_migration_state import ClusterMigrationState

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMigrationState from a JSON string
cluster_migration_state_instance = ClusterMigrationState.from_json(json)
# print the JSON string representation of the object
print(ClusterMigrationState.to_json())

# convert the object into a dict
cluster_migration_state_dict = cluster_migration_state_instance.to_dict()
# create an instance of ClusterMigrationState from a dict
cluster_migration_state_from_dict = ClusterMigrationState.from_dict(cluster_migration_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


