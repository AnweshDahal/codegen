from setuptools import setup

setup(
    name="codegen",
    version="2020.APR",
    py_modules=['codegen'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        codegen=codegen:codegen
    '''
)