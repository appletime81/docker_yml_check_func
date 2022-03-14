import yaml

from tokenize import String
from typing import Dict
from pprint import pprint


def check_file_exist(extension: String, config_content: Dict):
    save_flag = False
    if extension in config_content['services']['gnb_du']['volumes']:
        print('The extension is existing')
    else:
        save_flag = True
        config_content['services']['gnb_du']['volumes'].append(extension)
    save_file('new-docker-compose.yml', save_flag, config_content)
    return config_content


def save_file(fileName: String, save_flag: bool, config_content: Dict):
    if save_flag:
        with open(f'{fileName}', 'w') as f:
            yaml.dump(config_content, f, default_flow_style=False)


def main():
    with open("docker-compose.yml", 'r') as ymlfile:
        docker_config = yaml.safe_load(ymlfile)

    extension_cpu_table = './profile/active/du_cputable_1:/home/pegauser/synergy/config/du_cputable_1'
    extension_du_bin = './du_bin/frank_bin:/home/pegauser/synergy/du_bin_intel/bin'

    docker_config = check_file_exist(extension_cpu_table, {**docker_config})
    docker_config = check_file_exist(extension_du_bin, {**docker_config})


if __name__ == '__main__':
    main()
