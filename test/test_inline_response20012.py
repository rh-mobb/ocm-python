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
from openapi_client.models.inline_response20012 import InlineResponse20012  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20012(unittest.TestCase):
    """InlineResponse20012 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20012
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20012.InlineResponse20012()  # noqa: E501
        if include_optional :
            return InlineResponse20012(
                items = [
                    openapi_client.models.addon_upgrade_policy.AddonUpgradePolicy(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        addon_id = '0', 
                        cluster_id = '0', 
                        next_run = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        schedule = '0', 
                        schedule_type = '0', 
                        upgrade_type = '0', 
                        version = '0', )
                    ], 
                page = 56, 
                size = 56, 
                total = 56
            )
        else :
            return InlineResponse20012(
        )

    def testInlineResponse20012(self):
        """Test InlineResponse20012"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()