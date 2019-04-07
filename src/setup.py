from setuptools import setup

# Installs requirements and sets the environment variable
setup(
    name='gutec',
    version='0.1',
    py_modules=['cli'],
    install_requires=['Click', 'treelib'],
    entry_points='''
        [console_scripts]
        gutec=cli:cli
    ''',
)