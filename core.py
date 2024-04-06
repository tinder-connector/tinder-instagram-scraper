import yaml
from utils import obj
from model.config import Config

class Core:
    config_path = "./config.yml"
    config_file = open(config_path, "r", encoding="utf8")
    config:Config = obj(yaml.load(config_file, Loader=yaml.SafeLoader))