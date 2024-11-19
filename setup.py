from setuptools import setup, find_packages

setup(
    name="mimicry",
    version="0.1",
    packages=find_packages(),
    install_requires=['aiohttp',
                      'requests'],
    entry_points={
        'console_scripts': [
            'mimicry = mimicry.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: UNIX',
    ],
)
