#!/bin/sh

sudo pip3 install cython
git clone https://github.com/pandas-dev/pandas.git
cd pandas
sudo python3 setup.py install
cd ..
rm -rf pandas

PANDAS_VERSION=$(python3 -c "import pandas as pd;print(pd.__version__)")
echo "Pandas version $PANDAS_VERSION instalado correctamente."