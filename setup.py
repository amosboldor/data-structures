"""Setup mailroom madness module."""


from setuptools import setup

setup(
    name="Linked Lists",
    description="A Implementation a Singly-Linked List in Python",
    version=0.1,
    author=["Claire Gatenby", "Amos Boldor"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["linked_list", "stack", "doublelinkedlist"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
