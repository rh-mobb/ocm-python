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

from openapi_client.configuration import Configuration


class PrivateLinkClusterConfiguration(object):
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
        'principals': 'list[PrivateLinkPrincipal]'
    }

    attribute_map = {
        'principals': 'principals'
    }

    def __init__(self, principals=None, local_vars_configuration=None):  # noqa: E501
        """PrivateLinkClusterConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._principals = None
        self.discriminator = None

        if principals is not None:
            self.principals = principals

    @property
    def principals(self):
        """Gets the principals of this PrivateLinkClusterConfiguration.  # noqa: E501

        List of additional principals for the Private Link  # noqa: E501

        :return: The principals of this PrivateLinkClusterConfiguration.  # noqa: E501
        :rtype: list[PrivateLinkPrincipal]
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        """Sets the principals of this PrivateLinkClusterConfiguration.

        List of additional principals for the Private Link  # noqa: E501

        :param principals: The principals of this PrivateLinkClusterConfiguration.  # noqa: E501
        :type: list[PrivateLinkPrincipal]
        """

        self._principals = principals

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
        if not isinstance(other, PrivateLinkClusterConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrivateLinkClusterConfiguration):
            return True

        return self.to_dict() != other.to_dict()