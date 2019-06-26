#!/bin/bash

mkdir -p $PREFIX/share/intake/data
cp $RECIPE_DIR/data/poro_perm.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/2D_MV_200wells.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/unconv_MV.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/Density_Por_data.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/data/sample_data_biased.csv $PREFIX/share/intake/data/
cp $RECIPE_DIR/us_production.yml $PREFIX/share/intake/
cp $RECIPE_DIR/us_wells.yml $PREFIX/share/intake/
cp $RECIPE_DIR/petrophysical.yml $PREFIX/share/intake/
