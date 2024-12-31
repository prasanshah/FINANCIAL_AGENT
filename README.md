# Financial Agent Application

## Overview
This application provides a detailed analysis of companies based on their latest news, stock prices, analyst recommendations, and financial insights. The app uses advanced AI agents to deliver a comprehensive and user-friendly experience.

## Features
- **Web Search Agent:** Fetches the latest news about the company and summarizes it with sources.
- **Financial Agent:** Provides:
  - Current stock price.
  - Analyst recommendations.
  - Stock fundamentals and trends.
  - Actionable insights (buy, hold, sell suggestions).
- **Multi-AI Agent:** Combines data from the above agents to present a complete analysis in Markdown format.

## Prerequisites
- Python version 3.12 .
- Required Python libraries: `streamlit`, `phi`, `dotenv`, `re`.
- Access to necessary API tools (YFinance, DuckDuckGo).

## Installation
1. Clone the repository or download the code.
    "git clone https://github.com/prasanshah/FINANCIAL_AGENT.git"
2. Set up virtual environment (optional but recommended).
    conda:
        conda create -n <environment_name> python==3.12 -y
        conda activate <environment_name>
3. install dependencies.
    locate the folder FINANCIAL_AGENT:
        use command "pip install -r requirements.txt"
4. create .env file.
    save "groq api key" and "phi api key" in it.
4. launch the app.
    use command "streamlit run FINANCE_AGENT.py"




## Usage
1. Enter the name of the stock/company in the text area (e.g., Tesla, Apple).
2. Click on **Get Insights**.
3. View the detailed analysis, including:
   - Latest news with sources.
   - Stock price trends and analyst recommendations.
   - Actionable financial insights.

## Error Handling
- If no stock name is provided, an error message will prompt you to input one.
- Any technical errors during processing will be handled gracefully with an error message.

## Code Structure
- **`websearch_agent`**: Handles web search queries for company news.
- **`finance_agent`**: Retrieves stock data and provides financial analysis.
- **`multi_ai_agent`**: Integrates outputs from `websearch_agent` and `finance_agent` to create a comprehensive report.
- **Streamlit Frontend**: Provides a simple and interactive user interface for input and output.

## Limitations
- Requires internet access to fetch data.
- Output depends on the availability of up-to-date information from APIs and tools.

## Future Improvements
- Add support for additional financial metrics.
- Enable historical data comparison.
- Enhance UI with charts and graphs for better visualization.

## Contact
For any queries or suggestions, feel free to reach out to me.
prasanshah29@gmail.com
https://www.linkedin.com/in/prasansshah/

