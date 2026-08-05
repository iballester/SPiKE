# Copyright (c) Facebook, Inc. and its affiliates.
# 
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import glob
import os

''' Modified based on: https://github.com/hehefan/P4Transformer/ '''

_root_dir = os.path.dirname(os.path.abspath(__file__))
_ext_src_root = os.path.join(_root_dir, "_ext_src")
_ext_sources = glob.glob(os.path.join(_ext_src_root, "src", "*.cpp")) + glob.glob(
    os.path.join(_ext_src_root, "src", "*.cu")
)
_ext_headers = glob.glob(os.path.join(_ext_src_root, "include", "*"))

headers = "-I" + os.path.join(_ext_src_root, 'include')
print("!!!!!!", headers)

setup(
    name='pointnet2',
    ext_modules=[
        CUDAExtension(
            name='pointnet2._ext',
            sources=_ext_sources,
            extra_compile_args={
                "cxx": ["-O2", headers],
                "nvcc": ["-O2", headers],
            }, 
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
