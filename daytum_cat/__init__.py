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
import intake
import os

here = os.path.abspath(os.path.dirname(__file__))

# the catalog is a YAML file in the same directory as this init file
wells = intake.open_catalog(os.path.join(here, 'us_wells.yaml'))
production = intake.open_catalog(os.path.join(here, 'us_production.yaml'))
petrophysical = intake.open_catalog(os.path.join(here, 'petrophysical.yaml'))
siesmic = intake.open_catalog(os.path.join(here, 'siesmic.yaml'))

# register data sources
AI_grid = siesmic.AI_grid
poro_perm = petrophysical.poro_perm
MV_2D_200wells = petrophysical.MV_2D_200wells
unconv_MV = petrophysical.unconv_MV
unconv_MV_v4 = petrophysical.unconv_MV_v4
sample_data_biased = petrophysical.sample_data_biased
sample_data_MV_biased = petrophysical.sample_data_MV_biased
sample_data = petrophysical.sample_data
sample_data_12 = petrophysical.sample_data_12
porosity_1D = petrophysical.porosity_1D
nonlinear_facies_v1 = petrophysical.nonlinear_facies_v1
nonlinear_facies_v2 = petrophysical.nonlinear_facies_v2
random_parabola = petrophysical.random_parabola
stochastic_poro_perm = petrophysical.stochastic_poro_perm
