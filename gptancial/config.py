"""Config."""
from environs import Env

env = Env()
env.read_env()

FMP_API_KEY = env.str("FMP_API_KEY", "")
OPEN_AI_API_KEY = env.str("OPEN_AI_API_KEY", "")
