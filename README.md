AI Influencer Finder Agent using CrewAI
This project contains an AI agent built with the CrewAI framework. The agent is designed to find food bloggers and Instagram influencers based on a specific state in the USA. You provide a keyword (hardcoded as "food" for this example) and a state, and the agent will search the web and return a list of relevant Instagram IDs.

How It Works
The system consists of two main AI agents:

Senior Influencer Researcher: This agent uses a search tool to browse the internet, looking for articles, lists, and blog posts that mention food influencers in the specified state.

Data Analyst: This agent takes the raw data from the researcher, carefully analyzes it, and extracts the names and Instagram handles, presenting them in a clean, readable format.

These agents work together sequentially in a "Crew" to accomplish the goal.

Getting Started
Follow these steps to set up and run the project.

1. Prerequisites
Python 3.8 or higher

An API key from Serper for the search functionality. They offer a generous free plan.

2. Installation
Clone the repository (or download the files):
If this were a full git repository, you would clone it. For now, just save main.py, requirements.txt, and README.md in the same folder.

Create and activate a virtual environment (recommended):

First, create the environment:

python -m venv venv

Then, activate it. The command differs based on your operating system:

On Windows (Command Prompt or PowerShell):

venv\Scripts\activate

On macOS and Linux:

source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

3. Configuration
Set your API Key:
Open the main.py file and replace the placeholder text with your actual Serper API key:

# Replace this line with your key
os.environ["SERPER_API_KEY"] = "YOUR_SERPER_API_KEY" 

4. Running the Agent
Execute the main.py script from your terminal:

python main.py

The script will then prompt you to enter a state. For example:

Enter the state you want to search for food bloggers in: California

The AI agents will start their work, and you will see their progress printed to the console. Once finished, a final, formatted list of influencers and their Instagram IDs will be displayed.

Example Output
########################
## Here is your result:
########################

- California Foodie: @cali_eats
- SF Bites: @sffoodexplorer
- LA Food Guide: @la.food.guide
- San Diego Foodies: @sdfoodgram

(Note: The actual output will vary based on real-time search results.)
