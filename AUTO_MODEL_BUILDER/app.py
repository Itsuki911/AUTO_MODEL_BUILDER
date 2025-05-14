import streamlit as st
from scripts.fetch_papers import fetch_research_papers
from scripts.summarize_translate import summarize_and_translate
from scripts.github_fetcher import fetch_github_code
from scripts.hf_model_search import suggest_base_model
from scripts.generate_data import create_training_data
from scripts.train_model import train_model
from scripts.evaluate_model import evaluate_model
from scripts.generate_report import PDFReport
from scripts.utils import handle_error
from scripts.knowledge_extraction import extract_knowledge_and_propose
import sys
import os

# プロジェクトのルートディレクトリをモジュール検索パスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def initialize_session_state():
    """Initialize session state variables."""
    if "task" not in st.session_state:
        st.session_state.task = None
    if "requirements" not in st.session_state:
        st.session_state.requirements = None

def requirements_definition():
    """Handle the Requirements Definition section."""
    st.subheader("Define your task and requirements")
    task = st.text_input("Task (e.g., Sentiment Analysis)")
    requirements = st.text_area("Requirements (e.g., Classification type, Data format)")
    if st.button("Submit"):
        st.session_state.task = task
        st.session_state.requirements = requirements
        st.success("Requirements saved!")

def view_papers_used():
    """Handle the View Papers Used section."""
    st.subheader("Fetch and summarize relevant papers")
    if st.button("Fetch Papers"):
        try:
            if not st.session_state.task:
                st.warning("Please define your task in 'Requirements Definition' first.")
                return
            
            with st.spinner("Fetching papers..."):
                # Fetch research papers using the task
                papers = fetch_research_papers(st.session_state.task)
            
            if not papers:
                st.info("No relevant papers found.")
                return
            
            # Display the fetched papers
            st.write("### Recommended Papers:")
            for i, paper in enumerate(papers, start=1):
                st.write(f"**{i}. {paper['title']}**")
                st.write(f"[Read more]({paper['link']})")
            
            # Summarize and translate the papers
            summaries = summarize_and_translate(papers)
            st.write("### Summaries:")
            for summary in summaries:
                st.write(f"**Title:** {summary['title']}")
                st.write(f"**Link:** [Read more]({summary['link']})")
                st.write(f"**Summary:** {summary['summary']}")
                st.write(f"**Translated Summary:** {summary['translated_summary']}")
                st.write("---")
        
        except Exception as e:
            handle_error(e)
            st.error(f"An error occurred while fetching papers: {str(e)}")

def github_integration():
    """Handle the GitHub integration section."""
    st.subheader("Fetch relevant code from GitHub")
    if st.button("Fetch GitHub Code"):
        try:
            if not st.session_state.task:
                st.warning("Please define your task in 'Requirements Definition' first.")
                return
            code = fetch_github_code(st.session_state.task)
            st.write(code)
        except Exception as e:
            handle_error(e)
            st.error("An error occurred while fetching GitHub code.")

def knowledge_extraction():
    """Handle the Knowledge Extraction and Embedded Proposal section."""
    st.subheader("Extract knowledge and propose model design")
    if st.button("Extract Knowledge"):
        try:
            if not st.session_state.task:
                st.warning("Please define your task in 'Requirements Definition' first.")
                return
            proposal = extract_knowledge_and_propose(st.session_state.task)
            st.write(proposal)
        except Exception as e:
            handle_error(e)
            st.error("An error occurred while extracting knowledge.")

def base_model_suggestion():
    """Handle the Base Model suggestion section."""
    st.subheader("Suggest base models")
    if st.button("Suggest Base Model"):
        try:
            if not st.session_state.task:
                st.warning("Please define your task in 'Requirements Definition' first.")
                return
            model = suggest_base_model(st.session_state.task)
            st.write(model)
        except Exception as e:
            handle_error(e)
            st.error("An error occurred while suggesting a base model.")

def generate_learning_data():
    """Handle the Learning Data generation section."""
    st.subheader("Generate training data")
    if st.button("Generate Data"):
        try:
            if not st.session_state.requirements:
                st.warning("Please define your requirements in 'Requirements Definition' first.")
                return
            csv_path = create_training_data(st.session_state.requirements)
            with open(csv_path, "rb") as file:
                st.download_button("Download Training Data", file, "training_data.csv")
        except Exception as e:
            handle_error(e)
            st.error("An error occurred while generating training data.")

def train_example_model():
    """Handle the Create Example Model section."""
    st.subheader("Train the model")
    if st.button("Train Model"):
        try:
            if not st.session_state.requirements:
                st.warning("Please define your requirements in 'Requirements Definition' first.")
                return
            model_info = train_model(st.session_state.requirements)
            st.write(model_info)
        except Exception as e:
            handle_error(e)
            st.error("An error occurred while training the model.")

def evaluate_model_section():
    """Handle the Evaluation section."""
    st.subheader("Evaluate the trained model")
    if st.button("Evaluate Model"):
        try:
            evaluation_results = evaluate_model()
            st.write(evaluation_results)
        except Exception as e:
            handle_error(e)
            st.error("An error occurred while evaluating the model.")

def generate_report():
    """Handle the Report generation section."""
    st.subheader("Generate PDF report")
    if st.button("Generate Report"):
        try:
            report = PDFReport("AI Model Development Report")
            report.add_section("Requirements", str(st.session_state.requirements))
            report.add_section("Task", st.session_state.task)
            report_path = "reports/ai_model_report.pdf"
            report.save(report_path)
            with open(report_path, "rb") as file:
                st.download_button("Download Report", file, "ai_model_report.pdf")
        except Exception as e:
            handle_error(e)
            st.error("An error occurred while generating the report.")

def main():
    st.title("Automatic AI Model Development System")
    initialize_session_state()

    # Navigation
    menu = [
        "Requirements Definition", "View Papers Used", "GitHub",
        "Knowledge Extraction and Embedded Proposal", "Base Model",
        "Learning Data", "Create Example Model", "Evaluation", "Report"
    ]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Route to the appropriate section
    if choice == "Requirements Definition":
        requirements_definition()
    elif choice == "View Papers Used":
        view_papers_used()
    elif choice == "GitHub":
        github_integration()
    elif choice == "Knowledge Extraction and Embedded Proposal":
        knowledge_extraction()
    elif choice == "Base Model":
        base_model_suggestion()
    elif choice == "Learning Data":
        generate_learning_data()
    elif choice == "Create Example Model":
        train_example_model()
    elif choice == "Evaluation":
        evaluate_model_section()
    elif choice == "Report":
        generate_report()

if __name__ == "__main__":
    main()