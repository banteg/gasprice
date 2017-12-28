from setuptools import setup

setup(
    name='gasprice',
    version='1.1.1',
    description='predict ethereum gas price',
    url='https://github.com/banteg/gasprice',
    author='banteg',
    py_modules=[
        'gas_price',
    ],
    install_requires=[
        'sanic',
        'pandas',
        'web3>=4.0.0b4',
        'click',
        'retry',
    ],
    entry_points={
        'console_scripts': [
            'gasprice=gas_price:main',
        ]
    }
)
