from crewai_tools import BaseTool
import os
from dotenv import load_dotenv
import json
import requests
import json
from typing import Any
load_dotenv()

class CustomSerpApiTool(BaseTool):
    name: str = "Custom Serp API Tool"
    description: str = "Use this tool to search the web for news information."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _run(self, query: str) -> str:
        api_key = os.getenv("SERP_API_KEY")
        print(f"Using API key: {api_key}")
        
        url = "https://google.serper.dev/news"

        payload = json.dumps({
        "q": query,
        "tbs": "qdr:d",
        "num": 10,
        "autoCorrect": False,
        })
        headers = {
        'X-API-KEY': '5ce31ef5dcd4b50169b604222b52556b86519774',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        #parse the json response
        response_data = response.json()    
        news_data = response_data.get( "news",[])

        return json.dumps(news_data,indent=2)

if __name__ == "__main__":
    tool = CustomSerpApiTool()
    print(tool._run("AI Agents"))
