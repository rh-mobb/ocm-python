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
from openapi_client.models.inline_response20013 import InlineResponse20013  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20013(unittest.TestCase):
    """InlineResponse20013 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20013
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20013.InlineResponse20013()  # noqa: E501
        if include_optional :
            return InlineResponse20013(
                items = [
                    openapi_client.models.add_on_installation.AddOnInstallation(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        addon = openapi_client.models.add_on.AddOn(
                            kind = '0', 
                            id = '0', 
                            href = '0', 
                            common_annotations = {
                                'key' : '0'
                                }, 
                            common_labels = {
                                'key' : '0'
                                }, 
                            config = openapi_client.models.add_on_config.AddOnConfig(
                                kind = '0', 
                                id = '0', 
                                href = '0', 
                                add_on_environment_variables = [
                                    openapi_client.models.add_on_environment_variable.AddOnEnvironmentVariable(
                                        kind = '0', 
                                        id = '0', 
                                        href = '0', 
                                        name = '0', 
                                        value = '0', )
                                    ], 
                                secret_propagations = [
                                    openapi_client.models.add_on_secret_propagation.AddOnSecretPropagation(
                                        id = '0', 
                                        destination_secret = '0', 
                                        enabled = True, 
                                        source_secret = '0', )
                                    ], ), 
                            credentials_requests = [
                                openapi_client.models.credential_request.CredentialRequest(
                                    name = '0', 
                                    namespace = '0', 
                                    policy_permissions = [
                                        '0'
                                        ], 
                                    service_account = '0', )
                                ], 
                            description = '0', 
                            docs_link = '0', 
                            enabled = True, 
                            has_external_resources = True, 
                            hidden = True, 
                            icon = '0', 
                            install_mode = 'all_namespaces', 
                            label = '0', 
                            managed_service = True, 
                            name = '0', 
                            namespaces = [
                                openapi_client.models.add_on_namespace.AddOnNamespace(
                                    kind = '0', 
                                    id = '0', 
                                    href = '0', 
                                    annotations = {
                                        'key' : '0'
                                        }, 
                                    labels = {
                                        'key' : '0'
                                        }, 
                                    name = '0', )
                                ], 
                            operator_name = '0', 
                            parameters = [
                                openapi_client.models.add_on_parameter.AddOnParameter(
                                    kind = '0', 
                                    id = '0', 
                                    href = '0', 
                                    conditions = [
                                        openapi_client.models.add_on_requirement.AddOnRequirement(
                                            id = '0', 
                                            data = {
                                                'key' : None
                                                }, 
                                            enabled = True, 
                                            resource = '0', 
                                            status = openapi_client.models.add_on_requirement_status.AddOnRequirementStatus(
                                                error_msgs = [
                                                    '0'
                                                    ], 
                                                fulfilled = True, ), )
                                        ], 
                                    default_value = '0', 
                                    description = '0', 
                                    editable = True, 
                                    editable_direction = '0', 
                                    enabled = True, 
                                    name = '0', 
                                    options = [
                                        openapi_client.models.add_on_parameter_option.AddOnParameterOption(
                                            name = '0', 
                                            rank = 56, 
                                            requirements = [
                                                openapi_client.models.add_on_requirement.AddOnRequirement(
                                                    id = '0', 
                                                    enabled = True, 
                                                    resource = '0', )
                                                ], 
                                            value = '0', )
                                        ], 
                                    required = True, 
                                    validation = '0', 
                                    validation_err_msg = '0', 
                                    value_type = '0', )
                                ], 
                            requirements = [
                                openapi_client.models.add_on_requirement.AddOnRequirement(
                                    id = '0', 
                                    enabled = True, 
                                    resource = '0', )
                                ], 
                            resource_cost = 1.337, 
                            resource_name = '0', 
                            sub_operators = [
                                openapi_client.models.add_on_sub_operator.AddOnSubOperator(
                                    enabled = True, 
                                    operator_name = '0', 
                                    operator_namespace = '0', )
                                ], 
                            target_namespace = '0', 
                            version = openapi_client.models.add_on_version.AddOnVersion(
                                kind = '0', 
                                id = '0', 
                                href = '0', 
                                additional_catalog_sources = [
                                    openapi_client.models.additional_catalog_source.AdditionalCatalogSource(
                                        id = '0', 
                                        enabled = True, 
                                        image = '0', 
                                        name = '0', )
                                    ], 
                                available_upgrades = [
                                    '0'
                                    ], 
                                channel = '0', 
                                enabled = True, 
                                pull_secret_name = '0', 
                                source_image = '0', ), ), 
                        addon_version = openapi_client.models.add_on_version.AddOnVersion(
                            kind = '0', 
                            id = '0', 
                            href = '0', 
                            channel = '0', 
                            enabled = True, 
                            pull_secret_name = '0', 
                            source_image = '0', ), 
                        billing = openapi_client.models.add_on_installation_billing.AddOnInstallationBilling(
                            kind = '0', 
                            id = '0', 
                            href = '0', 
                            billing_marketplace_account = '0', 
                            billing_model = 'marketplace', ), 
                        creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        operator_version = '0', 
                        parameters = [
                            openapi_client.models.add_on_installation_parameter.AddOnInstallationParameter(
                                kind = '0', 
                                id = '0', 
                                href = '0', 
                                value = '0', )
                            ], 
                        state = 'deleting', 
                        state_description = '0', 
                        updated_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                page = 56, 
                size = 56, 
                total = 56
            )
        else :
            return InlineResponse20013(
        )

    def testInlineResponse20013(self):
        """Test InlineResponse20013"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
