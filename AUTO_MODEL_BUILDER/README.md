# AUTO_MODEL_BUILDER

## Overview
The AUTO_MODEL_BUILDER project is designed to streamline the development of AI models by automating various processes involved in model creation. This system allows users to input their tasks and requirements, and it handles everything from fetching relevant research papers to generating training data, training models, and producing comprehensive reports.

## Features
- **Automated Research**: Fetches and summarizes relevant research papers using the arXiv and Semantic Scholar APIs.
- **Code Retrieval**: Searches for and retrieves relevant code from GitHub repositories.
- **Model Suggestions**: Proposes suitable base models from the Hugging Face Hub based on user-defined tasks.
- **Data Generation**: Automatically generates training data in CSV format using a large language model.
- **Model Training**: Trains AI models using Google Colab with frameworks like PyTorch and TensorFlow.
- **Evaluation Metrics**: Evaluates the trained models using various metrics and visualizes the results.
- **PDF Reporting**: Generates a detailed PDF report summarizing the entire process.

## Installation
To set up the project, follow these steps:
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd AUTO_MODEL_BUILDER
   ```
3. Install the required dependencies. You can use a package manager like pip:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
2. Follow the on-screen instructions to input your task and requirements.
3. The system will automatically fetch relevant papers, retrieve code, generate training data, train the model, evaluate it, and produce a report.

## Directory Structure
- **app.py**: Main entry point for the Streamlit application.
- **scripts/**: Contains scripts for various functionalities such as fetching papers, generating data, training models, and generating reports.
- **data/**: Directory for storing generated training data.
- **models/**: Directory for storing trained models.
- **reports/**: Directory for storing generated reports.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.