# coding: utf-8

"""
    clusters_mgmt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: ocm-feedback@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.cluster_nodes import ClusterNodes  # noqa: E501
from openapi_client.rest import ApiException

class TestClusterNodes(unittest.TestCase):
    """ClusterNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClusterNodes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.cluster_nodes.ClusterNodes()  # noqa: E501
        if include_optional :
            return ClusterNodes(
                autoscale_compute = openapi_client.models.machine_pool_autoscaling.MachinePoolAutoscaling(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    max_replicas = 56, 
                    min_replicas = 56, ), 
                availability_zones = [
                    '0'
                    ], 
                compute = 56, 
                compute_labels = {
                    'key' : '0'
                    }, 
                compute_machine_type = openapi_client.models.machine_type.MachineType(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    ccs_only = True, 
                    cpu = openapi_client.models.value.Value(
                        unit = '0', 
                        value = 1.337, ), 
                    category = 'accelerated_computing', 
                    cloud_provider = openapi_client.models.cloud_provider.CloudProvider(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        display_name = '0', 
                        name = '0', ), 
                    generic_name = '0', 
                    memory = openapi_client.models.value.Value(
                        unit = '0', 
                        value = 1.337, ), 
                    name = '0', 
                    size = 'large', ), 
                compute_root_volume = openapi_client.models.root_volume.RootVolume(
                    aws = openapi_client.models.aws_volume.AWSVolume(
                        iops = 56, 
                        size = 56, ), 
                    gcp = openapi_client.models.gcp_volume.GCPVolume(
                        size = 56, ), ), 
                infra = 56, 
                infra_machine_type = openapi_client.models.machine_type.MachineType(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    ccs_only = True, 
                    cpu = openapi_client.models.value.Value(
                        unit = '0', 
                        value = 1.337, ), 
                    category = 'accelerated_computing', 
                    cloud_provider = openapi_client.models.cloud_provider.CloudProvider(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        display_name = '0', 
                        name = '0', ), 
                    generic_name = '0', 
                    memory = openapi_client.models.value.Value(
                        unit = '0', 
                        value = 1.337, ), 
                    name = '0', 
                    size = 'large', ), 
                master = 56, 
                master_machine_type = openapi_client.models.machine_type.MachineType(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    ccs_only = True, 
                    cpu = openapi_client.models.value.Value(
                        unit = '0', 
                        value = 1.337, ), 
                    category = 'accelerated_computing', 
                    cloud_provider = openapi_client.models.cloud_provider.CloudProvider(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        display_name = '0', 
                        name = '0', ), 
                    generic_name = '0', 
                    memory = openapi_client.models.value.Value(
                        unit = '0', 
                        value = 1.337, ), 
                    name = '0', 
                    size = 'large', ), 
                security_group_filters = [
                    openapi_client.models.machine_pool_security_group_filter.MachinePoolSecurityGroupFilter(
                        name = '0', 
                        value = '0', )
                    ], 
                total = 56
            )
        else :
            return ClusterNodes(
        )

    def testClusterNodes(self):
        """Test ClusterNodes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
