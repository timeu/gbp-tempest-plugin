from tempest import clients
from tempest import config
from tempest.lib import auth

from gbp_tempest_plugin.services.gbp.v2.json.policy_action_client import PolicyActionClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_classifier_client import PolicyClassifierClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_rule_client import PolicyRuleClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_rule_set_client import PolicyRuleSetClient
from gbp_tempest_plugin.services.gbp.v2.json.l3_policy_client import L3PolicyClient
from gbp_tempest_plugin.services.gbp.v2.json.l2_policy_client import L2PolicyClient
from gbp_tempest_plugin.services.gbp.v2.json.app_policy_group_client import AppPolicyGroupClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_target_group_client import PolicyTargetGroupClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_target_client import PolicyTargetClient
from gbp_tempest_plugin.services.gbp.v2.json.network_service_policy_client import NetworkServicePolicyClient
from gbp_tempest_plugin.services.gbp.v2.json.external_policy_client import ExternalPolicyClient
from gbp_tempest_plugin.services.gbp.v2.json.external_segment_client import ExternalSegmentClient
from gbp_tempest_plugin.services.gbp.v2.json.nat_pool_client import NATPoolClient
from gbp_tempest_plugin.services.gbp.v2.json.servicechain_spec_client import ServicechainSpecClient
from gbp_tempest_plugin.services.gbp.v2.json.service_profile_client import ServiceProfileClient

CONF = config.CONF

class ManagerV2(clients.Manager):

    def __init__(self, credentials=None):
        super(ManagerV2, self).__init__(credentials)
        self._init_clients(self._get_params())

    def _init_clients(self, params):
        self.policy_action_client  = PolicyActionClient(**params)
        self.policy_classifier_client = PolicyClassifierClient(**params)
        self.policy_rule_client = PolicyRuleClient(**params)
        self.policy_rule_set_client = PolicyRuleSetClient(**params)
        self.l3_policy_client = L3PolicyClient(**params)
        self.l2_policy_client = L2PolicyClient(**params)
        self.app_policy_group_client = AppPolicyGroupClient(**params)
        self.policy_target_group_client = PolicyTargetGroupClient(**params)
        self.policy_target_client = PolicyTargetClient(**params)
        self.network_service_policy_client = NetworkServicePolicyClient(**params)
        self.external_segment_client = ExternalSegmentClient(**params)
        self.external_policy_client = ExternalPolicyClient(**params)
        self.nat_pool_client = NATPoolClient(**params)
        self.servicechain_spec_client = ServicechainSpecClient(**params)
        self.service_profile_client = ServiceProfileClient(**params)

    def _get_params(self):
        params = dict(self.default_params)
        params.update({
            'auth_provider': self.auth_provider,
            'service': CONF.network.catalog_type,
            'region': CONF.identity.region,
            'endpoint_type': CONF.network.endpoint_type,
        })
        return params

