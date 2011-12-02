# -*- encoding: utf-8 -*-
# FIXME: include pip_requires.txt for pip -r pip_requires.txt
try:
    from setuptools import setup
except ImportError:
    raise ImportError('Please install clustershell >= 1.2.0')

setup(
        name='cassmanager',
        version='0.1.5',
        author='Chris Cheyne',
        author_email='chris@cheynes.org',
        scripts=['installer.py'],
        install_requires=[
            'setuptools',
            'ClusterShell',
            ]
        )
