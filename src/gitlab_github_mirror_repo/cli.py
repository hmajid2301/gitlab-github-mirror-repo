# -*- coding: utf-8 -*-
r"""This script will first create a repo on Gitlab and Github. Then it will create a push mirror link from
Gitlab -> Github.

Example:
    ::
        $ pip install -e .
        $ gitlab_github_mirror_repo -l "xxxx" -h "yyy" -u https://gitlab.com -r test123

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

"""

__VERSION__ = "0.1.1"

import sys

import click
import gitlab
from github import Github
from github.GithubException import GithubException
from gitlab import GitlabCreateError
from gitlab import GitlabHttpError


@click.command()
@click.option(
    "--gitlab-private-token",
    "-l",
    envvar="GITLAB_PRIVATE_TOKEN",
    required=True,
    help="Private GITLAB token, used to authenticate when calling the Gitlab API.",
)
@click.option("--gitlab-url", "-u", envvar="GITLAB_URL", required=True, help="The GitLab URL i.e. gitlab.com.")
@click.option(
    "--github-private-token",
    "-h",
    envvar="GITHUB_PRIVATE_TOKEN",
    required=True,
    help="Private GITHUB token, used to authenticate when calling the Github API.",
)
@click.option("--repo-name", "-r", required=True, help="The name of the repository on Github and Gitlab.")
def cli(gitlab_private_token, gitlab_url, github_private_token, repo_name):
    """A Python script used to mirror repos."""
    gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_private_token)
    gh = Github(github_private_token)

    try:
        github_project = gh.get_user().create_repo(repo_name)
    except GithubException as e:
        print(f"Failed to create repo on Github, {e}")
        sys.exit(1)

    try:
        gitlab_project = gl.projects.create({"name": repo_name})
    except (GitlabCreateError, GitlabHttpError) as e:
        print(f"Failed to create repo on Gitlab, {e}")
        sys.exit(1)

    github_user = github_project.owner.login
    mirror_url = f"https://{github_user}:{github_private_token}@github.com/{github_user}/{repo_name}.git"
    gitlab_project.remote_mirrors.create({"url": mirror_url, "enabled": True})
    print("Successfully created repos on Github and Gitlab. Also added push mirror from Gitlab -> Github.")
