# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.api.import_test_datetime_api import ImportTestDatetimeApi  # noqa: E501


class TestImportTestDatetimeApi(unittest.TestCase):
    """ImportTestDatetimeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ImportTestDatetimeApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_import_test_return_datetime(self) -> None:
        """Test case for import_test_return_datetime

        test date time  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
