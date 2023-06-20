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
from openapi_client.models.cloud_region import CloudRegion  # noqa: E501
from openapi_client.rest import ApiException

class TestCloudRegion(unittest.TestCase):
    """CloudRegion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CloudRegion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.cloud_region.CloudRegion()  # noqa: E501
        if include_optional :
            return CloudRegion(
                kind = '0', 
                id = '0', 
                href = '0', 
                ccs_only = True, 
                cloud_provider = openapi_client.models.cloud_provider.CloudProvider(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    display_name = '0', 
                    name = '0', ), 
                display_name = '0', 
                enabled = True, 
                name = '0', 
                supports_hypershift = True, 
                supports_multi_az = True
            )
        else :
            return CloudRegion(
        )

    def testCloudRegion(self):
        """Test CloudRegion"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()