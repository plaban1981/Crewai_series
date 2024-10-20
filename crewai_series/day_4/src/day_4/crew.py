from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,ScrapeWebsiteTool
from langchain_groq import ChatGroq
from langchain.llms import Ollama
import os
from dotenv import load_dotenv
load_dotenv()

# Uncomment the following line to use an example of a custom tool
from tools.custom_tool import CustomSerpApiTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class Day4Crew:
	"""Day4 crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	llm = LLM(model='groq/llama-3.1-70b-versatile',
           base_url="https://api.groq.com/openai/v1",
           api_key=os.getenv("GROQ_API_KEY"))
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[CustomSerpApiTool(),ScrapeWebsiteTool()],
			verbose=True,
			llm=self.llm  # Add this line
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			llm=self.llm,
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher()
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day03 crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)