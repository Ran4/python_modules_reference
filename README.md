Showcases

Directory setup:

```
    setup.py
    programname/
        __init__.py
        __main__.py
        sub/
            __init__.py
            subfile.py
```

```python
# setup.py
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
```

```python
# __main__.py
from programname.main_helper import red
from programname.sub.subfile import subfunc
if __name__ == "__main__":
    red("from main")
```

```python
# main_helper.py
print("main_helper")

def red(x):
    print("from red:", x)
```

```python
# sub/subfile.py
from programname.main_helper import red

def subfunc():
    red("from subfunc")
```

