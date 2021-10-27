
import yaml
import os
def read_yaml(filename):
    dirname=os.path.dirname(os.path.realpath(filename))
    filename=os.path.join(dirname,filename)
    ls=yaml.safe_load(open(filename,encoding='utf-8'))
    print(yaml.safe_load(open('login_infos.yaml')))
    return ls


# print(read_yaml(r'test.yaml'))