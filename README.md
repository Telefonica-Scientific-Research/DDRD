
# Python Project Template

A low dependency and really simple to start project template for Python Projects.

### HOW TO USE THIS TEMPLATE

> **DO NOT FORK** this is meant to be used from **[Use this template](https://github.com/maviva/python-project-silver-template/generate)** feature.

1. Click on **[Use this template](https://github.com/maviva/python-project-silver-template/generate)**
3. Give a name to your project  
   (e.g. `my_awesome_project` recommendation is to use all lowercase and underscores separation for repo names.)
3. Wait until the first run of CI finishes  
   (Github Actions will process the template and commit to your new repo)
4. If you want [codecov](https://about.codecov.io/sign-up/) Reports and Automatic Release to [PyPI](https://pypi.org)  
  On the new repository `settings->secrets` add your `PYPI_API_TOKEN` and `CODECOV_TOKEN` (get the tokens on respective websites)
4. Read the file [CONTRIBUTING.md](CONTRIBUTING.md)
5. Then clone your new project and happy coding!

> **NOTE**: **WAIT** until first CI run on github actions before cloning your new project.

### What is included on this template?

- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <project_name>` or `$ project_name` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.

### Repository quality

<p align="center">
<img src = "figs/info_levels.png" alt="Repository quality"/>
</p>


<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---
# project_name

[![codecov](https://codecov.io/gh/author_name/project_urlname/branch/main/graph/badge.svg?token=project_urlname_token_here)](https://codecov.io/gh/author_name/project_urlname)
[![CI](https://github.com/author_name/project_urlname/actions/workflows/main.yml/badge.svg)](https://github.com/author_name/project_urlname/actions/workflows/main.yml)

Brief abstract of the research
[_"Title"_](https://journal.net/forum?id=Title)


## Description

Description

<p align="center">
<img src = "figs/python-logo.svg" alt="Alternative caption 1"/>
</p>
<p align="center">
Fig. 1. Caption 1
</p>


### Subsection

Description


## Results

Main Results

<table style="border-collapse: collapse; width: 100%; height: 108px;" align="center">
   <thead>
      <tr style="height: 18px;">
         <td style="width: 20%; height: 18px; text-align: center;" align="center"><strong>Dataset</strong></td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center"><strong>Rows</strong></td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center"><strong>Num. Feats</strong></td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center"><strong>Cat. Feats</strong></td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center"><strong>Task</strong></td>
      </tr>
   </thead>
   <tbody>
      <tr style="height: 18px;">
         <td style="width: 20%; height: 18px; text-align: center;" align="center"><a href="https://community.fico.com/s/explainable-machine-learning-challenge">HELOC</a></td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center">9871</td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center">21</td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center">2</td>
         <td style="width: 20%; height: 18px; text-align: center;" align="center">Binary</td>
      </tr>
   </tbody>
</table>


## How to use the code

### Install it from PyPI

```bash
pip install project_name
```

### Usage

```py
from project_name import BaseClass
from project_name import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m project_name
#or
$ project_name
```


### Requirements

```bash
numpy==1.25.2
pandas==2.1.0
scikit-learn==1.1.2
tqdm==4.64.1
torch==1.13.0+cu117
torch-geometric==2.2.0
xgboost==1.7.2
```


## Citation

If you use this codebase, please cite our work:

```bib
@article{authorYearTitle,
    title={title},
    author={author},
    year={year},
    journal={journal},
    url={url}
}
```
