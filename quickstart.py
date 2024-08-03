"""
python quickstart.py
"""
import os
import yaml
import httpx
from openai import AzureOpenAI


CONFIG_PATH = ""
# Load the YAML configuration file
with open('path/to/config/file.yaml', 'r') as file:
    config = yaml.safe_load(file)


client = AzureOpenAI(
    api_key= config["AZURE_OPENAI_API_KEY"] ,  
    api_version=config["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = config["AZURE_OPENAI_ENDPOINT"],
    http_client=httpx.Client(verify=False)
    )
    
response = client.chat.completions.create(
    model=config["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None

)

print(response.choices[0].message.content)
