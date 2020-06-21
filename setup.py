from setuptools import find_packages
from setuptools import setup

setup(
    name="gitlab-github-mirror-repo",
    version="0.1.0 ",
    description="",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Haseeb Majid",
    author_email="hello@haseebmajid.dev",
    keywords="",
    license="Apache License",
    url="",
    python_requires="~=3.8",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    include_package_data=True,
    install_requires=["click>=7.0"],
    entry_points={"console_scripts": ["gitlab_github_mirror_repo = gitlab_github_mirror_repo.cli:cli"]},
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
