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


class CloudRegion(object):
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
        'ccs_only': 'bool',
        'kms_location_id': 'str',
        'kms_location_name': 'str',
        'cloud_provider': 'CloudProvider',
        'display_name': 'str',
        'enabled': 'bool',
        'govcloud': 'bool',
        'name': 'str',
        'supports_hypershift': 'bool',
        'supports_multi_az': 'bool'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'ccs_only': 'ccs_only',
        'kms_location_id': 'kms_location_id',
        'kms_location_name': 'kms_location_name',
        'cloud_provider': 'cloud_provider',
        'display_name': 'display_name',
        'enabled': 'enabled',
        'govcloud': 'govcloud',
        'name': 'name',
        'supports_hypershift': 'supports_hypershift',
        'supports_multi_az': 'supports_multi_az'
    }

    def __init__(self, kind=None, id=None, href=None, ccs_only=None, kms_location_id=None, kms_location_name=None, cloud_provider=None, display_name=None, enabled=None, govcloud=None, name=None, supports_hypershift=None, supports_multi_az=None, local_vars_configuration=None):  # noqa: E501
        """CloudRegion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._ccs_only = None
        self._kms_location_id = None
        self._kms_location_name = None
        self._cloud_provider = None
        self._display_name = None
        self._enabled = None
        self._govcloud = None
        self._name = None
        self._supports_hypershift = None
        self._supports_multi_az = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if ccs_only is not None:
            self.ccs_only = ccs_only
        if kms_location_id is not None:
            self.kms_location_id = kms_location_id
        if kms_location_name is not None:
            self.kms_location_name = kms_location_name
        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if display_name is not None:
            self.display_name = display_name
        if enabled is not None:
            self.enabled = enabled
        if govcloud is not None:
            self.govcloud = govcloud
        if name is not None:
            self.name = name
        if supports_hypershift is not None:
            self.supports_hypershift = supports_hypershift
        if supports_multi_az is not None:
            self.supports_multi_az = supports_multi_az

    @property
    def kind(self):
        """Gets the kind of this CloudRegion.  # noqa: E501

        Indicates the type of this object. Will be 'CloudRegion' if this is a complete object or 'CloudRegionLink' if it is just a link.  # noqa: E501

        :return: The kind of this CloudRegion.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CloudRegion.

        Indicates the type of this object. Will be 'CloudRegion' if this is a complete object or 'CloudRegionLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this CloudRegion.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this CloudRegion.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this CloudRegion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudRegion.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this CloudRegion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this CloudRegion.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this CloudRegion.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CloudRegion.

        Self link.  # noqa: E501

        :param href: The href of this CloudRegion.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def ccs_only(self):
        """Gets the ccs_only of this CloudRegion.  # noqa: E501

        'true' if the region is supported only for CCS clusters, 'false' otherwise.  # noqa: E501

        :return: The ccs_only of this CloudRegion.  # noqa: E501
        :rtype: bool
        """
        return self._ccs_only

    @ccs_only.setter
    def ccs_only(self, ccs_only):
        """Sets the ccs_only of this CloudRegion.

        'true' if the region is supported only for CCS clusters, 'false' otherwise.  # noqa: E501

        :param ccs_only: The ccs_only of this CloudRegion.  # noqa: E501
        :type: bool
        """

        self._ccs_only = ccs_only

    @property
    def kms_location_id(self):
        """Gets the kms_location_id of this CloudRegion.  # noqa: E501

        (GCP only) Comma-separated list of KMS location IDs that can be used with this region. E.g. \"global,nam4,us\". Order is not guaranteed.  # noqa: E501

        :return: The kms_location_id of this CloudRegion.  # noqa: E501
        :rtype: str
        """
        return self._kms_location_id

    @kms_location_id.setter
    def kms_location_id(self, kms_location_id):
        """Sets the kms_location_id of this CloudRegion.

        (GCP only) Comma-separated list of KMS location IDs that can be used with this region. E.g. \"global,nam4,us\". Order is not guaranteed.  # noqa: E501

        :param kms_location_id: The kms_location_id of this CloudRegion.  # noqa: E501
        :type: str
        """

        self._kms_location_id = kms_location_id

    @property
    def kms_location_name(self):
        """Gets the kms_location_name of this CloudRegion.  # noqa: E501

        (GCP only) Comma-separated list of display names corresponding to KMSLocationID. E.g. \"Global,nam4 (Iowa, South Carolina, and Oklahoma),US\". Order is not guaranteed but will match KMSLocationID. Unfortunately, this API doesn't allow robust splitting - Contact ocm-feedback@redhat.com if you want to rely on this.  # noqa: E501

        :return: The kms_location_name of this CloudRegion.  # noqa: E501
        :rtype: str
        """
        return self._kms_location_name

    @kms_location_name.setter
    def kms_location_name(self, kms_location_name):
        """Sets the kms_location_name of this CloudRegion.

        (GCP only) Comma-separated list of display names corresponding to KMSLocationID. E.g. \"Global,nam4 (Iowa, South Carolina, and Oklahoma),US\". Order is not guaranteed but will match KMSLocationID. Unfortunately, this API doesn't allow robust splitting - Contact ocm-feedback@redhat.com if you want to rely on this.  # noqa: E501

        :param kms_location_name: The kms_location_name of this CloudRegion.  # noqa: E501
        :type: str
        """

        self._kms_location_name = kms_location_name

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this CloudRegion.  # noqa: E501


        :return: The cloud_provider of this CloudRegion.  # noqa: E501
        :rtype: CloudProvider
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this CloudRegion.


        :param cloud_provider: The cloud_provider of this CloudRegion.  # noqa: E501
        :type: CloudProvider
        """

        self._cloud_provider = cloud_provider

    @property
    def display_name(self):
        """Gets the display_name of this CloudRegion.  # noqa: E501

        Name of the region for display purposes, for example `N. Virginia`.  # noqa: E501

        :return: The display_name of this CloudRegion.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CloudRegion.

        Name of the region for display purposes, for example `N. Virginia`.  # noqa: E501

        :param display_name: The display_name of this CloudRegion.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def enabled(self):
        """Gets the enabled of this CloudRegion.  # noqa: E501

        Whether the region is enabled for deploying a managed cluster.  # noqa: E501

        :return: The enabled of this CloudRegion.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CloudRegion.

        Whether the region is enabled for deploying a managed cluster.  # noqa: E501

        :param enabled: The enabled of this CloudRegion.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def govcloud(self):
        """Gets the govcloud of this CloudRegion.  # noqa: E501

        Whether the region is an AWS GovCloud region.  # noqa: E501

        :return: The govcloud of this CloudRegion.  # noqa: E501
        :rtype: bool
        """
        return self._govcloud

    @govcloud.setter
    def govcloud(self, govcloud):
        """Sets the govcloud of this CloudRegion.

        Whether the region is an AWS GovCloud region.  # noqa: E501

        :param govcloud: The govcloud of this CloudRegion.  # noqa: E501
        :type: bool
        """

        self._govcloud = govcloud

    @property
    def name(self):
        """Gets the name of this CloudRegion.  # noqa: E501

        Human friendly identifier of the region, for example `us-east-1`.  NOTE: Currently for all cloud providers and all regions `id` and `name` have exactly the same values.  # noqa: E501

        :return: The name of this CloudRegion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudRegion.

        Human friendly identifier of the region, for example `us-east-1`.  NOTE: Currently for all cloud providers and all regions `id` and `name` have exactly the same values.  # noqa: E501

        :param name: The name of this CloudRegion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def supports_hypershift(self):
        """Gets the supports_hypershift of this CloudRegion.  # noqa: E501

        'true' if the region is supported for Hypershift deployments, 'false' otherwise.  # noqa: E501

        :return: The supports_hypershift of this CloudRegion.  # noqa: E501
        :rtype: bool
        """
        return self._supports_hypershift

    @supports_hypershift.setter
    def supports_hypershift(self, supports_hypershift):
        """Sets the supports_hypershift of this CloudRegion.

        'true' if the region is supported for Hypershift deployments, 'false' otherwise.  # noqa: E501

        :param supports_hypershift: The supports_hypershift of this CloudRegion.  # noqa: E501
        :type: bool
        """

        self._supports_hypershift = supports_hypershift

    @property
    def supports_multi_az(self):
        """Gets the supports_multi_az of this CloudRegion.  # noqa: E501

        Whether the region supports multiple availability zones.  # noqa: E501

        :return: The supports_multi_az of this CloudRegion.  # noqa: E501
        :rtype: bool
        """
        return self._supports_multi_az

    @supports_multi_az.setter
    def supports_multi_az(self, supports_multi_az):
        """Sets the supports_multi_az of this CloudRegion.

        Whether the region supports multiple availability zones.  # noqa: E501

        :param supports_multi_az: The supports_multi_az of this CloudRegion.  # noqa: E501
        :type: bool
        """

        self._supports_multi_az = supports_multi_az

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
        if not isinstance(other, CloudRegion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudRegion):
            return True

        return self.to_dict() != other.to_dict()
