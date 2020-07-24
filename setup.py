import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taxonomy_ranks",
    version="0.0.9",
    author='Guanliang MENG',
    author_email='linzhi2012@gmail.com',
    description="To get taxonomy ranks information with ETE3 from NCBI Taxonomy database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    url='https://github.com/linzhi2013/taxonomy_ranks',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['ete3', 'six'],

    entry_points={
        'console_scripts': [
            'taxaranks=taxonomy_ranks.get_taxonomy_rank_with_ete3_with_super_and_sub:main',
        ],
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ),
)