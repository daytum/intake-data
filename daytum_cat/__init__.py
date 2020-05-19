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
tickers_by_state = wells.tickers_by_state
well_location_by_ticker_and_state = wells.well_location_by_ticker_and_state
well_location_by_api = wells.well_location_by_api
well_columns = wells.well_columns
production_by_state = production.production_by_state
production_by_api = production.production_by_api
production_columns = production.production_columns()
apis_with_production_data_by_state = production.apis_with_production_data_by_state
production_by_ticker_and_state = production.production_by_ticker_and_state
AI_grid = siesmic.AI_grid
poro_perm = petrophysical.poro_perm
MV_2D_200wells = petrophysical.MV_2D_200wells
unconv_MV = petrophysical.unconv_MV
sample_data_biased = petrophysical.sample_data_biased
sample_data_MV_biased = petrophysical.sample_data_MV_biased
sample_data = petrophysical.sample_data
porosity_1D = petrophysical.porosity_1D
