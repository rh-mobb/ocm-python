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
from openapi_client.models.external_configuration import ExternalConfiguration  # noqa: E501
from openapi_client.rest import ApiException

class TestExternalConfiguration(unittest.TestCase):
    """ExternalConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExternalConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.external_configuration.ExternalConfiguration()  # noqa: E501
        if include_optional :
            return ExternalConfiguration(
                labels = [
                    openapi_client.models.label.Label(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        key = '0', 
                        value = '0', )
                    ], 
                manifests = [
                    openapi_client.models.manifest.Manifest(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        workloads = [
                            None
                            ], )
                    ], 
                syncsets = [
                    openapi_client.models.syncset.Syncset(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        resources = [
                            None
                            ], )
                    ]
            )
        else :
            return ExternalConfiguration(
        )

    def testExternalConfiguration(self):
        """Test ExternalConfiguration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
