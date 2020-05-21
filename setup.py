#!/usr/bin/env python

# Copyright 2019-2020 Daytum

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup, find_packages

setup(
    name='daytum-data',
    version='0.1.0',
    description="Intake data package for Daytum classes",
    packages=find_packages(),
    package_data={'': ['*.yaml']},
    include_package_data=True,
    install_requires=['intake>=0.5.5', 'intake-sql', 'psycopg2-binary'],
    zip_safe=False,
    entry_points={
        'intake.catalogs': [
            'wells=daytum_cat:wells',
            'production=daytum_cat:production',
            'petrophysical=daytum_cat:petrophysical',
            'siesmic=daytum_cat:siesmic',
            'AI_grid=daytum_cat:AI_grid',
            'poro_perm=daytum_cat:poro_perm',
            'MV_2D_200wells=daytum_cat:MV_2D_200wells',
            'unconv_MV=daytum_cat:unconv_MV',
            'sample_data_biased=daytum_cat:sample_data_biased',
            'sample_data_MV_biased=daytum_cat:sample_data_MV_biased',
            'sample_data=daytum_cat:sample_data',
            'porosity_1D=daytum_cat:porosity_1D'
        ]
    }
)
