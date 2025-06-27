```
# 🩺 AI-Assisted Blood Test Interpreter for Pakistan

## Project Overview

The **AI-Assisted Blood Test Interpreter** is an essential tool designed to provide preliminary information and insights into common blood test results. It aims to help individuals in Pakistan better understand their lab reports by offering clear, AI-generated interpretations of various parameters.

**Crucially, this application is for informational purposes only and is NOT a medical diagnosis, nor a substitute for professional medical advice, diagnosis, or treatment. Users are always strongly advised to seek the advice of a qualified healthcare provider for accurate interpretation of their results, diagnosis of any condition, and appropriate treatment plans.**

This chatbot empowers individuals with basic health literacy regarding their blood work, helping them formulate informed questions for their doctors and understand general implications, especially in areas where detailed medical explanations might not be readily available.

## Key Features

-   **Blood Test Result Input**: Users can input values for common blood tests (e.g., CBC, Glucose, Lipid Profile, Liver/Kidney Function Tests).
-   **Preliminary Interpretation**: Provides insights into potential common implications of results (e.g., what high/low values *could* indicate), without offering a diagnosis.
-   **"Consult a Doctor" Advice**: Crucially highlights the necessity of professional medical consultation for diagnosis and treatment, outlining why a doctor's expertise is essential.
-   **General Health Tips**: Offers general lifestyle or preventative tips relevant to common blood test findings (e.g., for high cholesterol, advice on diet/exercise).
-   **Interactive Web GUI**: Built with Streamlit for an accessible, user-friendly, browser-based interface.
-   **AI-Powered Core**: Leverages the Google Gemini API (`gemini-2.0-flash`) for intelligent analysis and response generation.
-   **Secure API Key Management**: Uses `.env` files for safe handling of sensitive API keys.
-   **Automated Setup**: Includes a PowerShell script to quickly set up the required project directory structure and populate initial files.

## How It Works

1.  **User Input**: Through the Streamlit GUI (`app.py`), the user enters their blood test names and their corresponding values (e.g., "Hemoglobin: 14 g/dL", "Fasting Glucose: 95 mg/dL").
2.  **API Key Loading**: The application securely loads the Google API key from the `.env` file.
3.  **Prompt Engineering**: The `MedicalGuideGenerator` (`src/core/generator.py`) crafts a detailed prompt, instructing the Gemini model to act as an AI interpreter for blood test results, with a strong emphasis on disclaimers and the need for professional medical advice.
4.  **Gemini API Interaction**: An HTTP POST request is made to the Google Gemini API (`gemini-2.0-flash`) to obtain the AI-generated interpretation.
5.  **AI-Generated Interpretation**: The Gemini model processes the data and returns a preliminary interpretation for each provided parameter, along with general implications and clear advice to consult a doctor.
6.  **Display Output**: The generated information is presented clearly and prominently in the Streamlit interface, always accompanied by disclaimers.
7.  **Directory Management**: Utility functions (`src/utils/file_operations.py`) ensure that project directories are correctly structured.

## Project Structure


```

ai-medical-guide-pakistan/

├── .env                  # Environment variables (e.g., API keys - already existing, not created by script)

├── src/                  # Source code directory

│   ├── init.py       # Makes 'src' a Python package

│   ├── core/             # Core logic for AI generation

│   │   ├── init.py

│   │   ├── generator.py  # Contains the MedicalGuideGenerator class and API integration

│   │   └── config.py     # Global configuration (optional)

│   └── utils/            # Utility functions

│       ├── init.py

│       └── file_operations.py # Utility for directory creation

├── app.py                # Main Streamlit application entry point (GUI)

├── main.py               # Optional: Command-line interface (CLI) entry point/backend processing

├── requirements.txt      # Python dependencies

└── README.md             # Project documentation (this file)

```

## Setup and Installation

1.  **Create GitHub Repository:**
    Start by creating a new repository (e.g., `ai-medical-guide-pakistan`) via GitHub Desktop. Provide a description. Clone it to your local machine.

2.  **Open in VS Code & Run Setup Script:**
    Open the cloned repository folder in VS Code. Open the PowerShell terminal within VS Code and **navigate into your `ai-medical-guide-pakistan` directory**. Then, run the PowerShell command provided in this guide. This script will create all necessary folders and placeholder files within your existing repository, but **it will NOT create or modify your `.env` file, nor will it interfere with your `.git` or `.gitignore` files.**

3.  **Copy Code into Files:**
    Copy the code provided in separate blocks below (for `.env` if needed, and for `requirements.txt`, `app.py`, `main.py`, and all files under `src/`) and paste them into their respective files in your project directory.

4.  **Create and Activate a Python Virtual Environment (Recommended):**
    In your project's root directory (`ai-medical-guide-pakistan`), run:
    ```bash
    python -m venv venv
    ```
    * **Activate the virtual environment:**
        * On Windows:
            ```bash
            .\venv\Scripts\activate
            ```
        * On macOS/Linux:
            ```bash
            source venv/bin/activate
            ```

5.  **Install Dependencies:**
    With your virtual environment activated:
    ```bash
    pip install -r requirements.txt
    ```

6.  **Verify Google API Key in .env:**
    Ensure your `.env` file (which you already have) in the `ai-medical-guide-pakistan/` root directory contains your API key correctly set:
    ```
    API_KEY=YOUR_GOOGLE_API_KEY_HERE
    ```
    **Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual API key.**

## Usage

1.  **Run the Streamlit application:**
    Ensure your virtual environment is active, then from the `ai-medical-guide-pakistan/` directory, run:
    ```bash
    streamlit run app.py
    ```
    This will open the web-based GUI for your AI Blood Test Interpreter in your default web browser.

## Deployment

To deploy your Streamlit application to the web, you can use services like:
-   **Streamlit Community Cloud:** Easiest option for quick deployment. Connects directly to your GitHub repository.
-   **Hugging Face Spaces:** Another free and easy option for deploying Streamlit apps.
-   **Render.com / Heroku / DigitalOcean / AWS:** For more control and scalability (requires more setup).

For Streamlit Community Cloud or Hugging Face Spaces, you typically need:
1.  Your project pushed to a public GitHub repository.
2.  A `requirements.txt` file listing all Python dependencies.
3.  Your `app.py` as the main entry point.
4.  Your `AI_KEY` or `GOOGLE_API_KEY` set as a **secret variable** in the deployment platform's settings (do NOT hardcode it in `app.py` or commit your `.env` file).

## Future Enhancements (Ideas for Expansion)

-   **Urdu/Regional Language Support**: Implement input and output in local languages for wider accessibility in Pakistan.
-   **Reference Ranges**: (Advanced) Allow users to input lab-specific reference ranges for more precise context.
-   **Historical Tracking**: Enable users to save and track their blood test results over time.
-   **Symptom Correlation**: (Carefully implemented) Allow users to optionally input symptoms for context, with strong disclaimers about non-diagnosis.
-   **Tele-consultation Linkage**: (Advanced) Provide links to platforms for virtual consultations with medical professionals in Pakistan.
-   **Educational Modules**: Create short, interactive modules explaining common blood tests and their general significance.

```
