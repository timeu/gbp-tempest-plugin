# Copyright 2015
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import os

from tempest import config
from tempest.test_discover import plugins

from gbp_tempest_plugin import config as project_config


class GbpTempestPlugin(plugins.TempestPlugin):
    def load_tests(self):
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "gbp_tempest_plugin/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        config.register_opt_group(conf, project_config.service_available_group, project_config.ServiceAvailableGroup)
        config.register_opt_group(conf, project_config.gbp_group, project_config.GbpGroup)
        config.register_opt_group(conf, project_config.gbp_feature_group, project_config.GbpFeatureGroup)

    def get_opt_lists(self):
        return [
           (project_config.service_available_group.name, project_config.ServiceAvailableGroup),
           (project_config.gbp_group.name, project_config.GbpGroup),
           (project_config.gbp_feature_group.name, project_config.GbpFeatureGroup),
        ]

    def get_service_clients(self):
        gbp_config = config.service_client_config('gbp')
        v2_params = {
            'name': 'gbp_v2',
            'service_version': 'gbp.v2',
            'module_path': 'gbp_tempest_plugin.services.gbp.v2',
            'client_names': ['PolicyActionClient', 'PolicyClassifierClient', 'PolicyRuleClient', 'PolicyRuleSetClient', 
                             'L3PolicyClient', 'L2PolicyClient', 'AppPolicyGroupClient', 'PolicyTargetGroupClient', 
                             'PolicyTargetClient', 'NetworkServicePolicyClient', 'ExternalPolicyClient', 'ExternalSegmentClient',
                             'NATPoolClient', 'ServiceChainSpecClient', 'ServiceProfileClient']
        }
        v2_params.update(gbp_config)
        return [v2_params]
