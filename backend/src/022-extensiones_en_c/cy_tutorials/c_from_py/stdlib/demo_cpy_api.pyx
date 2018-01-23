# ===================================================

from cpython.version cimport (
	PY_VERSION_HEX,
    PY_MAJOR_VERSION,
    PY_MINOR_VERSION
)
from libc.stdio cimport printf
# https://github.com/cython/cython/blob/master/Cython/Includes/cpython/version.pxd

def demo_version():
    # Python version >= 3.2 final ?
    print(PY_VERSION_HEX >= 0x030200F0)  # Versión en hexadecimal

    printf("%d\n", PY_MAJOR_VERSION)
    printf("%d\n", PY_MINOR_VERSION)

