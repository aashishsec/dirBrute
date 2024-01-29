from setuptools import setup, find_packages

setup(
    name='DirBrute',
    version='1.0.2',
    description='DirBrute is a tool designed to efficiently probe for alive endpoints from a provided wordlist list.',
    author='Bande Aashish',
    url='https://github.com/aashishsec/dirBrute',
    packages=find_packages(),
    install_requires=[
        'requests',
        'httpx',
        'colorama',
    ],
    extras_require={
        'dev': ['argparse', 'concurrent.futures'],
    },
    entry_points={
        'console_scripts': [
            'dirbrute=dirbrute.dirbrute:main',
        ],
    },
)
