import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"] = "5c7d11ecb8192e8bcde049ba7a07193682d8733d" # Replace with your actual Serper API key


search_tool = SerperDevTool()


researcher = Agent(
  role='Senior Influencer Researcher',
  goal='Find relevant food bloggers and Instagram influencers in a given state',
  backstory=(
    "You are an expert at scouring the internet for social media influencers. "
    "Your specialty is finding popular bloggers and Instagrammers in specific "
    "geographic locations based on keywords like 'food', 'travel', or 'fashion'."
  ),
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
)


analyst = Agent(
  role='Data Analyst',
  goal='Extract Instagram IDs and names from the research findings',
  backstory=(
    "You are a meticulous Data Analyst. You can read through large amounts of text "
    "and pick out the most important information. Your skill lies in identifying "
    "patterns, specifically recognizing social media handles and names from web content."
  ),
  verbose=True,
  allow_delegation=False,
)


research_task = Task(
  description=(
    "Search the internet to find a list of food bloggers and influencers for the state: {state}. "
    "Focus on finding articles, blog posts, and lists that mention these influencers and their Instagram accounts."
  ),
  expected_output='A comprehensive list of URLs and text snippets containing names and Instagram handles of food influencers in the specified state.',
  agent=researcher
)


analysis_task = Task(
  description=(
    "Review the research findings and compile a clean, final list of the influencers. "
    "For each influencer, extract their name and their Instagram ID (usually starting with '@')."
  ),
  expected_output='A formatted list of influencer names and their corresponding Instagram IDs. Example: - Blogger Name: @instagram_handle',
  agent=analyst
)


crew = Crew(
  agents=[researcher, analyst],
  tasks=[research_task, analysis_task],
  process=Process.sequential, # The tasks will be executed one after the other.
  verbose=2 # Verbose level 2 provides detailed logs of the agent's actions.
)


if __name__ == "__main__":
    print("######################################")
    print("## Welcome to the Influencer Finder ##")
    print("######################################")
    
   
    state_input = input("Enter the state you want to search for food bloggers in: ")

    if not state_input:
        print("State cannot be empty. Exiting.")
    else:
        
        result = crew.kickoff(inputs={'state': state_input})
        
        print("\n\n########################")
        print("## Here is your result:")
        print("########################\n")
        print(result)
