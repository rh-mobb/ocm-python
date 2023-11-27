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
from ocm_client.models.awssts_account_role import AWSSTSAccountRole  # noqa: E501
from ocm_client.rest import ApiException

class TestAWSSTSAccountRole(unittest.TestCase):
    """AWSSTSAccountRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AWSSTSAccountRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ocm_client.models.awssts_account_role.AWSSTSAccountRole()  # noqa: E501
        if include_optional :
            return AWSSTSAccountRole(
                items = [
                    ocm_client.models.awssts_role.AWSSTSRole(
                        hcp_managed_policies = True, 
                        is_admin = True, 
                        managed_policies = True, 
                        arn = '0', 
                        type = '0', 
                        role_version = '0', )
                    ], 
                prefix = '0'
            )
        else :
            return AWSSTSAccountRole(
        )

    def testAWSSTSAccountRole(self):
        """Test AWSSTSAccountRole"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
