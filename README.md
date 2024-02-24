# 🗃️ Aubaine.io **API**

![Python Badge](https://img.shields.io/badge/Python-3.12-%233776AB?logo=python&logoColor=%233776AB)

The API used for the Web and Mobile client of Aubaine.io.

## 🔨 Installation
It's rather simple to install once you have taken care of all the [dependencies](#🔗-dependencies). Just run:
```bash
$ make venv install
```
> Please make sure you have all **dependencies** installed before trying to install the project.

## 🏃 Run the app
For developpement purposes just run the following command:
```bash
$ make up dev
```
> You can just hit `CTRL+C` to stop the dev server and then run `$ make down` to stop and remove the running containers.

## ⚙️ Make rules 
- ***help***:           Show this help.
- ***dev***:            Run the API Server on dev mode (with reload).
- ***up***:             Up a Database container and a PHPMyAdmin container for dev purposes.
- ***down***:           Down the Database container and the PHPMyAdmin container upped by the `up` rule.
- ***venv***:           Generate a Python Virtual Environnement.
- ***install***:        Install all the files in the requirement file.
- ***freeze***:         Update the requirement file.
- ***info***:           Display information about the Virtual Environnement.
- ***clean***:          Clean all the generated files and folders.

## 🔗 Dependencies
- [make](https://www.gnu.org/software/make/)
- [python3.12](https://docs.python.org/3/whatsnew/3.12.html)
- [python3.12-venv](https://docs.python.org/3/library/venv.html)
- [docker](https://docs.docker.com/get-docker/)
- [docker-compose-plugin](https://docs.docker.com/compose/install/#installation-scenarios)

##
Kori-san / Aubaine.io

<a href="https://gitmoji.dev">
  <img
    src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square"
    alt="Gitmoji"
  />
</a>
