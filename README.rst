.. image:: https://gitlab.com/gitlab-automation-toolkit/gitlab-github-mirror-repo/badges/master/pipeline.svg
   :target: https://gitlab.com/gitlab-automation-toolkit/gitlab-github-mirror-repo
   :alt: Pipeline Status

.. image:: https://img.shields.io/pypi/l/gitlab-github-mirror-repo.svg
   :target: https://pypi.org/project/gitlab-github-mirror-repo/
   :alt: PyPI Project License

.. image:: https://img.shields.io/pypi/v/gitlab-github-mirror-repo.svg
   :target: https://pypi.org/project/gitlab-github-mirror-repo/
   :alt: PyPI Project Version

GitLab Github Mirror Repo
=========================

This is a simple Python cli script will first create a new repo on Gitlab and Github. Then it will create a push
mirror link between them. Where all changes on the Gitlab repo are pushed to the Github repo (Gitlab -> Github).

Usage
-----

To use this script you will need to have an access token for both Gitlab and Github, both must have permissions to
create new repositories on your behalf.

.. code-block:: bash

   gitlab_github_mirror_repo -l "xxxx" -h "xxx" -u https://gitlab.com -r test123 

.. code-block:: bash

  pip install gitlab-github-mirror-repo
  gitlab_github_mirror_repo --help

Usage: gitlab_github_mirror_repo [OPTIONS]

  A Python script used to mirror repos.

Options:
  -l, --gitlab-private-token TEXT
                                  Private GITLAB token, used to authenticate
                                  when calling the Gitlab API.  [required]
  -u, --gitlab-url TEXT           The GitLab URL i.e. gitlab.com.  [required]
  -h, --github-private-token TEXT
                                  Private GITHUB token, used to authenticate
                                  when calling the Github API.  [required]
  -r, --repo-name TEXT            The name of the repository on Github and
                                  Gitlab.  [required]
  --help                          Show this message and exit.

Docker
^^^^^^

You can also use the Docker image like:

.. code-block:: bash

   docker run gitlab-github-mirror-repo -l "xxxx" -h "xxx" -u https://gitlab.com -r test123 

Predefined Variables
^^^^^^^^^^^^^^^^^^^^
Please note some of the arguments can be filled in using environment variables.

* If ``--gitlab-private-token`` is not set the script will look for the ENV variable ``GITLAB_PRIVATE_TOKEN``
* If ``--github-private-token`` is not set it will look for for the ENV variable ``GITHUB_PRIVATE_TOKEN``

Setup Development Environment
=============================

.. code-block:: bash

  git clone git@gitlab.com:gitlab-automation-toolkit/gitlab-github-mirror-repo.git
  cd gitlab-github-mirror-repo
  pip install tox
  make install-venv
  source .venv/bin/activate
  make install-dev

Changelog
=========

You can find the `changelog here <https://gitlab.com/gitlab-automation-toolkit/gitlab-github-mirror-repo/blob/master/CHANGELOG.md>`_.
