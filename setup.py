from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='fecittext',
    version='0.1',
    description='Text normalization tool. The helpful instrument for data-scientists.',
    url='https://github.com/fecitpotentiam/fecittext',
    install_requires=required,
    packages=find_packages(),
    zip_safe=False
)