# AI Travel Planner 🌍✈️

Plan your next adventure with AI Travel Planner! This application uses advanced AI agents to research your destination and create a personalized, detailed itinerary for your trip.

## Features

- **AI Research Agent**: Searches for the best destinations, activities, and accommodations based on your input.
- **AI Planning Agent**: Crafts a structured and engaging day-by-day itinerary.
- **Calendar Integration**: Download your personalized itinerary as an `.ics` file to easily add it to your calendar (Google Calendar, Apple Calendar, etc.).

## Project Description

AI Travel Planner leverages two specialized agents:
- **Researcher**: A world-class travel researcher that finds the most relevant activities and local gems using web search.
- **Planner**: A senior travel planner that synthesizes research results into a nuanced, balanced, and high-quality itinerary.

## Setup Instructions

### 1. Prerequisites

Ensure you have [uv](https://github.com/astral-sh/uv) installed. If not, you can install it via:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd travel_agent
```

### 3. Environment Setup

Install the dependencies and set up the virtual environment:

```bash
uv sync
```

### 4. Configuration

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Open `.env` and provide the following:
- `OPENAI_API_KEY`: Your OpenAI API key.
- `TAVILY_API_KEY`: Your Tavily API key for web search.
- `LANGSMITH_API_KEY`: (Optional) For tracing and debugging.

## How to Run

To start the AI Travel Planner web application, run:

```bash
uv run streamlit run src/app.py
```

Once the app is running, open your browser to the local URL provided (usually `http://localhost:8501`).

## Usage

1. Enter your desired **destination**.
2. Specify the **number of days** for your trip.
3. Click **"Generate Itinerary"**.
4. Once generated, you can review your plan and click **"Download Itinerary as Calendar (.ics)"** to save it to your calendar.
