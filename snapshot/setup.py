from setuptools import setup, find_packages

setup(
    name='snapshot',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snapshot = monitor.cli:main'
        ]
    },
    install_requires=[
        'psutil',
    ],
    author='Ihor Bytskalo',
    description='System monitoring tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
