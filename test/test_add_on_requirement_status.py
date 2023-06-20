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
from openapi_client.models.add_on_requirement_status import AddOnRequirementStatus  # noqa: E501
from openapi_client.rest import ApiException

class TestAddOnRequirementStatus(unittest.TestCase):
    """AddOnRequirementStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddOnRequirementStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.add_on_requirement_status.AddOnRequirementStatus()  # noqa: E501
        if include_optional :
            return AddOnRequirementStatus(
                error_msgs = [
                    '0'
                    ], 
                fulfilled = True
            )
        else :
            return AddOnRequirementStatus(
        )

    def testAddOnRequirementStatus(self):
        """Test AddOnRequirementStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
