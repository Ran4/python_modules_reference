from distutils.core import setup

setup(
    name="Program example",
    license='LICENSE.txt',
    version='0.1.0',
    author='Nah Nah',
    author_email='nah@nah.com',
    description='CLI for Layke',
    #~ requires=[],
    packages=[
        "programname",
        "programname/sub",
    ],
    package_dir={
        "programname": "programname",
        "programname/sub": "programname/sub",
    },
)

