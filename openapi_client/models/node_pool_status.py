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


class NodePoolStatus(object):
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
        'current_replicas': 'int',
        'message': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'current_replicas': 'current_replicas',
        'message': 'message'
    }

    def __init__(self, kind=None, id=None, href=None, current_replicas=None, message=None, local_vars_configuration=None):  # noqa: E501
        """NodePoolStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._current_replicas = None
        self._message = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if current_replicas is not None:
            self.current_replicas = current_replicas
        if message is not None:
            self.message = message

    @property
    def kind(self):
        """Gets the kind of this NodePoolStatus.  # noqa: E501

        Indicates the type of this object. Will be 'NodePoolStatus' if this is a complete object or 'NodePoolStatusLink' if it is just a link.  # noqa: E501

        :return: The kind of this NodePoolStatus.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this NodePoolStatus.

        Indicates the type of this object. Will be 'NodePoolStatus' if this is a complete object or 'NodePoolStatusLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this NodePoolStatus.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this NodePoolStatus.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this NodePoolStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodePoolStatus.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this NodePoolStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this NodePoolStatus.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this NodePoolStatus.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this NodePoolStatus.

        Self link.  # noqa: E501

        :param href: The href of this NodePoolStatus.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def current_replicas(self):
        """Gets the current_replicas of this NodePoolStatus.  # noqa: E501

        The current number of replicas for the node pool.  # noqa: E501

        :return: The current_replicas of this NodePoolStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """Sets the current_replicas of this NodePoolStatus.

        The current number of replicas for the node pool.  # noqa: E501

        :param current_replicas: The current_replicas of this NodePoolStatus.  # noqa: E501
        :type: int
        """

        self._current_replicas = current_replicas

    @property
    def message(self):
        """Gets the message of this NodePoolStatus.  # noqa: E501

        Adds additional information about the NodePool status when the node pool doesn't reach the desired replicas.  # noqa: E501

        :return: The message of this NodePoolStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NodePoolStatus.

        Adds additional information about the NodePool status when the node pool doesn't reach the desired replicas.  # noqa: E501

        :param message: The message of this NodePoolStatus.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, NodePoolStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodePoolStatus):
            return True

        return self.to_dict() != other.to_dict()
