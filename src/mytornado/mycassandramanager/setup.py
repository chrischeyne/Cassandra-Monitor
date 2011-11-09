# -*- encoding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    raise ImportError('Please install clustershell >= 1.2.0')

setup(
        name='cassmanager',
        version='0.1.3',
        author='Chris Cheyne',
        author_email='chris.cheyne@hearst.co.uk',
        scripts=['installer.py'],
        install_requires=[
            'setuptools',
            'ClusterShell',
            ]
        )
