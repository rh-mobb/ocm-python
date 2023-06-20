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


class UpgradePolicy(object):
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
        'cluster_id': 'str',
        'enable_minor_version_upgrades': 'bool',
        'next_run': 'datetime',
        'schedule': 'str',
        'schedule_type': 'str',
        'upgrade_type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'cluster_id': 'cluster_id',
        'enable_minor_version_upgrades': 'enable_minor_version_upgrades',
        'next_run': 'next_run',
        'schedule': 'schedule',
        'schedule_type': 'schedule_type',
        'upgrade_type': 'upgrade_type',
        'version': 'version'
    }

    def __init__(self, kind=None, id=None, href=None, cluster_id=None, enable_minor_version_upgrades=None, next_run=None, schedule=None, schedule_type=None, upgrade_type=None, version=None, local_vars_configuration=None):  # noqa: E501
        """UpgradePolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._cluster_id = None
        self._enable_minor_version_upgrades = None
        self._next_run = None
        self._schedule = None
        self._schedule_type = None
        self._upgrade_type = None
        self._version = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if enable_minor_version_upgrades is not None:
            self.enable_minor_version_upgrades = enable_minor_version_upgrades
        if next_run is not None:
            self.next_run = next_run
        if schedule is not None:
            self.schedule = schedule
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if upgrade_type is not None:
            self.upgrade_type = upgrade_type
        if version is not None:
            self.version = version

    @property
    def kind(self):
        """Gets the kind of this UpgradePolicy.  # noqa: E501

        Indicates the type of this object. Will be 'UpgradePolicy' if this is a complete object or 'UpgradePolicyLink' if it is just a link.  # noqa: E501

        :return: The kind of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this UpgradePolicy.

        Indicates the type of this object. Will be 'UpgradePolicy' if this is a complete object or 'UpgradePolicyLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this UpgradePolicy.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this UpgradePolicy.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpgradePolicy.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this UpgradePolicy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this UpgradePolicy.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this UpgradePolicy.

        Self link.  # noqa: E501

        :param href: The href of this UpgradePolicy.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpgradePolicy.  # noqa: E501

        Cluster ID this upgrade policy is defined for.  # noqa: E501

        :return: The cluster_id of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpgradePolicy.

        Cluster ID this upgrade policy is defined for.  # noqa: E501

        :param cluster_id: The cluster_id of this UpgradePolicy.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def enable_minor_version_upgrades(self):
        """Gets the enable_minor_version_upgrades of this UpgradePolicy.  # noqa: E501

        Indicates if minor version upgrades are allowed for automatic upgrades (for manual it's always allowed).  # noqa: E501

        :return: The enable_minor_version_upgrades of this UpgradePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_minor_version_upgrades

    @enable_minor_version_upgrades.setter
    def enable_minor_version_upgrades(self, enable_minor_version_upgrades):
        """Sets the enable_minor_version_upgrades of this UpgradePolicy.

        Indicates if minor version upgrades are allowed for automatic upgrades (for manual it's always allowed).  # noqa: E501

        :param enable_minor_version_upgrades: The enable_minor_version_upgrades of this UpgradePolicy.  # noqa: E501
        :type: bool
        """

        self._enable_minor_version_upgrades = enable_minor_version_upgrades

    @property
    def next_run(self):
        """Gets the next_run of this UpgradePolicy.  # noqa: E501

        Next time the upgrade should run.  # noqa: E501

        :return: The next_run of this UpgradePolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._next_run

    @next_run.setter
    def next_run(self, next_run):
        """Sets the next_run of this UpgradePolicy.

        Next time the upgrade should run.  # noqa: E501

        :param next_run: The next_run of this UpgradePolicy.  # noqa: E501
        :type: datetime
        """

        self._next_run = next_run

    @property
    def schedule(self):
        """Gets the schedule of this UpgradePolicy.  # noqa: E501

        Schedule cron expression that defines automatic upgrade scheduling.  # noqa: E501

        :return: The schedule of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this UpgradePolicy.

        Schedule cron expression that defines automatic upgrade scheduling.  # noqa: E501

        :param schedule: The schedule of this UpgradePolicy.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def schedule_type(self):
        """Gets the schedule_type of this UpgradePolicy.  # noqa: E501

        Schedule type can be either \"manual\" (single execution) or \"automatic\" (re-occurring).  # noqa: E501

        :return: The schedule_type of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this UpgradePolicy.

        Schedule type can be either \"manual\" (single execution) or \"automatic\" (re-occurring).  # noqa: E501

        :param schedule_type: The schedule_type of this UpgradePolicy.  # noqa: E501
        :type: str
        """

        self._schedule_type = schedule_type

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this UpgradePolicy.  # noqa: E501

        Upgrade type specify the type of the upgrade. Can be \"OSD\" or \"CVE\".  # noqa: E501

        :return: The upgrade_type of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this UpgradePolicy.

        Upgrade type specify the type of the upgrade. Can be \"OSD\" or \"CVE\".  # noqa: E501

        :param upgrade_type: The upgrade_type of this UpgradePolicy.  # noqa: E501
        :type: str
        """

        self._upgrade_type = upgrade_type

    @property
    def version(self):
        """Gets the version of this UpgradePolicy.  # noqa: E501

        Version is the desired upgrade version.  # noqa: E501

        :return: The version of this UpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpgradePolicy.

        Version is the desired upgrade version.  # noqa: E501

        :param version: The version of this UpgradePolicy.  # noqa: E501
        :type: str
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
        if not isinstance(other, UpgradePolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpgradePolicy):
            return True

        return self.to_dict() != other.to_dict()