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


class Proxy(object):
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
        'http_proxy': 'str',
        'https_proxy': 'str',
        'no_proxy': 'str'
    }

    attribute_map = {
        'http_proxy': 'http_proxy',
        'https_proxy': 'https_proxy',
        'no_proxy': 'no_proxy'
    }

    def __init__(self, http_proxy=None, https_proxy=None, no_proxy=None, local_vars_configuration=None):  # noqa: E501
        """Proxy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._http_proxy = None
        self._https_proxy = None
        self._no_proxy = None
        self.discriminator = None

        if http_proxy is not None:
            self.http_proxy = http_proxy
        if https_proxy is not None:
            self.https_proxy = https_proxy
        if no_proxy is not None:
            self.no_proxy = no_proxy

    @property
    def http_proxy(self):
        """Gets the http_proxy of this Proxy.  # noqa: E501

        HTTPProxy is the URL of the proxy for HTTP requests.  # noqa: E501

        :return: The http_proxy of this Proxy.  # noqa: E501
        :rtype: str
        """
        return self._http_proxy

    @http_proxy.setter
    def http_proxy(self, http_proxy):
        """Sets the http_proxy of this Proxy.

        HTTPProxy is the URL of the proxy for HTTP requests.  # noqa: E501

        :param http_proxy: The http_proxy of this Proxy.  # noqa: E501
        :type: str
        """

        self._http_proxy = http_proxy

    @property
    def https_proxy(self):
        """Gets the https_proxy of this Proxy.  # noqa: E501

        HTTPSProxy is the URL of the proxy for HTTPS requests.  # noqa: E501

        :return: The https_proxy of this Proxy.  # noqa: E501
        :rtype: str
        """
        return self._https_proxy

    @https_proxy.setter
    def https_proxy(self, https_proxy):
        """Sets the https_proxy of this Proxy.

        HTTPSProxy is the URL of the proxy for HTTPS requests.  # noqa: E501

        :param https_proxy: The https_proxy of this Proxy.  # noqa: E501
        :type: str
        """

        self._https_proxy = https_proxy

    @property
    def no_proxy(self):
        """Gets the no_proxy of this Proxy.  # noqa: E501

        NoProxy is a comma-separated list of domains and CIDRs for which  the proxy should not be used  # noqa: E501

        :return: The no_proxy of this Proxy.  # noqa: E501
        :rtype: str
        """
        return self._no_proxy

    @no_proxy.setter
    def no_proxy(self, no_proxy):
        """Sets the no_proxy of this Proxy.

        NoProxy is a comma-separated list of domains and CIDRs for which  the proxy should not be used  # noqa: E501

        :param no_proxy: The no_proxy of this Proxy.  # noqa: E501
        :type: str
        """

        self._no_proxy = no_proxy

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
        if not isinstance(other, Proxy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Proxy):
            return True

        return self.to_dict() != other.to_dict()
