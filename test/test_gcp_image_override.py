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
from ocm_client.models.gcp_image_override import GCPImageOverride  # noqa: E501
from ocm_client.rest import ApiException

class TestGCPImageOverride(unittest.TestCase):
    """GCPImageOverride unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GCPImageOverride
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ocm_client.models.gcp_image_override.GCPImageOverride()  # noqa: E501
        if include_optional :
            return GCPImageOverride(
                kind = '0', 
                id = '0', 
                href = '0', 
                billing_model = ocm_client.models.billing_model_item.BillingModelItem(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    billing_model_type = '0', 
                    description = '0', 
                    display_name = '0', 
                    marketplace = '0', ), 
                image_id = '0', 
                product = ocm_client.models.product.Product(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    name = '0', ), 
                project_id = '0'
            )
        else :
            return GCPImageOverride(
        )

    def testGCPImageOverride(self):
        """Test GCPImageOverride"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()