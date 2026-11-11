# Version

Representation of an _OpenShift_ version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;Version&#39; if this is a complete object or &#39;VersionLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**gcp_marketplace_enabled** | **bool** | GCPMarketplaceEnabled indicates if this version can be used to create GCP Marketplace clusters. | [optional] 
**rosa_enabled** | **bool** | ROSAEnabled indicates whether this version can be used to create ROSA clusters. | [optional] 
**available_channels** | **List[str]** | AvailableChannels is the list of channels in which this version is present | [optional] 
**available_upgrades** | **List[str]** | AvailableUpgrades is the list of versions this version can be upgraded to. | [optional] 
**channel_group** | **str** | ChannelGroup is the name of the group where this image belongs. ChannelGroup is a mechanism to partition the images to different groups, each image belongs to only a single group. | [optional] 
**default** | **bool** | Indicates if this should be selected as the default version when a cluster is created without specifying explicitly the version. | [optional] 
**enabled** | **bool** | Indicates if this version can be used to create clusters. | [optional] 
**end_of_life_timestamp** | **datetime** | EndOfLifeTimestamp is the date and time when the version will get to End of Life, using the format defined in https://www.ietf.org/rfc/rfc3339.txt[RC3339]. | [optional] 
**hosted_control_plane_default** | **bool** | HostedControlPlaneDefault is a flag that indicates if this should be selected as the default version when a HCP cluster is created without specifying explicitly the version. | [optional] 
**hosted_control_plane_enabled** | **bool** | HostedControlPlaneEnabled indicates whether this version can be used to create HCP clusters. | [optional] 
**image_overrides** | [**ImageOverrides**](ImageOverrides.md) |  | [optional] 
**raw_id** | **str** | RawID is the id of the version - without channel group and prefix. | [optional] 
**release_image** | **str** | ReleaseImage contains the URI of Openshift release image for amd64 architecture. | [optional] 
**release_images** | [**ReleaseImages**](ReleaseImages.md) |  | [optional] 
**wif_enabled** | **bool** | WifEnabled is a flag that indicates whether this version is enabled for Workload Identity Federation. | [optional] 

## Example

```python
from ocm_client.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print(Version.to_json())

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_from_dict = Version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


