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

import ocm_client
from ocm_client.models.autoscaler_resource_limits_gpu_limit import AutoscalerResourceLimitsGPULimit  # noqa: E501
from ocm_client.rest import ApiException

class TestAutoscalerResourceLimitsGPULimit(unittest.TestCase):
    """AutoscalerResourceLimitsGPULimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AutoscalerResourceLimitsGPULimit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ocm_client.models.autoscaler_resource_limits_gpu_limit.AutoscalerResourceLimitsGPULimit()  # noqa: E501
        if include_optional :
            return AutoscalerResourceLimitsGPULimit(
                range = ocm_client.models.resource_range.ResourceRange(
                    max = 56, 
                    min = 56, ), 
                type = '0'
            )
        else :
            return AutoscalerResourceLimitsGPULimit(
        )

    def testAutoscalerResourceLimitsGPULimit(self):
        """Test AutoscalerResourceLimitsGPULimit"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
