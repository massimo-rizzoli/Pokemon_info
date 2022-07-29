from setuptools import setup

with open("requirements.txt") as requirements:
    REQUIREMENTS = requirements.read().split('\n')
    print(REQUIREMENTS)

setup(
    name='Pokemon_info',
    version='1.0',
    description='Packaged version of \'EthanWadsworth/Pokemon_info\', a scraper for Pikalytics',
    author='Massimo Rizzoli',
    author_email='massimo.rizzoli99@gmail.com',
    packages=['pokemon_info'],
    install_requires=REQUIREMENTS,
)
