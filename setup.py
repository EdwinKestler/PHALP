#!/usr/bin/env python
from setuptools import find_packages, setup
# from pip.req import parse_requirements

setup(
    name='phalp',
    version='0.1.3',    
    description='PHALP: A Python package for People Tracking in 3D',
    url='https://github.com/brjathu/PHALP',
    author='Jathushan Rajasegaran',
    author_email='jathushan@berkeley.edu',
    license='MIT License',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
            "opencv-python==4.8.0.76",
            "joblib==1.4.2",
            "scikit-learn==1.2.2",
            "pyrender==0.1.45",
            "dill==0.3.8",
            "rich==13.7.1",
            "einops==0.8.0",
            "scenedetect[opencv]==0.6.4",
            "hydra-core==1.3.2",
            "timm==1.0.7",
            "av==12.2.0",
            "smplx==0.1.28",
            "numpy==1.25.2",
            "detectron2 @ git+https://github.com/EdwinKestler/detectron2.git",
            "pytube @ git+https://github.com/EdwinKestler/pytube.git",
            "pyopengl @ git+https://github.com/EdwinKestler/pyopengl.git",
            "chumpy @ git+https://github.com/EdwinKestler/chumpy", # smplx dependency
            "neural-renderer-pytorch @ git+https://github.com/EdwinKestler/NMR.git",
        ],
    extras_require={
        'all': [
            "hmr2 @ git+https://github.com/EdwinKestler/4D-Humans.git",
        ],
        'blur': [
            'facenet_pytorch==2.5.2'
        ]
    },
    dependency_links=[]
)
