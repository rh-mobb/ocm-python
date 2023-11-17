# coding: utf-8

"""
    clusters_mgmt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: ocm-feedback@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ocm_client.configuration import Configuration


class Version(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'kind': 'str',
        'id': 'str',
        'href': 'str',
        'gcp_marketplace_enabled': 'bool',
        'rosa_enabled': 'bool',
        'available_upgrades': 'list[str]',
        'channel_group': 'str',
        'default': 'bool',
        'enabled': 'bool',
        'end_of_life_timestamp': 'datetime',
        'hosted_control_plane_enabled': 'bool',
        'image_overrides': 'ImageOverrides',
        'raw_id': 'str',
        'release_image': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'gcp_marketplace_enabled': 'gcp_marketplace_enabled',
        'rosa_enabled': 'rosa_enabled',
        'available_upgrades': 'available_upgrades',
        'channel_group': 'channel_group',
        'default': 'default',
        'enabled': 'enabled',
        'end_of_life_timestamp': 'end_of_life_timestamp',
        'hosted_control_plane_enabled': 'hosted_control_plane_enabled',
        'image_overrides': 'image_overrides',
        'raw_id': 'raw_id',
        'release_image': 'release_image'
    }

    def __init__(self, kind=None, id=None, href=None, gcp_marketplace_enabled=None, rosa_enabled=None, available_upgrades=None, channel_group=None, default=None, enabled=None, end_of_life_timestamp=None, hosted_control_plane_enabled=None, image_overrides=None, raw_id=None, release_image=None, local_vars_configuration=None):  # noqa: E501
        """Version - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._gcp_marketplace_enabled = None
        self._rosa_enabled = None
        self._available_upgrades = None
        self._channel_group = None
        self._default = None
        self._enabled = None
        self._end_of_life_timestamp = None
        self._hosted_control_plane_enabled = None
        self._image_overrides = None
        self._raw_id = None
        self._release_image = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if gcp_marketplace_enabled is not None:
            self.gcp_marketplace_enabled = gcp_marketplace_enabled
        if rosa_enabled is not None:
            self.rosa_enabled = rosa_enabled
        if available_upgrades is not None:
            self.available_upgrades = available_upgrades
        if channel_group is not None:
            self.channel_group = channel_group
        if default is not None:
            self.default = default
        if enabled is not None:
            self.enabled = enabled
        if end_of_life_timestamp is not None:
            self.end_of_life_timestamp = end_of_life_timestamp
        if hosted_control_plane_enabled is not None:
            self.hosted_control_plane_enabled = hosted_control_plane_enabled
        if image_overrides is not None:
            self.image_overrides = image_overrides
        if raw_id is not None:
            self.raw_id = raw_id
        if release_image is not None:
            self.release_image = release_image

    @property
    def kind(self):
        """Gets the kind of this Version.  # noqa: E501

        Indicates the type of this object. Will be 'Version' if this is a complete object or 'VersionLink' if it is just a link.  # noqa: E501

        :return: The kind of this Version.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Version.

        Indicates the type of this object. Will be 'Version' if this is a complete object or 'VersionLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this Version.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this Version.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this Version.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Version.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this Version.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this Version.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this Version.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Version.

        Self link.  # noqa: E501

        :param href: The href of this Version.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def gcp_marketplace_enabled(self):
        """Gets the gcp_marketplace_enabled of this Version.  # noqa: E501

        GCPMarketplaceEnabled indicates if this version can be used to create GCP Marketplace clusters.  # noqa: E501

        :return: The gcp_marketplace_enabled of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._gcp_marketplace_enabled

    @gcp_marketplace_enabled.setter
    def gcp_marketplace_enabled(self, gcp_marketplace_enabled):
        """Sets the gcp_marketplace_enabled of this Version.

        GCPMarketplaceEnabled indicates if this version can be used to create GCP Marketplace clusters.  # noqa: E501

        :param gcp_marketplace_enabled: The gcp_marketplace_enabled of this Version.  # noqa: E501
        :type: bool
        """

        self._gcp_marketplace_enabled = gcp_marketplace_enabled

    @property
    def rosa_enabled(self):
        """Gets the rosa_enabled of this Version.  # noqa: E501

        ROSAEnabled indicates whether this version can be used to create ROSA clusters.  # noqa: E501

        :return: The rosa_enabled of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._rosa_enabled

    @rosa_enabled.setter
    def rosa_enabled(self, rosa_enabled):
        """Sets the rosa_enabled of this Version.

        ROSAEnabled indicates whether this version can be used to create ROSA clusters.  # noqa: E501

        :param rosa_enabled: The rosa_enabled of this Version.  # noqa: E501
        :type: bool
        """

        self._rosa_enabled = rosa_enabled

    @property
    def available_upgrades(self):
        """Gets the available_upgrades of this Version.  # noqa: E501

        AvailableUpgrades is the list of versions this version can be upgraded to.  # noqa: E501

        :return: The available_upgrades of this Version.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_upgrades

    @available_upgrades.setter
    def available_upgrades(self, available_upgrades):
        """Sets the available_upgrades of this Version.

        AvailableUpgrades is the list of versions this version can be upgraded to.  # noqa: E501

        :param available_upgrades: The available_upgrades of this Version.  # noqa: E501
        :type: list[str]
        """

        self._available_upgrades = available_upgrades

    @property
    def channel_group(self):
        """Gets the channel_group of this Version.  # noqa: E501

        ChannelGroup is the name of the group where this image belongs. ChannelGroup is a mechanism to partition the images to different groups, each image belongs to only a single group.  # noqa: E501

        :return: The channel_group of this Version.  # noqa: E501
        :rtype: str
        """
        return self._channel_group

    @channel_group.setter
    def channel_group(self, channel_group):
        """Sets the channel_group of this Version.

        ChannelGroup is the name of the group where this image belongs. ChannelGroup is a mechanism to partition the images to different groups, each image belongs to only a single group.  # noqa: E501

        :param channel_group: The channel_group of this Version.  # noqa: E501
        :type: str
        """

        self._channel_group = channel_group

    @property
    def default(self):
        """Gets the default of this Version.  # noqa: E501

        Indicates if this should be selected as the default version when a cluster is created without specifying explicitly the version.  # noqa: E501

        :return: The default of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Version.

        Indicates if this should be selected as the default version when a cluster is created without specifying explicitly the version.  # noqa: E501

        :param default: The default of this Version.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def enabled(self):
        """Gets the enabled of this Version.  # noqa: E501

        Indicates if this version can be used to create clusters.  # noqa: E501

        :return: The enabled of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Version.

        Indicates if this version can be used to create clusters.  # noqa: E501

        :param enabled: The enabled of this Version.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def end_of_life_timestamp(self):
        """Gets the end_of_life_timestamp of this Version.  # noqa: E501

        EndOfLifeTimestamp is the date and time when the version will get to End of Life, using the format defined in https://www.ietf.org/rfc/rfc3339.txt[RC3339].  # noqa: E501

        :return: The end_of_life_timestamp of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._end_of_life_timestamp

    @end_of_life_timestamp.setter
    def end_of_life_timestamp(self, end_of_life_timestamp):
        """Sets the end_of_life_timestamp of this Version.

        EndOfLifeTimestamp is the date and time when the version will get to End of Life, using the format defined in https://www.ietf.org/rfc/rfc3339.txt[RC3339].  # noqa: E501

        :param end_of_life_timestamp: The end_of_life_timestamp of this Version.  # noqa: E501
        :type: datetime
        """

        self._end_of_life_timestamp = end_of_life_timestamp

    @property
    def hosted_control_plane_enabled(self):
        """Gets the hosted_control_plane_enabled of this Version.  # noqa: E501

        HostedControlPlaneEnabled indicates whether this version can be used to create HCP clusters.  # noqa: E501

        :return: The hosted_control_plane_enabled of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._hosted_control_plane_enabled

    @hosted_control_plane_enabled.setter
    def hosted_control_plane_enabled(self, hosted_control_plane_enabled):
        """Sets the hosted_control_plane_enabled of this Version.

        HostedControlPlaneEnabled indicates whether this version can be used to create HCP clusters.  # noqa: E501

        :param hosted_control_plane_enabled: The hosted_control_plane_enabled of this Version.  # noqa: E501
        :type: bool
        """

        self._hosted_control_plane_enabled = hosted_control_plane_enabled

    @property
    def image_overrides(self):
        """Gets the image_overrides of this Version.  # noqa: E501


        :return: The image_overrides of this Version.  # noqa: E501
        :rtype: ImageOverrides
        """
        return self._image_overrides

    @image_overrides.setter
    def image_overrides(self, image_overrides):
        """Sets the image_overrides of this Version.


        :param image_overrides: The image_overrides of this Version.  # noqa: E501
        :type: ImageOverrides
        """

        self._image_overrides = image_overrides

    @property
    def raw_id(self):
        """Gets the raw_id of this Version.  # noqa: E501

        RawID is the id of the version - without channel group and prefix.  # noqa: E501

        :return: The raw_id of this Version.  # noqa: E501
        :rtype: str
        """
        return self._raw_id

    @raw_id.setter
    def raw_id(self, raw_id):
        """Sets the raw_id of this Version.

        RawID is the id of the version - without channel group and prefix.  # noqa: E501

        :param raw_id: The raw_id of this Version.  # noqa: E501
        :type: str
        """

        self._raw_id = raw_id

    @property
    def release_image(self):
        """Gets the release_image of this Version.  # noqa: E501

        ReleaseImage contains the URI of Openshift release image.  # noqa: E501

        :return: The release_image of this Version.  # noqa: E501
        :rtype: str
        """
        return self._release_image

    @release_image.setter
    def release_image(self, release_image):
        """Sets the release_image of this Version.

        ReleaseImage contains the URI of Openshift release image.  # noqa: E501

        :param release_image: The release_image of this Version.  # noqa: E501
        :type: str
        """

        self._release_image = release_image

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Version):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Version):
            return True

        return self.to_dict() != other.to_dict()
