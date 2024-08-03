import os
import yaml
import httpx
from openai import AzureOpenAI


CONFIG_PATH = ""
# Load the YAML configuration file
with open('path/to/file/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

client = AzureOpenAI(
    api_key=config["AZURE_OPENAI_API_KEY"],  
    api_version=config["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = config["AZURE_OPENAI_ENDPOINT"],
    http_client=httpx.Client(verify=False)
    )

def get_completion(msg):

    response = client.chat.completions.create(
        model=config["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg}
        ],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    print("Welcome to Azure OpenAI!")

    while True:

        user_message = input(">>")

        if user_message != "exit":

            completion = get_completion(user_message)

            print(completion)

        else:

            break

    print("Bye Bye!")
