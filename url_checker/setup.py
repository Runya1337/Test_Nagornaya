# setup.py

from setuptools import setup, find_packages

setup(
    name='url_checker',
    version='1.0.0',
    description='CLI-приложение для проверки доступных HTTP-методов для заданных URL.',
    author='Ainur Nurtdinov',
    author_email='ainurnurtdinov1337@gmail.com',
    url='https://github.com/Runya1337/Test_Nagornaya',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.7.4',
    ],
    entry_points={
        'console_scripts': [
            'url_checker=url_checker.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
