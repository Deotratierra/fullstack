#!/bin/sh

git clone https://github.com/numpy/numpy.git
cd numpy
sudo python3 setup.py build_ext --inplace -j 4
sudo python3 setup.py install
cd ..
sudo rm -rf numpy

NUMPY_VERSION=$(python3 -c "import numpy as np;print(np.__version__)")
echo "Numpy version $NUMPY_VERSION instalado correctamente."

