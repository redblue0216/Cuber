import yaml

cuber_config = {'ray_host':'127.0.0.1',
                'ray_port':'10001',
                'cuber_sheduler_sys_name':'tmp_sheduler'}

with open('cuber_config.yaml','w') as cuber_yaml:
    yaml.dump(cuber_config,cuber_yaml)