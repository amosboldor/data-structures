"""Setup datastructures module."""


from setuptools import setup

setup(
    name="Data structures",
    description="The implementation of data structures in Python",
    version=0.1,
    author=["Claire Gatenby", "Amos Boldor"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["linked_list", "stack", "doublelinkedlist", "queue"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
