"""
Reads config.ini and validates parameters.

Copyright (c) 2018, Battelle Memorial Institute

Open source under license BSD 2-Clause - see LICENSE and DISCLAIMER

@author:  Nino Zuljevic (nino.zuljevic@pnnl.gov)
"""

import datetime
import os
import untangle
import logger

class ReadData:

    # required XML files
    XML = ['constants.xml', 'powerzones.xml', 'technologies.xml']

    # required constants with [ lower bounds, upper bounds, type ] None if not applicable
    CNST = {'discount_rate': [0.0, 1.0, float],
            'carbon_tax': [0.0, 1.0, float],
            'carbon_tax_escalation': [0.0, 1.0, float],
            'tx_lifetime': [0, None, int],
            'interconnection_cost_gas': [0, None, float]}

    # required nodes, bounds, and types for technologies.xml [ lower bounds, upper bounds, type ]
    TECH = {'id': [0, None, int],
            'unit_size': [0, None, int],
            'capacity_factor': [0.0, 1.0, float],
            'variable_om': [0.0, None, float],
            'variable_cost_escalation_rate': [None, None, float],
            'heat_rate': [0.0, None, float],
            'fuel_price': [0.0, None, float],
            'fuel_price_escalation': [None, None, float],
            'fuel_co2_content': [0, None, float],
            'interconnection_cost_per_km': [0, None, int],
            'full_name': [None, None, str],
            'lifetime': [0, None, int],
            'category': [None, None, str],
            'fixed_om_2005': [0.0, None, float],
            'variable_om_2005': [None, None, float],
            'minimum_capacity': [0, None, int],
            'maintenance_requirement': [0, None, int],
            'forced_outage_rate': [0, None, float],
            'forced_outage_duration': [0, None, int],
            'efficiency_2005': [0.0, None, float],
            'siting_buffer': [0, None, int],
            'carbon_capture_rate': [0.0, None, float]}

    dictConstants = {}
    dictTechs = {}

    # acceptable values for the capacity factor fractions in the powerzones.xml file
    CF_VALS = ('0.9', '0.8', '0.5', '0.3', '0.1')

    def __init__(self):
        return None

    def read_constants(self, f):
        """
        Read constants.xml input data.

        :return 
        """
        obj = untangle.parse(f)

        root = obj.constants
        child = root.constant

        for v in child:
            e = self.CNST[v['name']]
            xp = e[2](v.cdata)
            self.dictConstants[v['name']] = xp

    def read_techs(self, f):
        """
        Read technologies.xml input data.

        :return:
        """
        obj = untangle.parse(f)

        root = obj.technologies
        child = root.technology

        for idx in range(len(child)):
            dictTech = {}
            for k in self.TECH.keys():
                
                e = self.TECH[k]
                v = eval('child[{0}].{1}'.format(idx, k))
                xp = e[2](v.cdata)
                dictTech[k] = xp
                if k == 'id':
                    tempKey = xp 
                    self.dictTechs[xp] = {}
            self.dictTechs[tempKey] = dictTech


#rdt = ReadData()
#rdt.read_constants('constants.xml')
#rdt.read_techs('technologies.xml')

