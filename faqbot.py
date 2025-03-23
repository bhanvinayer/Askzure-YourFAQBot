import os  
import base64
from openai import AzureOpenAI  
from azure.identity import DefaultAzureCredential, get_bearer_token_provider  
        
endpoint = os.getenv("ENDPOINT_URL", "https://bhanv-m8la4dhj-eastus2.openai.azure.com/")  
deployment = os.getenv("DEPLOYMENT_NAME", "Askzure-YourFAQBot")  
      
# Initialize Azure OpenAI Service client with Entra ID authentication
token_provider = get_bearer_token_provider(  
    DefaultAzureCredential(),  
    "https://cognitiveservices.azure.com/.default"  
)  
  
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    azure_ad_token_provider=token_provider,  
    api_version="2024-05-01-preview",  
)  
  

chat_prompt = [
    {
        "role": "system",
        "content": "You are a chatbot for the Azure Student Chapter Amity University Noida. Answer questions based on this FAQ:\n1. What is the Azure Student Chapter? - It’s a community for students to learn Azure & AI.\n2. How can I join? - Sign up on our website or attend an event.\n3. What events do you have? - Hackathons, AI/ML workshops, and more.\n4. How do I get Azure credits? - Apply via Azure for Students.\n5. Where can I get help? - Join our Discord #ai-ml-help channel.\n"
    },
    {
        "role": "user",
        "content": "how can i join Azure Student Chapter Amity University Noida Where can I get help?"
    },
    {
        "role": "assistant",
        "content": "To join the Azure Student Chapter at Amity University Noida, you can sign up on our website or attend one of our events. For help and assistance, you can join our Discord server and navigate to the #ai-ml-help channel where you can get support from fellow members and mentors."
    }
] 
    
# Include speech result if speech is enabled  
messages = chat_prompt 

completion = client.chat.completions.create(  
    model=deployment,  
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False  
)  
  
print(completion.to_json())  
