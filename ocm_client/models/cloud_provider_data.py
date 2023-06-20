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


class CloudProviderData(object):
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
        'aws': 'AWS',
        'gcp': 'GCP',
        'availability_zones': 'list[str]',
        'key_location': 'str',
        'key_ring_name': 'str',
        'region': 'CloudRegion',
        'subnets': 'list[str]',
        'version': 'Version'
    }

    attribute_map = {
        'aws': 'aws',
        'gcp': 'gcp',
        'availability_zones': 'availability_zones',
        'key_location': 'key_location',
        'key_ring_name': 'key_ring_name',
        'region': 'region',
        'subnets': 'subnets',
        'version': 'version'
    }

    def __init__(self, aws=None, gcp=None, availability_zones=None, key_location=None, key_ring_name=None, region=None, subnets=None, version=None, local_vars_configuration=None):  # noqa: E501
        """CloudProviderData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aws = None
        self._gcp = None
        self._availability_zones = None
        self._key_location = None
        self._key_ring_name = None
        self._region = None
        self._subnets = None
        self._version = None
        self.discriminator = None

        if aws is not None:
            self.aws = aws
        if gcp is not None:
            self.gcp = gcp
        if availability_zones is not None:
            self.availability_zones = availability_zones
        if key_location is not None:
            self.key_location = key_location
        if key_ring_name is not None:
            self.key_ring_name = key_ring_name
        if region is not None:
            self.region = region
        if subnets is not None:
            self.subnets = subnets
        if version is not None:
            self.version = version

    @property
    def aws(self):
        """Gets the aws of this CloudProviderData.  # noqa: E501


        :return: The aws of this CloudProviderData.  # noqa: E501
        :rtype: AWS
        """
        return self._aws

    @aws.setter
    def aws(self, aws):
        """Sets the aws of this CloudProviderData.


        :param aws: The aws of this CloudProviderData.  # noqa: E501
        :type: AWS
        """

        self._aws = aws

    @property
    def gcp(self):
        """Gets the gcp of this CloudProviderData.  # noqa: E501


        :return: The gcp of this CloudProviderData.  # noqa: E501
        :rtype: GCP
        """
        return self._gcp

    @gcp.setter
    def gcp(self, gcp):
        """Sets the gcp of this CloudProviderData.


        :param gcp: The gcp of this CloudProviderData.  # noqa: E501
        :type: GCP
        """

        self._gcp = gcp

    @property
    def availability_zones(self):
        """Gets the availability_zones of this CloudProviderData.  # noqa: E501

        Availability zone  # noqa: E501

        :return: The availability_zones of this CloudProviderData.  # noqa: E501
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this CloudProviderData.

        Availability zone  # noqa: E501

        :param availability_zones: The availability_zones of this CloudProviderData.  # noqa: E501
        :type: list[str]
        """

        self._availability_zones = availability_zones

    @property
    def key_location(self):
        """Gets the key_location of this CloudProviderData.  # noqa: E501

        Key location  # noqa: E501

        :return: The key_location of this CloudProviderData.  # noqa: E501
        :rtype: str
        """
        return self._key_location

    @key_location.setter
    def key_location(self, key_location):
        """Sets the key_location of this CloudProviderData.

        Key location  # noqa: E501

        :param key_location: The key_location of this CloudProviderData.  # noqa: E501
        :type: str
        """

        self._key_location = key_location

    @property
    def key_ring_name(self):
        """Gets the key_ring_name of this CloudProviderData.  # noqa: E501

        Key ring name  # noqa: E501

        :return: The key_ring_name of this CloudProviderData.  # noqa: E501
        :rtype: str
        """
        return self._key_ring_name

    @key_ring_name.setter
    def key_ring_name(self, key_ring_name):
        """Sets the key_ring_name of this CloudProviderData.

        Key ring name  # noqa: E501

        :param key_ring_name: The key_ring_name of this CloudProviderData.  # noqa: E501
        :type: str
        """

        self._key_ring_name = key_ring_name

    @property
    def region(self):
        """Gets the region of this CloudProviderData.  # noqa: E501


        :return: The region of this CloudProviderData.  # noqa: E501
        :rtype: CloudRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudProviderData.


        :param region: The region of this CloudProviderData.  # noqa: E501
        :type: CloudRegion
        """

        self._region = region

    @property
    def subnets(self):
        """Gets the subnets of this CloudProviderData.  # noqa: E501

        Subnets  # noqa: E501

        :return: The subnets of this CloudProviderData.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this CloudProviderData.

        Subnets  # noqa: E501

        :param subnets: The subnets of this CloudProviderData.  # noqa: E501
        :type: list[str]
        """

        self._subnets = subnets

    @property
    def version(self):
        """Gets the version of this CloudProviderData.  # noqa: E501


        :return: The version of this CloudProviderData.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CloudProviderData.


        :param version: The version of this CloudProviderData.  # noqa: E501
        :type: Version
        """

        self._version = version

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
        if not isinstance(other, CloudProviderData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudProviderData):
            return True

        return self.to_dict() != other.to_dict()