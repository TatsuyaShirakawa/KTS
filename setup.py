from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext = Extension('cpd_nonlin', sources=['cpd_nonlin.pyx'], include_dirs=['.', np.get_include()])
setup(name='cpd_nonlin', ext_modules=cythonize([ext]))
