from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
       
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        deserialisoitu = toml.loads(content)
        name = deserialisoitu['tool']['poetry']['name']
        description = deserialisoitu['tool']['poetry']['description']
        dependencies = deserialisoitu['tool']['poetry']['dependencies']
        devdependencies = deserialisoitu['tool']['poetry']['dev-dependencies']
        return Project(name, description, dependencies, devdependencies)
