from praisonaiagents import Agent, MCP
import streamlit as st



def search_airbnb(query):
    agent = Agent(
        instructions="You help book apartments on Airbnb.",
        llm="ollama/llama3.2",
        tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
    )
    result = agent.start(query)
    return f"## Airbnb Search Results\n\n{result}"

st.title("Airbnb Booking Assistant")
st.write("Enter your booking requirements below:")

user_input = st.text_input("Plae...")

if user_input:
    result = search_airbnb(user_input)
    st.markdown(result)



