import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

print(os.environ.get("LLM_DEFAULT_MODEL"))