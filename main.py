import yaml
from pprint import pprint
with open("docker-compose.yml", 'r') as ymlfile:
    docker_config = yaml.safe_load(ymlfile)

pprint(docker_config)
print(type(docker_config))

