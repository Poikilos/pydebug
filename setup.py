import setuptools
import sys
# - For the example on which this was based, see
#   https://github.com/poikilos/nopackage/blob/master/setup.py
#   which was based on:
#   - https://github.com/poikilos/pypicolcd/blob/master/setup.py
#   - (For nose) https://github.com/poikilos/mgep/blob/master/setup.py

python_mr = sys.version_info.major
# versionedModule = {}
# versionedModule['urllib'] = 'urllib'
# if python_mr == 2:
#     versionedModule['urllib'] = 'urllib2'
long_description = ""
with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PyDebug',
    version='1.5.5',
    description="View Python debug (pdb) info in a GUI Window!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Debuggers',
    ],
    keywords='python debugging GUI tkinter',
    url="https://github.com/poikilos/pydebug",
    author="Daniel Larsson, Ulrich Herold, Jake Gustafson",
    author_email='dlarsson@sw.seisy.abb.se, Ulrich.Herold@ProConsult-Online.com, 7557867+poikilos@users.noreply.github.com',
    license='Other/Proprietary License',
    # packages=setuptools.find_packages(),
    # packages=['rotocanvas'],
    # include_package_data=True,  # look for MANIFEST.in (See rotocanvas for an example)
    # scripts=['example'] ,
    # See <https://stackoverflow.com/questions/27784271/
    # how-can-i-use-setuptools-to-generate-a-console-scripts-entry-
    # point-which-calls>
    # entry_points={
    #     'gui_scripts': [
    #         '=pydebug:main',
    #     ],
    # },
    install_requires=[
        'regex',
        'tkinter',
    ],
    #     versionedModule['urllib'],
    # ^ "ERROR: Could not find a version that satisfies the requirement urllib (from nopackage) (from versions: none)
    # ERROR: No matching distribution found for urllib"
    # test_suite='nose.collector',
    # tests_require=['nose', 'nose-cover3'],
    zip_safe=False, # It can't run zipped due to needing data files.
 )
