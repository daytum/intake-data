#!/usr/bin/env python

# Copyright 2020 Daytum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
import unittest
import datetime
from intake import cat
import numpy as np


class TestDaytumData(unittest.TestCase):

    def setUp(self):
        self.schema = 'staging'
        self.subdomain = 'premium-west'
        self.database = 'db'


    def test_production_by_api(self):

        df = cat.production.production_by_api(api='33001000050000', 
                table='production_nd_20190202034444',
                subdomain=self.subdomain, 
                schema=self.schema, 
                database=self.database).read()

        assert df.loc[0, 'date'] == datetime.date(1994, 10, 1)
        assert len(df) == 8
        np.testing.assert_allclose(df['volume_oil_formation_bbls'].values, np.array([237, 58, 42, 20, 150, 30, 30, 30]))

    # def test_production_by_state(self):

        # df = cat.production.production_by_state(state='NM', 
                # table='production_nm_20190202021002',
                # subdomain=self.subdomain, 
                # schema=self.schema, 
                # database=self.database).read()

        # np.testing.assert_allclose(df.iloc[0:24, 'volume_gas_formation_mcf'], np.array([225, 174, 222, 210, 3, 12, 26, 104, 159, 108, 282, 298, 260, 252, 208, 91, 153, 175, 132, 75, 17, 26, 310, 212]))

if __name__ == "__main__":
    unittest.main()
