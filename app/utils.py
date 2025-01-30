from omegaconf import OmegaConf
from omegaconf.dictconfig import DictConfig


def load_config() -> DictConfig:
    return OmegaConf.load("config.yaml")
