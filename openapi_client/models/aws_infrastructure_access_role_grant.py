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


class AWSInfrastructureAccessRoleGrant(object):
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
        'console_url': 'str',
        'role': 'AWSInfrastructureAccessRole',
        'state': 'AWSInfrastructureAccessRoleGrantState',
        'state_description': 'str',
        'user_arn': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'console_url': 'console_url',
        'role': 'role',
        'state': 'state',
        'state_description': 'state_description',
        'user_arn': 'user_arn'
    }

    def __init__(self, kind=None, id=None, href=None, console_url=None, role=None, state=None, state_description=None, user_arn=None, local_vars_configuration=None):  # noqa: E501
        """AWSInfrastructureAccessRoleGrant - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._console_url = None
        self._role = None
        self._state = None
        self._state_description = None
        self._user_arn = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if console_url is not None:
            self.console_url = console_url
        if role is not None:
            self.role = role
        if state is not None:
            self.state = state
        if state_description is not None:
            self.state_description = state_description
        if user_arn is not None:
            self.user_arn = user_arn

    @property
    def kind(self):
        """Gets the kind of this AWSInfrastructureAccessRoleGrant.  # noqa: E501

        Indicates the type of this object. Will be 'AWSInfrastructureAccessRoleGrant' if this is a complete object or 'AWSInfrastructureAccessRoleGrantLink' if it is just a link.  # noqa: E501

        :return: The kind of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AWSInfrastructureAccessRoleGrant.

        Indicates the type of this object. Will be 'AWSInfrastructureAccessRoleGrant' if this is a complete object or 'AWSInfrastructureAccessRoleGrantLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this AWSInfrastructureAccessRoleGrant.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AWSInfrastructureAccessRoleGrant.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this AWSInfrastructureAccessRoleGrant.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AWSInfrastructureAccessRoleGrant.

        Self link.  # noqa: E501

        :param href: The href of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def console_url(self):
        """Gets the console_url of this AWSInfrastructureAccessRoleGrant.  # noqa: E501

        URL to switch to the role in AWS console.  # noqa: E501

        :return: The console_url of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        """Sets the console_url of this AWSInfrastructureAccessRoleGrant.

        URL to switch to the role in AWS console.  # noqa: E501

        :param console_url: The console_url of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: str
        """

        self._console_url = console_url

    @property
    def role(self):
        """Gets the role of this AWSInfrastructureAccessRoleGrant.  # noqa: E501


        :return: The role of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: AWSInfrastructureAccessRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AWSInfrastructureAccessRoleGrant.


        :param role: The role of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: AWSInfrastructureAccessRole
        """

        self._role = role

    @property
    def state(self):
        """Gets the state of this AWSInfrastructureAccessRoleGrant.  # noqa: E501


        :return: The state of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: AWSInfrastructureAccessRoleGrantState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AWSInfrastructureAccessRoleGrant.


        :param state: The state of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: AWSInfrastructureAccessRoleGrantState
        """

        self._state = state

    @property
    def state_description(self):
        """Gets the state_description of this AWSInfrastructureAccessRoleGrant.  # noqa: E501

        Description of the state. Will be empty unless state is 'Failed'.  # noqa: E501

        :return: The state_description of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: str
        """
        return self._state_description

    @state_description.setter
    def state_description(self, state_description):
        """Sets the state_description of this AWSInfrastructureAccessRoleGrant.

        Description of the state. Will be empty unless state is 'Failed'.  # noqa: E501

        :param state_description: The state_description of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: str
        """

        self._state_description = state_description

    @property
    def user_arn(self):
        """Gets the user_arn of this AWSInfrastructureAccessRoleGrant.  # noqa: E501

        The user AWS IAM ARN we want to grant the role.  # noqa: E501

        :return: The user_arn of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :rtype: str
        """
        return self._user_arn

    @user_arn.setter
    def user_arn(self, user_arn):
        """Sets the user_arn of this AWSInfrastructureAccessRoleGrant.

        The user AWS IAM ARN we want to grant the role.  # noqa: E501

        :param user_arn: The user_arn of this AWSInfrastructureAccessRoleGrant.  # noqa: E501
        :type: str
        """

        self._user_arn = user_arn

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
        if not isinstance(other, AWSInfrastructureAccessRoleGrant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AWSInfrastructureAccessRoleGrant):
            return True

        return self.to_dict() != other.to_dict()
