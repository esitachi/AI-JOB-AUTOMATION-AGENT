import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

JOB_EMAIL = os.getenv("JOB_EMAIL", "eshaanhegde29@gmail.com")
JOB_NAME = os.getenv("JOB_NAME", "Eshaan Hegde")
