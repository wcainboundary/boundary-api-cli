#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from boundary import ApiCli


class PluginBase(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "GET"
        self.path = "v1/plugins"
        self.pluginName = None

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--plugin-name', dest='pluginName', action='store', required=True,
                                 metavar="plugin_name", help='Plugin name')

    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        ApiCli.getArguments(self)
        if self.args.pluginName != None:
            self.pluginName = self.args.pluginName
