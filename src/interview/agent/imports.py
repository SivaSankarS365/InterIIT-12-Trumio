# imports
import warnings
import json
import random

warnings.filterwarnings("ignore")
from openai import OpenAI
from litellm import completion as LLMBackend, completion_cost, token_counter
from litellm import embedding
import os
import time
import re
import numpy as np


# constants/args
API_TOKEN = os.environ["AGENT_API_TOKEN"]
GPT_4 = "openai/gpt-4-1106-preview"
GPT_3 = "openai/gpt-3.5-turbo-1106"
GPT_3_1 = GPT_3
GPT_3_2 = "openai/gpt-3.5-turbo-0301"
GPT_3_3 = 'openai/ft:gpt-3.5-turbo-1106:interiit:trumio-interiit:8UeS19Kf'
GPT_3_4 = 'opeani/ft:gpt-3.5-turbo-1106:interiit:trumio-interiit2:8UegAuHm'
INSTRUCT = "openai/gpt-3.5-turbo-instruct"
ZEPHR = os.environ["AGENT_ZEPHR"]
OPENCHAT = os.environ["AGENT_OPENCHAT"]
LLAMA_JSON = os.environ["AGENT_LLAMA_JSON"]
STARLING = os.environ["AGENT_STARLING"]
# init
client = OpenAI(api_key=API_TOKEN)
os.environ["OPENAI_API_KEY"] = API_TOKEN
