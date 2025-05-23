# Copyright 2019 AstroLab Software
# Author: Julien Peloton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import setuptools
from fink_science import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fink-science",
    version=__version__,
    author="JulienPeloton",
    author_email="peloton@lal.in2p3.fr",
    description="User-defined science module for the Fink broker.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://fink-broker.readthedocs.io/en/latest/",
    packages=setuptools.find_packages(),
    package_data={
        'fink_science': [
            'data/models/*.obj',
            'data/models/*.sav',
            'data/models/*.npy',
            'data/models/*.pkl',
            'data/models/*.csv',
            'data/models/*.tflite',
            'data/models/*.joblib',
            'data/models/snn_models/*/*.pt',
            'data/models/snn_models/*/*.json',
            'data/models/snn_models/*/*.txt',
            'data/models/snn_models/elasticc_binary_broad/*/*.pt',
            'data/models/snn_models/elasticc_binary_broad/*/*.json',
            'data/models/snn_models/elasticc_binary_broad/*/*.txt',
            'data/models/cats_models/cats_small_nometa_serial.keras',
            'data/models/t2/*/*.pb',
            'data/models/t2/*/*/variables*',
            'data/models/anomaly_detection/*.csv',
            'data/models/anomaly_detection/*.zip',
            'data/models/for_al_loop/*.pkl',
            'data/catalogs/*.parquet',
            'data/catalogs/*.fits',
            'data/catalogs/*.csv',
            'ztf/hostless_detection/config.json',
            'ztf/hostless_detection/config*.json'],
    },

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Unix",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
    ],
    project_urls={
        'Documentation': "https://fink-broker.readthedocs.io/en/latest/",
        'Source': 'https://github.com/astrolabsoftware/fink-science'
    },
)
