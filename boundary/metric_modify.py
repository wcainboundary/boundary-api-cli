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
import json
import logging

from boundary import MetricCommon

"""
Common Base class for defining and update metric definitions
"""
class MetricModify (MetricCommon):
     
    def __init__(self):
        """
        """
        MetricCommon.__init__(self)
        self.metricName = None
        self.displayName = None
        self.displayNameShort = None
        self.description = None
        self.aggregate = None
        self.unit = None
        self.resolution = None
        self.isDisabled = None
        
    def addArguments(self):
        """
        Add the specific arguments of this CLI
        """
        MetricCommon.addArguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metricName', action='store',
                                 required=True, metavar='metric_name', help='Metric identifier')
        self.parser.add_argument('-d', '--display-name', dest='displayName', action='store',
                                 required=True, metavar='display_name', help='Metric display name')
        self.parser.add_argument('-s', '--display-name-short', dest='displayNameShort', action='store',
                                 required=True, metavar='display_short_name', help='Metric short display name')
        self.parser.add_argument('-i', '--description', dest='description', action='store',
                                 metavar='description', help='Metric description')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate', action='store',
                                 required=True, choices=['AVG', 'MAX', 'MIN', 'SUM'],
                                 help='Metric default aggregate')
        self.parser.add_argument('-u', '--unit', dest='unit', action='store',
                                 required=True, choices=['percent', 'number', 'bytecount', 'duration'],
                                 help='Metric unit')
        self.parser.add_argument('-r', '--resolution', dest='resolution', action='store', metavar='resolution',
                                 help='Metric default resolution')
        self.parser.add_argument('-x', '--is-disabled', dest='isDisabled', action='store', default=None,
                                 choices=['yes', 'no'], help='Enable or disable the metric definition')
        
    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        MetricCommon.getArguments(self)
        
        if self.args.metricName is not None:
            self.metricName = self.args.metricName
            
        if self.args.displayName is not None:
            self.displayName = self.args.displayName
                        
        if self.args.displayNameShort is not None:
            self.displayNameShort = self.args.displayNameShort

        if self.args.description is not None:
            self.description = self.args.description
                    
        if self.args.aggregate is not None:
            self.aggregate = self.args.aggregate
            
        if self.args.unit is not None:
            self.unit = self.args.unit
            
        if self.args.resolution is not None:
            self.resolution = self.args.resolution

        if self.args.isDisabled is not None:
            self.isDisabled = self.args.isDisabled
       
        data = {}
        if self.metricName is not None:
            data['name'] = self.metricName
        if self.displayName is not None:
            data['displayName'] = self.displayName
        if self.displayNameShort is not None:
            data['displayNameShort'] = self.displayNameShort
        if self.description is not None:
            data['description'] = self.description
        if self.aggregate is not None:
            data['defaultAggregate'] = self.aggregate
        if self.unit is not None:
            data['unit'] = self.unit
        if self.resolution is not None:
            data['defaultResolutionMS'] = self.resolution
        if self.isDisabled is not None:
            data['isDisabled'] = True if self.isDisabled == 'yes' else False

        self.path = "v1/metrics/{0}".format(self.metricName)
        self.data = json.dumps(data, sort_keys=True)
        self.headers = {'Content-Type': 'application/json', "Accept": "application/json"}
