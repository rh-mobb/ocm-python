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


class LDAPIdentityProvider(object):
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
        'ca': 'str',
        'url': 'str',
        'attributes': 'LDAPAttributes',
        'bind_dn': 'str',
        'bind_password': 'str',
        'insecure': 'bool'
    }

    attribute_map = {
        'ca': 'ca',
        'url': 'url',
        'attributes': 'attributes',
        'bind_dn': 'bind_dn',
        'bind_password': 'bind_password',
        'insecure': 'insecure'
    }

    def __init__(self, ca=None, url=None, attributes=None, bind_dn=None, bind_password=None, insecure=None, local_vars_configuration=None):  # noqa: E501
        """LDAPIdentityProvider - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ca = None
        self._url = None
        self._attributes = None
        self._bind_dn = None
        self._bind_password = None
        self._insecure = None
        self.discriminator = None

        if ca is not None:
            self.ca = ca
        if url is not None:
            self.url = url
        if attributes is not None:
            self.attributes = attributes
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_password is not None:
            self.bind_password = bind_password
        if insecure is not None:
            self.insecure = insecure

    @property
    def ca(self):
        """Gets the ca of this LDAPIdentityProvider.  # noqa: E501

        Certificate bundle to use to validate server certificates for the configured URL.  # noqa: E501

        :return: The ca of this LDAPIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this LDAPIdentityProvider.

        Certificate bundle to use to validate server certificates for the configured URL.  # noqa: E501

        :param ca: The ca of this LDAPIdentityProvider.  # noqa: E501
        :type: str
        """

        self._ca = ca

    @property
    def url(self):
        """Gets the url of this LDAPIdentityProvider.  # noqa: E501

        An https://tools.ietf.org/html/rfc2255[RFC 2255] URL which specifies the LDAP host and search parameters to use.  # noqa: E501

        :return: The url of this LDAPIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LDAPIdentityProvider.

        An https://tools.ietf.org/html/rfc2255[RFC 2255] URL which specifies the LDAP host and search parameters to use.  # noqa: E501

        :param url: The url of this LDAPIdentityProvider.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def attributes(self):
        """Gets the attributes of this LDAPIdentityProvider.  # noqa: E501


        :return: The attributes of this LDAPIdentityProvider.  # noqa: E501
        :rtype: LDAPAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this LDAPIdentityProvider.


        :param attributes: The attributes of this LDAPIdentityProvider.  # noqa: E501
        :type: LDAPAttributes
        """

        self._attributes = attributes

    @property
    def bind_dn(self):
        """Gets the bind_dn of this LDAPIdentityProvider.  # noqa: E501

        Optional distinguished name to use to bind during the search phase.  # noqa: E501

        :return: The bind_dn of this LDAPIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this LDAPIdentityProvider.

        Optional distinguished name to use to bind during the search phase.  # noqa: E501

        :param bind_dn: The bind_dn of this LDAPIdentityProvider.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_password(self):
        """Gets the bind_password of this LDAPIdentityProvider.  # noqa: E501

        Optional password to use to bind during the search phase.  # noqa: E501

        :return: The bind_password of this LDAPIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._bind_password

    @bind_password.setter
    def bind_password(self, bind_password):
        """Sets the bind_password of this LDAPIdentityProvider.

        Optional password to use to bind during the search phase.  # noqa: E501

        :param bind_password: The bind_password of this LDAPIdentityProvider.  # noqa: E501
        :type: str
        """

        self._bind_password = bind_password

    @property
    def insecure(self):
        """Gets the insecure of this LDAPIdentityProvider.  # noqa: E501

        When `true` no TLS connection is made to the server. When `false` `ldaps://...` URLs connect using TLS and `ldap://...` are upgraded to TLS.  # noqa: E501

        :return: The insecure of this LDAPIdentityProvider.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this LDAPIdentityProvider.

        When `true` no TLS connection is made to the server. When `false` `ldaps://...` URLs connect using TLS and `ldap://...` are upgraded to TLS.  # noqa: E501

        :param insecure: The insecure of this LDAPIdentityProvider.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

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
        if not isinstance(other, LDAPIdentityProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LDAPIdentityProvider):
            return True

        return self.to_dict() != other.to_dict()
