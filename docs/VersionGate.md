# VersionGate

Representation of an _OpenShift_ version gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;VersionGate&#39; if this is a complete object or &#39;VersionGateLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**sts_only** | **bool** | STSOnly indicates if this version gate is for STS clusters only, deprecated: to be replaced with ClusterCondition | [optional] 
**cluster_condition** | **str** | ClusterCondition aims at selecting the clusters targeted by this version gate, ignored if STSOnly is true | [optional] 
**creation_timestamp** | **datetime** | CreationTimestamp is the date and time when the version gate was created, format defined in https://www.ietf.org/rfc/rfc3339.txt[RC3339]. | [optional] 
**description** | **str** | Description of the version gate. | [optional] 
**documentation_url** | **str** | DocumentationURL is the URL for the documentation of the version gate. | [optional] 
**label** | **str** | Label representing the version gate in OpenShift. | [optional] 
**value** | **str** | Value represents the required value of the label. | [optional] 
**version_raw_id_prefix** | **str** | VersionRawIDPrefix represents the versions prefix that the gate applies to. | [optional] 
**warning_message** | **str** | WarningMessage is a warning that will be displayed to the user before they acknowledge the gate | [optional] 

## Example

```python
from ocm_client.models.version_gate import VersionGate

# TODO update the JSON string below
json = "{}"
# create an instance of VersionGate from a JSON string
version_gate_instance = VersionGate.from_json(json)
# print the JSON string representation of the object
print(VersionGate.to_json())

# convert the object into a dict
version_gate_dict = version_gate_instance.to_dict()
# create an instance of VersionGate from a dict
version_gate_from_dict = VersionGate.from_dict(version_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


