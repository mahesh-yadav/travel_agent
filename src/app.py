from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.messages import HumanMessage

from agents import research_agent, planner_agent
from helpers import generate_ics_content


# Set up the Streamlit app
st.title("AI Travel Planner ")
st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary using GPT-5-nano")

# Initialize session state to store the generated itinerary
if 'itinerary' not in st.session_state:
    st.session_state.itinerary = None

# Input fields for the user's destination and the number of days they want to travel for
destination = st.text_input("Where do you want to go?")
num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Itinerary"):
        with st.spinner("Researching your destination..."):
            # First get research results
            research_response = research_agent.invoke({
                "messages": [
                    HumanMessage(content=f"Research {destination} for a {num_days} day trip")
                ]
            })

            # Show research progress
            st.write(" Research completed")
            
        with st.spinner("Creating your personalized itinerary..."):
            # Pass research results to planner
            prompt = f"""
            Destination: {destination}
            Duration: {num_days} days
            Research Results: {research_response["messages"][-1].content}
            
            Please create a detailed itinerary based on this research.
            """
            planner_response = planner_agent.invoke({
                "messages": [
                    HumanMessage(content=prompt)
                ]
            })

            # Store the response in session state
            st.session_state.itinerary = planner_response["messages"][-1].content
            st.write(planner_response["messages"][-1].content)

# Only show download button if there's an itinerary
with col2:
    if st.session_state.itinerary:
        # Generate the ICS file
        ics_content = generate_ics_content(st.session_state.itinerary)
        
        # Provide the file for download
        st.download_button(
            label="Download Itinerary as Calendar (.ics)",
            data=ics_content,
            file_name="travel_itinerary.ics",
            mime="text/calendar"
        )