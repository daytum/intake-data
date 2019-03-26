#!/bin/bash

mkdir -p $PREFIX/share/intake/data
cp $SRC_DIR/data/*_production.csv $PREFIX/share/intake/data
cp $RECIPE_DIR/production.yml $PREFIX/share/intake/
cp $RECIPE_DIR/csv.yml $PREFIX/share/intake/
