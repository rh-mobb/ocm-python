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


class SubnetNetworkVerification(object):
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
        'details': 'list[str]',
        'state': 'str',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'details': 'details',
        'state': 'state',
        'tags': 'tags'
    }

    def __init__(self, kind=None, id=None, href=None, details=None, state=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """SubnetNetworkVerification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._details = None
        self._state = None
        self._tags = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if details is not None:
            self.details = details
        if state is not None:
            self.state = state
        if tags is not None:
            self.tags = tags

    @property
    def kind(self):
        """Gets the kind of this SubnetNetworkVerification.  # noqa: E501

        Indicates the type of this object. Will be 'SubnetNetworkVerification' if this is a complete object or 'SubnetNetworkVerificationLink' if it is just a link.  # noqa: E501

        :return: The kind of this SubnetNetworkVerification.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this SubnetNetworkVerification.

        Indicates the type of this object. Will be 'SubnetNetworkVerification' if this is a complete object or 'SubnetNetworkVerificationLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this SubnetNetworkVerification.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this SubnetNetworkVerification.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this SubnetNetworkVerification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubnetNetworkVerification.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this SubnetNetworkVerification.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this SubnetNetworkVerification.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this SubnetNetworkVerification.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SubnetNetworkVerification.

        Self link.  # noqa: E501

        :param href: The href of this SubnetNetworkVerification.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def details(self):
        """Gets the details of this SubnetNetworkVerification.  # noqa: E501

        Slice of failures that happened during a subnet network verification.  # noqa: E501

        :return: The details of this SubnetNetworkVerification.  # noqa: E501
        :rtype: list[str]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SubnetNetworkVerification.

        Slice of failures that happened during a subnet network verification.  # noqa: E501

        :param details: The details of this SubnetNetworkVerification.  # noqa: E501
        :type: list[str]
        """

        self._details = details

    @property
    def state(self):
        """Gets the state of this SubnetNetworkVerification.  # noqa: E501

        State of the subnet network verification.  # noqa: E501

        :return: The state of this SubnetNetworkVerification.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubnetNetworkVerification.

        State of the subnet network verification.  # noqa: E501

        :param state: The state of this SubnetNetworkVerification.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tags(self):
        """Gets the tags of this SubnetNetworkVerification.  # noqa: E501

        Tags supplied to the network verifier for this subnet.  # noqa: E501

        :return: The tags of this SubnetNetworkVerification.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SubnetNetworkVerification.

        Tags supplied to the network verifier for this subnet.  # noqa: E501

        :param tags: The tags of this SubnetNetworkVerification.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

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
        if not isinstance(other, SubnetNetworkVerification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubnetNetworkVerification):
            return True

        return self.to_dict() != other.to_dict()