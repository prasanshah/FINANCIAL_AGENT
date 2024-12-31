import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import re
from dotenv import load_dotenv
load_dotenv()


# Define agents
websearch_agent = Agent(
    name="web search agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=[
        "When the query is a company name, search the web for the latest news about the company.",
        "Provide at least 3 recent and relevant news articles or updates about the company.",
        "important: Include the source of each news item as a link for reference.",
        "Summarize the news clearly and concisely in Markdown format for readability.",
        "Focus on key developments that could impact the company's stock or market position.",
        "Provide a plain-text output without any LaTeX or mathematical formatting (e.g., no use of '$', '^', '_', or other symbols).",
        "Avoid using HTML or any special rendering syntax in the response."
    ]
)

finance_agent = Agent(
    name="financial agent",
    description="You are an investment analyst that researches stock prices, analyst recommendations, stock fundamentals, and company news.",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=[
        "When the query is a company name, provide insights in a conversational and narrative style:",
        "1. Start with the current stock price and briefly summarize its recent performance trends.",
        "2. Discuss analyst recommendations naturally, mentioning the number of analysts for each category (e.g., '13 analysts recommend buying, 15 suggest holding, and 8 advise selling').",
        "3. Highlight any strong buy or strong sell recommendations and their implications, integrating these points seamlessly into the narrative.",
        "4. Offer an analysis of what these recommendations indicate about the stock's future potential, avoiding structured tables or bullet points.",
        "5. Conclude with actionable insights or suggestions, like whether the stock might be worth buying, holding, or selling, and explain why in simple terms."
        "6. Ensure that any output does not use math-mode syntax like dollar signs ('$') or similar LaTeX-like formatting.",
        "Provide a plain-text output without any LaTeX or mathematical formatting (e.g., no use of '$', '^', '_', or other symbols).",
        "Avoid using HTML or any special rendering syntax in the response."
    ]
)

multi_ai_agent = Agent(
    team=[websearch_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    instructions=[
        "For a company name query, coordinate the following actions:",
        "1. Use the web search agent to retrieve and summarize the latest news about the company, including sources.",
        "2. Use the financial agent to provide the current stock price, analyst recommendations, and stock fundamentals.",
        "3. Combine insights from both agents to give a detailed analysis, including the impact of news on stock performance.",
        "4. Offer a recommendation (buy, hold, sell) with clear justifications and future predictions based on trends.",
        "5. Format the entire response using Markdown for clarity, with tables for numerical data and clear headings for sections.",
        "6. Ensure the response is up-to-date, well-organized, and actionable.",
        "Provide a plain-text output without any LaTeX or mathematical formatting (e.g., no use of '$', '^', '_', or other symbols).",
        "Avoid using HTML or any special rendering syntax in the response."
    ]
)


# multi_ai_agent.print_response("Tesla", stream=True)

def main():
    st.title("Financial Agent - Company Analysis and Stock Insights")

    st.subheader("Enter a Stock name to get the latest news, stock insights, and analyst recommendations.")

    question = st.text_area("Enter the Stock name:", placeholder="e.g., Tesla, Apple, Meta Platforms Inc")

    if st.button("Get Insights"):
        if not question.strip():
            st.error("Please enter a valid company name to get insights.")
            return
        
        try:
            with st.spinner("Retrieving the latest company news and financial data..."):
                response = multi_ai_agent.run(question)
                
                # Sanitize the response to avoid HTML/Math rendering issues
                def sanitize_response(content):
                    sanitized_content = re.sub(r'<[^>]+>', '', content)  # Remove HTML tags
                    sanitized_content = re.sub(r'\$(.*?)\$', r'\1', sanitized_content)  # Remove math mode
                    return sanitized_content
                
                sanitized_content = sanitize_response(response.content)
                st.markdown(sanitized_content, unsafe_allow_html=True)
        except Exception as e:
            st.error("An error occurred while processing your request. Please try again later.")


if __name__ == "__main__":
    main()