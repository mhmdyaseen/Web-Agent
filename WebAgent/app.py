from src.agent.web.browser.config import BrowserConfig
from src.inference.gemini import ChatGemini
from src.inference.groq import AudioGroq
from src.agent.web import WebAgent
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key='AIzaSyCLXTJO5XG3oW_Y3ubAjojYNxbkyX9Mrmg'
groq_api_key=os.getenv('GROQ_API_KEY')
browser_instance_dir=os.getenv('BROWSER_INSTANCE_DIR')
user_data_dir=os.getenv('USER_DATA_DIR')


llm=ChatGemini(model='gemini-2.0-flash',api_key=google_api_key,temperature=0)
config=BrowserConfig(browser='chrome',browser_instance_dir=browser_instance_dir,user_data_dir=user_data_dir,headless=False)
agent=WebAgent(config=config,instructions=[],llm=llm,verbose=True,use_vision=False,max_iteration=100,token_usage=False)

print('Enter the command for WebAgent to do:')
agent_response=agent.invoke(input('Enter your query: '))