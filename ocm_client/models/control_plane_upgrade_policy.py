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


class ControlPlaneUpgradePolicy(object):
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
        'creation_timestamp': 'datetime',
        'enable_minor_version_upgrades': 'bool',
        'last_update_timestamp': 'datetime',
        'next_run': 'datetime',
        'schedule': 'str',
        'schedule_type': 'ScheduleType',
        'state': 'UpgradePolicyState',
        'upgrade_type': 'UpgradeType',
        'version': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'cluster_id': 'cluster_id',
        'creation_timestamp': 'creation_timestamp',
        'enable_minor_version_upgrades': 'enable_minor_version_upgrades',
        'last_update_timestamp': 'last_update_timestamp',
        'next_run': 'next_run',
        'schedule': 'schedule',
        'schedule_type': 'schedule_type',
        'state': 'state',
        'upgrade_type': 'upgrade_type',
        'version': 'version'
    }

    def __init__(self, kind=None, id=None, href=None, cluster_id=None, creation_timestamp=None, enable_minor_version_upgrades=None, last_update_timestamp=None, next_run=None, schedule=None, schedule_type=None, state=None, upgrade_type=None, version=None, local_vars_configuration=None):  # noqa: E501
        """ControlPlaneUpgradePolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._cluster_id = None
        self._creation_timestamp = None
        self._enable_minor_version_upgrades = None
        self._last_update_timestamp = None
        self._next_run = None
        self._schedule = None
        self._schedule_type = None
        self._state = None
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
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if enable_minor_version_upgrades is not None:
            self.enable_minor_version_upgrades = enable_minor_version_upgrades
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if next_run is not None:
            self.next_run = next_run
        if schedule is not None:
            self.schedule = schedule
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if state is not None:
            self.state = state
        if upgrade_type is not None:
            self.upgrade_type = upgrade_type
        if version is not None:
            self.version = version

    @property
    def kind(self):
        """Gets the kind of this ControlPlaneUpgradePolicy.  # noqa: E501

        Indicates the type of this object. Will be 'ControlPlaneUpgradePolicy' if this is a complete object or 'ControlPlaneUpgradePolicyLink' if it is just a link.  # noqa: E501

        :return: The kind of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ControlPlaneUpgradePolicy.

        Indicates the type of this object. Will be 'ControlPlaneUpgradePolicy' if this is a complete object or 'ControlPlaneUpgradePolicyLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this ControlPlaneUpgradePolicy.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ControlPlaneUpgradePolicy.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this ControlPlaneUpgradePolicy.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ControlPlaneUpgradePolicy.

        Self link.  # noqa: E501

        :param href: The href of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ControlPlaneUpgradePolicy.  # noqa: E501

        Cluster ID this upgrade policy for control plane is defined for.  # noqa: E501

        :return: The cluster_id of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ControlPlaneUpgradePolicy.

        Cluster ID this upgrade policy for control plane is defined for.  # noqa: E501

        :param cluster_id: The cluster_id of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this ControlPlaneUpgradePolicy.  # noqa: E501

        Timestamp for creation of resource.  # noqa: E501

        :return: The creation_timestamp of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this ControlPlaneUpgradePolicy.

        Timestamp for creation of resource.  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def enable_minor_version_upgrades(self):
        """Gets the enable_minor_version_upgrades of this ControlPlaneUpgradePolicy.  # noqa: E501

        Indicates if minor version upgrades are allowed for automatic upgrades (for manual it's always allowed).  # noqa: E501

        :return: The enable_minor_version_upgrades of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_minor_version_upgrades

    @enable_minor_version_upgrades.setter
    def enable_minor_version_upgrades(self, enable_minor_version_upgrades):
        """Sets the enable_minor_version_upgrades of this ControlPlaneUpgradePolicy.

        Indicates if minor version upgrades are allowed for automatic upgrades (for manual it's always allowed).  # noqa: E501

        :param enable_minor_version_upgrades: The enable_minor_version_upgrades of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: bool
        """

        self._enable_minor_version_upgrades = enable_minor_version_upgrades

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this ControlPlaneUpgradePolicy.  # noqa: E501

        Timestamp for last update that happened to resource.  # noqa: E501

        :return: The last_update_timestamp of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this ControlPlaneUpgradePolicy.

        Timestamp for last update that happened to resource.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: datetime
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def next_run(self):
        """Gets the next_run of this ControlPlaneUpgradePolicy.  # noqa: E501

        Next time the upgrade should run.  # noqa: E501

        :return: The next_run of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._next_run

    @next_run.setter
    def next_run(self, next_run):
        """Sets the next_run of this ControlPlaneUpgradePolicy.

        Next time the upgrade should run.  # noqa: E501

        :param next_run: The next_run of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: datetime
        """

        self._next_run = next_run

    @property
    def schedule(self):
        """Gets the schedule of this ControlPlaneUpgradePolicy.  # noqa: E501

        Schedule cron expression that defines automatic upgrade scheduling.  # noqa: E501

        :return: The schedule of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ControlPlaneUpgradePolicy.

        Schedule cron expression that defines automatic upgrade scheduling.  # noqa: E501

        :param schedule: The schedule of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def schedule_type(self):
        """Gets the schedule_type of this ControlPlaneUpgradePolicy.  # noqa: E501


        :return: The schedule_type of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: ScheduleType
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this ControlPlaneUpgradePolicy.


        :param schedule_type: The schedule_type of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: ScheduleType
        """

        self._schedule_type = schedule_type

    @property
    def state(self):
        """Gets the state of this ControlPlaneUpgradePolicy.  # noqa: E501


        :return: The state of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: UpgradePolicyState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ControlPlaneUpgradePolicy.


        :param state: The state of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: UpgradePolicyState
        """

        self._state = state

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this ControlPlaneUpgradePolicy.  # noqa: E501


        :return: The upgrade_type of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: UpgradeType
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this ControlPlaneUpgradePolicy.


        :param upgrade_type: The upgrade_type of this ControlPlaneUpgradePolicy.  # noqa: E501
        :type: UpgradeType
        """

        self._upgrade_type = upgrade_type

    @property
    def version(self):
        """Gets the version of this ControlPlaneUpgradePolicy.  # noqa: E501

        Version is the desired upgrade version.  # noqa: E501

        :return: The version of this ControlPlaneUpgradePolicy.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ControlPlaneUpgradePolicy.

        Version is the desired upgrade version.  # noqa: E501

        :param version: The version of this ControlPlaneUpgradePolicy.  # noqa: E501
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
        if not isinstance(other, ControlPlaneUpgradePolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlPlaneUpgradePolicy):
            return True

        return self.to_dict() != other.to_dict()
