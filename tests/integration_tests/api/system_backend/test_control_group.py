from unittest import TestCase, skipIf

from hvac.exceptions import VaultError
from tests import utils
from tests.utils.hvac_integration_test_case import HvacIntegrationTestCase


@skipIf(
    not utils.is_enterprise(), "Control Groups only supported with Enterprise Vault"
)
class TestControlGroup(HvacIntegrationTestCase, TestCase):
    def test_authorize_control_group(self):
        with self.assertRaises(VaultError):
            self.client.sys.authorize_control_group(accessor="invalid-accessor")

    def test_check_control_group_request(self):
        with self.assertRaises(VaultError):
            self.client.sys.check_control_group_request(accessor="invalid-accessor")
