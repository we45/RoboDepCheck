import docker
from robot.api import logger
from docker.types import Mount

class RoboDepCheck(object):

    def __init__(self):
        self.client = docker.from_env()
        self.depcheck_docker = "owasp/dependency-check"

    def run_depcheck_against_source(self, code_path, results_path, nvd_db_path):
        self.source_path = code_path
        self.results_path = results_path
        self.nvd_db_path = nvd_db_path
        source_mount = Mount("/src", self.source_path, type = "bind")
        results_mount = Mount("/dep_check_results", self.results_path, type = "bind")
        nvd_db_mount = Mount("/usr/share/dependency-check/data", self.nvd_db_path, type="bind")
        self.client.containers.run(self.depcheck_docker, mounts = [source_mount, results_mount, nvd_db_mount], command='--scan /src --format "ALL" --out /dep_check_results --project "RoboDepCheck"')
        logger.info("Successfully ran OWASP Dependency Check against the src. Please find the *.html, *.json and *.xml files in the results directory")