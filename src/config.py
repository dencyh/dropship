import yaml

class Config:
    _instance = None

    def __new__(cls, config_file='./config.yaml'):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            with open(config_file) as f:
                cls._instance.cfg = yaml.load(f, Loader=yaml.FullLoader)
        return cls._instance

    def get(self, key):
        return self.cfg.get(key)