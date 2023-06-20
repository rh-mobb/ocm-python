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


class AddOnParameter(object):
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
        'addon': 'AddOn',
        'conditions': 'list[AddOnRequirement]',
        'default_value': 'str',
        'description': 'str',
        'editable': 'bool',
        'editable_direction': 'str',
        'enabled': 'bool',
        'name': 'str',
        'options': 'list[AddOnParameterOption]',
        'required': 'bool',
        'validation': 'str',
        'validation_err_msg': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'addon': 'addon',
        'conditions': 'conditions',
        'default_value': 'default_value',
        'description': 'description',
        'editable': 'editable',
        'editable_direction': 'editable_direction',
        'enabled': 'enabled',
        'name': 'name',
        'options': 'options',
        'required': 'required',
        'validation': 'validation',
        'validation_err_msg': 'validation_err_msg',
        'value_type': 'value_type'
    }

    def __init__(self, kind=None, id=None, href=None, addon=None, conditions=None, default_value=None, description=None, editable=None, editable_direction=None, enabled=None, name=None, options=None, required=None, validation=None, validation_err_msg=None, value_type=None, local_vars_configuration=None):  # noqa: E501
        """AddOnParameter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._addon = None
        self._conditions = None
        self._default_value = None
        self._description = None
        self._editable = None
        self._editable_direction = None
        self._enabled = None
        self._name = None
        self._options = None
        self._required = None
        self._validation = None
        self._validation_err_msg = None
        self._value_type = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if addon is not None:
            self.addon = addon
        if conditions is not None:
            self.conditions = conditions
        if default_value is not None:
            self.default_value = default_value
        if description is not None:
            self.description = description
        if editable is not None:
            self.editable = editable
        if editable_direction is not None:
            self.editable_direction = editable_direction
        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if required is not None:
            self.required = required
        if validation is not None:
            self.validation = validation
        if validation_err_msg is not None:
            self.validation_err_msg = validation_err_msg
        if value_type is not None:
            self.value_type = value_type

    @property
    def kind(self):
        """Gets the kind of this AddOnParameter.  # noqa: E501

        Indicates the type of this object. Will be 'AddOnParameter' if this is a complete object or 'AddOnParameterLink' if it is just a link.  # noqa: E501

        :return: The kind of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AddOnParameter.

        Indicates the type of this object. Will be 'AddOnParameter' if this is a complete object or 'AddOnParameterLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this AddOnParameter.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddOnParameter.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this AddOnParameter.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AddOnParameter.

        Self link.  # noqa: E501

        :param href: The href of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def addon(self):
        """Gets the addon of this AddOnParameter.  # noqa: E501


        :return: The addon of this AddOnParameter.  # noqa: E501
        :rtype: AddOn
        """
        return self._addon

    @addon.setter
    def addon(self, addon):
        """Sets the addon of this AddOnParameter.


        :param addon: The addon of this AddOnParameter.  # noqa: E501
        :type: AddOn
        """

        self._addon = addon

    @property
    def conditions(self):
        """Gets the conditions of this AddOnParameter.  # noqa: E501

        Conditions in which this parameter is valid for  # noqa: E501

        :return: The conditions of this AddOnParameter.  # noqa: E501
        :rtype: list[AddOnRequirement]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AddOnParameter.

        Conditions in which this parameter is valid for  # noqa: E501

        :param conditions: The conditions of this AddOnParameter.  # noqa: E501
        :type: list[AddOnRequirement]
        """

        self._conditions = conditions

    @property
    def default_value(self):
        """Gets the default_value of this AddOnParameter.  # noqa: E501

        Indicates the value default for the add-on parameter.  # noqa: E501

        :return: The default_value of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this AddOnParameter.

        Indicates the value default for the add-on parameter.  # noqa: E501

        :param default_value: The default_value of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def description(self):
        """Gets the description of this AddOnParameter.  # noqa: E501

        Description of the add-on parameter.  # noqa: E501

        :return: The description of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddOnParameter.

        Description of the add-on parameter.  # noqa: E501

        :param description: The description of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def editable(self):
        """Gets the editable of this AddOnParameter.  # noqa: E501

        Indicates if this parameter can be edited after creation.  # noqa: E501

        :return: The editable of this AddOnParameter.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this AddOnParameter.

        Indicates if this parameter can be edited after creation.  # noqa: E501

        :param editable: The editable of this AddOnParameter.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def editable_direction(self):
        """Gets the editable_direction of this AddOnParameter.  # noqa: E501

        Restricts if the parameter can be upscaled/downscaled Expected values are \"up\", \"down\", or \"\" (no restriction).  # noqa: E501

        :return: The editable_direction of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._editable_direction

    @editable_direction.setter
    def editable_direction(self, editable_direction):
        """Sets the editable_direction of this AddOnParameter.

        Restricts if the parameter can be upscaled/downscaled Expected values are \"up\", \"down\", or \"\" (no restriction).  # noqa: E501

        :param editable_direction: The editable_direction of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._editable_direction = editable_direction

    @property
    def enabled(self):
        """Gets the enabled of this AddOnParameter.  # noqa: E501

        Indicates if this parameter is enabled for the add-on.  # noqa: E501

        :return: The enabled of this AddOnParameter.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AddOnParameter.

        Indicates if this parameter is enabled for the add-on.  # noqa: E501

        :param enabled: The enabled of this AddOnParameter.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def name(self):
        """Gets the name of this AddOnParameter.  # noqa: E501

        Name of the add-on parameter.  # noqa: E501

        :return: The name of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddOnParameter.

        Name of the add-on parameter.  # noqa: E501

        :param name: The name of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this AddOnParameter.  # noqa: E501

        List of options for the add-on parameter value.  # noqa: E501

        :return: The options of this AddOnParameter.  # noqa: E501
        :rtype: list[AddOnParameterOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this AddOnParameter.

        List of options for the add-on parameter value.  # noqa: E501

        :param options: The options of this AddOnParameter.  # noqa: E501
        :type: list[AddOnParameterOption]
        """

        self._options = options

    @property
    def required(self):
        """Gets the required of this AddOnParameter.  # noqa: E501

        Indicates if this parameter is required by the add-on.  # noqa: E501

        :return: The required of this AddOnParameter.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this AddOnParameter.

        Indicates if this parameter is required by the add-on.  # noqa: E501

        :param required: The required of this AddOnParameter.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def validation(self):
        """Gets the validation of this AddOnParameter.  # noqa: E501

        Validation rule for the add-on parameter.  # noqa: E501

        :return: The validation of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this AddOnParameter.

        Validation rule for the add-on parameter.  # noqa: E501

        :param validation: The validation of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._validation = validation

    @property
    def validation_err_msg(self):
        """Gets the validation_err_msg of this AddOnParameter.  # noqa: E501

        Error message to return should the parameter be invalid.  # noqa: E501

        :return: The validation_err_msg of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._validation_err_msg

    @validation_err_msg.setter
    def validation_err_msg(self, validation_err_msg):
        """Sets the validation_err_msg of this AddOnParameter.

        Error message to return should the parameter be invalid.  # noqa: E501

        :param validation_err_msg: The validation_err_msg of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._validation_err_msg = validation_err_msg

    @property
    def value_type(self):
        """Gets the value_type of this AddOnParameter.  # noqa: E501

        Type of value of the add-on parameter.  # noqa: E501

        :return: The value_type of this AddOnParameter.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this AddOnParameter.

        Type of value of the add-on parameter.  # noqa: E501

        :param value_type: The value_type of this AddOnParameter.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

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
        if not isinstance(other, AddOnParameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddOnParameter):
            return True

        return self.to_dict() != other.to_dict()
