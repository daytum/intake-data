#!/bin/bash

mkdir -p $CONDA_PREFIX/share/intake/data
cp $RECIPE_DIR/data/poro_perm.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/2D_MV_200wells.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/unconv_MV.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/unconv_MV_v4.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/Density_Por_data.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/sample_data.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/sample_data_biased.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/sample_data_MV_biased.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/sample_data_12.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/AI_grid.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/1D_Porosity.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/us_production.yaml $PREFIX/share/intake/
cp $RECIPE_DIR/us_wells.yaml $PREFIX/share/intake/
cp $RECIPE_DIR/petrophysical.yaml $PREFIX/share/intake/
cp $RECIPE_DIR/siesmic.yaml $PREFIX/share/intake/
