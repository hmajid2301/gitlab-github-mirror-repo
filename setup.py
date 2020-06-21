from setuptools import find_packages
from setuptools import setup

setup(
    name="gitlab-github-mirror-repo",
    version="0.1.0 ",
    description="Script used to create repos on Gitlab and Github. Then create a push mirror link between them Gitlab -> Github.",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Haseeb Majid",
    author_email="hello@haseebmajid.dev",
    keywords="script,gitlab,github,mirror,automation",
    license="Apache License",
    url="https://gitlab.com/gitlab-automation-toolkit/gitlab-github-mirror-repo",
    python_requires="~=3.6",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    include_package_data=True,
    install_requires=["click>=7.0", "python-gitlab>=2.3.1", "pygithub>=1.51"],
    entry_points={"console_scripts": ["gitlab_github_mirror_repo = gitlab_github_mirror_repo.cli:cli"]},
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
