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


class AddOnConfig(object):
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
        'add_on_environment_variables': 'list[AddOnEnvironmentVariable]',
        'secret_propagations': 'list[AddOnSecretPropagation]'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'add_on_environment_variables': 'add_on_environment_variables',
        'secret_propagations': 'secret_propagations'
    }

    def __init__(self, kind=None, id=None, href=None, add_on_environment_variables=None, secret_propagations=None, local_vars_configuration=None):  # noqa: E501
        """AddOnConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._add_on_environment_variables = None
        self._secret_propagations = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if add_on_environment_variables is not None:
            self.add_on_environment_variables = add_on_environment_variables
        if secret_propagations is not None:
            self.secret_propagations = secret_propagations

    @property
    def kind(self):
        """Gets the kind of this AddOnConfig.  # noqa: E501

        Indicates the type of this object. Will be 'AddOnConfig' if this is a complete object or 'AddOnConfigLink' if it is just a link.  # noqa: E501

        :return: The kind of this AddOnConfig.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AddOnConfig.

        Indicates the type of this object. Will be 'AddOnConfig' if this is a complete object or 'AddOnConfigLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this AddOnConfig.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this AddOnConfig.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this AddOnConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddOnConfig.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this AddOnConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this AddOnConfig.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this AddOnConfig.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AddOnConfig.

        Self link.  # noqa: E501

        :param href: The href of this AddOnConfig.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def add_on_environment_variables(self):
        """Gets the add_on_environment_variables of this AddOnConfig.  # noqa: E501

        List of environment variables for the addon  # noqa: E501

        :return: The add_on_environment_variables of this AddOnConfig.  # noqa: E501
        :rtype: list[AddOnEnvironmentVariable]
        """
        return self._add_on_environment_variables

    @add_on_environment_variables.setter
    def add_on_environment_variables(self, add_on_environment_variables):
        """Sets the add_on_environment_variables of this AddOnConfig.

        List of environment variables for the addon  # noqa: E501

        :param add_on_environment_variables: The add_on_environment_variables of this AddOnConfig.  # noqa: E501
        :type: list[AddOnEnvironmentVariable]
        """

        self._add_on_environment_variables = add_on_environment_variables

    @property
    def secret_propagations(self):
        """Gets the secret_propagations of this AddOnConfig.  # noqa: E501

        List of secret propagations for the addon  # noqa: E501

        :return: The secret_propagations of this AddOnConfig.  # noqa: E501
        :rtype: list[AddOnSecretPropagation]
        """
        return self._secret_propagations

    @secret_propagations.setter
    def secret_propagations(self, secret_propagations):
        """Sets the secret_propagations of this AddOnConfig.

        List of secret propagations for the addon  # noqa: E501

        :param secret_propagations: The secret_propagations of this AddOnConfig.  # noqa: E501
        :type: list[AddOnSecretPropagation]
        """

        self._secret_propagations = secret_propagations

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
        if not isinstance(other, AddOnConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddOnConfig):
            return True

        return self.to_dict() != other.to_dict()
