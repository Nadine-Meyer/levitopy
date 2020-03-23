from setuptools import setup, find_packages
from levitopy import __version__ as current_version

# NOTES for updating this file:
# 1) for version update in the levitopy.__init__
# 2) update the following comment_on_changes
comment_on_changes = 'First version'

setup(
    name='levitopy',
    version=current_version,
    packages=find_packages(),
    url='https://gitlab.icfo.net/pno-trappers/levitopy',
    license='BSD-2-Clause',
    author='pn-trappers (Jan Gieseler)',
    author_email='JanGie@pm.me',
    description=comment_on_changes,
    keywords='levitodynamics, data analysis',
    long_description='Levitodynamics theory, fitting and simulation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: 2-Clause BSD License',
        'Development Status :: 4 - Beta',
        'Environment :: Linux (Ubuntu)',
        ],
    # install_requires=[
    #     'matplotlib',
    #     'pandas',
    #     'numpy',
    #     'scipy',
    #     'lmfit',
    #     'uncertainties',
    # ]
    # test_suite='nose.collector',
    # tests_require=['nose'],
    # python_requires='>=3.6',
    # entry_points={
    #     'console_scripts': ['pylabcontrol = pylabcontrol.gui.launch_gui:launch_gui']
    # }
)
