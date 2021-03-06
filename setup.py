import os

from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '0.8.2'

exec_dirs = [
    'src/pif/bin/',
]

execs = []
for exec_dir in exec_dirs:
    execs += [os.path.join(exec_dir, f) for f in os.listdir(exec_dir)]

setup(
    name='pif',
    version=version,
    description="Public IP address checker.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Internet"
    ],
    keywords='public ip checker, ip',
    author='Clinton',
    author_email='clintonmakosh72@gmail.com',
    url='https://https://github.com/Kingsly62/pif',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    include_package_data=True,
    package_data={
        'pif': execs,
    },
    scripts=['src/pif/bin/get-public-ip',],
    license='GPL 2.0/LGPL 2.1',
    install_requires=['requests>=1.2.3', 'argparse']
)
