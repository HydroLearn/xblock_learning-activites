"""Setup for xblock-hl-learning-activities XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='xblock-hl_learning_activities',
    version='0.1',
    author="cRivet",
    description='Custom Xblock for generating a learning activity for use in HydroLearn platform. (using hl_text)',
    packages=[
        'hl_learning_activities',
    ],
    install_requires=[
        'XBlock',
        'xblock-hl-text',
    ],
    entry_points={
        'xblock.v1': [
            'hl_learning_activities = hl_learning_activities:HL_LearningObjs_XBlock',
        ]
    },
    package_data=package_data("hl_learning_objs", ["static", "public", "templates"]),
)