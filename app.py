import streamlit as st
import os
from dotenv import load_dotenv
from src.core.generator import MedicalGuideGenerator
from src.utils.file_operations import create_directories_if_not_exist

def run_streamlit_app():
    load_dotenv()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    directories_to_create = [
        os.path.join(base_dir, "src"),
        os.path.join(base_dir, "src", "core"),
        os.path.join(base_dir, "src", "utils"),
        os.path.join(base_dir, "data")
    ]
    create_directories_if_not_exist(directories_to_create)

    google_api_key = os.getenv("API_KEY")
    if not google_api_key:
        st.error("Error: API_KEY not found in .env file. Please ensure it's in the project root and named 'API_KEY'.")
        st.stop()

    generator = MedicalGuideGenerator(api_key=google_api_key)

    st.set_page_config(page_title="AI Blood Test Interpreter Pakistan", layout="centered", initial_sidebar_state="expanded")

    # Custom CSS for a beautiful, darker, and simple interface
    st.markdown("""
    <style>
    /* Overall app background - A soft, dark blue */
    .stApp {
        background-color: #1a202c;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    /* Main content area background - Slightly lighter than app background */
    .main {
        background-color: #2d3748;
        padding: 35px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
        border: 1px solid #4a5568;
    }

    /* Titles and Headers */
    h1 {
        color: #63b3ed;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 3em;
        margin-bottom: 30px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    h2, h3, h4 {
        color: #bee3f8;
        font-family: 'Inter', sans-serif;
        border-bottom: 1px solid #4a5568;
        padding-bottom: 8px;
        margin-top: 35px;
        margin-bottom: 20px;
    }
    h3 {
        color: #9f7aea;
    }

    /* Buttons */
    .stButton>button {
        background-color: #48bb78;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 25px;
        font-size: 1.15em;
        font-weight: bold;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        cursor: pointer;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #38a169;
        transform: translateY(-2px);
        box-shadow: 0 6px 10px rgba(0,0,0,0.4);
    }

    /* Text Inputs, Text Areas, Selectboxes, Multiselects */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div>div:first-child,
    .stMultiSelect>div>div>div:first-child {
        border-radius: 10px;
        border: 1px solid #4a5568;
        padding: 10px 15px;
        background-color: #2d3748;
        color: #e2e8f0;
        box-shadow: inset 1px 1px 3px rgba(0,0,0,0.2);
    }

    /* Placeholder text color */
    .stTextInput>div>div>input::placeholder,
    .stTextArea>div>div>textarea::placeholder {
        color: #a0aec0;
    }

    /* Alerts (Info, Warning, Error, Success) */
    .stAlert {
        border-radius: 10px;
        padding: 15px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stAlert.info { background-color: #4a5568; border-color: #63b3ed; color: #e2e8f0; }
    .stAlert.warning { background-color: #d69e2e; border-color: #ed8936; color: white; }
    .stAlert.error { background-color: #e53e3e; border-color: #c53030; color: white; }
    .stSuccess { background-color: #48bb78; color: white; border-radius: 10px; padding: 15px; font-weight: bold; margin-bottom: 20px;}

    /* Radio buttons and checkboxes */
    .stRadio > label, .stCheckbox > label {
        color: #e2e8f0;
        padding: 5px 0;
    }

    /* Style for the generated output markdown (code block style) */
    .stMarkdown pre {
        background-color: #232d3d;
        color: #e2e8f0;
        border-radius: 10px;
        padding: 25px;
        white-space: pre-wrap;
        word-break: break-word;
        border: 1px solid #4a5568;
        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    .stMarkdown code {
        background-color: #4a5568;
        color: #81e6d9;
        border-radius: 4px;
        padding: 2px 4px;
    }

    /* Sidebar styling */
    .css-1d391kg.e1fqkh3o1 {
        background-color: #232d3d;
        color: #e2e8f0;
        padding: 25px;
        border-right: 1px solid #4a5568;
        box-shadow: 5px 0 10px rgba(0,0,0,0.3);
    }
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4 {
        color: #9f7aea;
        border-bottom: none;
    }
    .css-1d391kg a {
        color: #9f7aea;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar for branding
    st.sidebar.title("Blood Test Interpreter 🇵🇰")
    st.sidebar.image("https://placehold.co/200x200/63b3ed/232d3d?text=AI+Lab+Logo") # Placeholder logo
    st.sidebar.write("Your AI assistant for understanding your blood test results, tailored for Pakistan.")
    st.sidebar.info("⚠️ **Important:** This tool is for informational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified health provider for any medical condition or emergency.")


    st.title("🔬 AI-Assisted Blood Test Interpreter")
    st.write("Understand your blood test results with preliminary information and insights, tailored for common conditions in Pakistan.")

    # --- DISCLAIMER ---
    st.warning("""
    **🛑 DISCLAIMER:** This tool provides general information and potential implications based on blood test results.
    It **DOES NOT** provide medical diagnosis or treatment advice.
    Always consult a qualified doctor or healthcare professional for interpretation of your results, diagnosis of any condition, and treatment plans.
    In case of a medical emergency, seek immediate medical attention.
    """)
    st.markdown("---")

    status_message_placeholder = st.empty()
    guidance_placeholder = st.empty()

    status_message_placeholder.info("🚀 Enter your blood test results below to get started.")


    st.subheader("📝 Enter Your Blood Test Results:")

    with st.form("blood_test_form"):
        st.write("### Common Blood Tests")
        st.markdown("*(You can input results for multiple tests. Include test name, value, and unit if known.)*")

        # Example fields for common tests
        col1, col2 = st.columns(2)
        with col1:
            cbc_rbc = st.text_input("RBC Count (e.g., 4.5 x 10^6/uL)", placeholder="e.g., 4.5")
            cbc_wbc = st.text_input("WBC Count (e.g., 7.2 x 10^3/uL)", placeholder="e.g., 7.2")
            cbc_hgb = st.text_input("Hemoglobin (Hgb) (e.g., 14 g/dL)", placeholder="e.g., 14")
            lipid_chol = st.text_input("Total Cholesterol (e.g., 180 mg/dL)", placeholder="e.g., 180")
            lipid_ldl = st.text_input("LDL Cholesterol (e.g., 100 mg/dL)", placeholder="e.g., 100")
            glucose_fasting = st.text_input("Fasting Glucose (e.g., 95 mg/dL)", placeholder="e.g., 95")
        with col2:
            glucose_rbs = st.text_input("Random Blood Sugar (RBS) (e.g., 140 mg/dL)", placeholder="e.g., 140")
            glucose_hba1c = st.text_input("HbA1c (e.g., 5.7 %)", placeholder="e.g., 5.7")
            liver_alt = st.text_input("ALT (SGPT) (e.g., 30 U/L)", placeholder="e.g., 30")
            liver_ast = st.text_input("AST (SGOT) (e.g., 25 U/L)", placeholder="e.g., 25")
            kidney_creatinine = st.text_input("Creatinine (e.g., 1.0 mg/dL)", placeholder="e.g., 1.0")
            kidney_urea = st.text_input("Urea (e.g., 20 mg/dL)", placeholder="e.g., 20")

        st.markdown("---")
        st.write("### Other / Specific Test Results")
        other_tests_desc = st.text_area(
            "Enter any other blood test results here (e.g., 'Thyroid Stimulating Hormone (TSH): 3.0 mIU/L', 'Vitamin D: 25 ng/mL'):",
            placeholder="List other test results here, one per line or separated by commas. E.g., 'Uric Acid: 6.5 mg/dL, ESR: 15 mm/hr'",
            height=150,
            help="For less common tests, provide test name, value, and unit if possible."
        )

        st.markdown("---")

        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            # FIX: Removed the 'key' parameter from st.form_submit_button when inside st.form
            submitted = st.form_submit_button("🔬 Interpret My Results!")
        with col_reset:
            # FIX: Removed the 'key' parameter from st.form_submit_button when inside st.form.
            # The reset_counter logic is no longer needed with this approach for keying.
            reset_button = st.form_submit_button("🔄 Reset Form", help="Clear all inputs and start fresh.")
            if reset_button:
                # To truly reset the form in Streamlit, clearing session_state and rerunning is the robust way.
                # The form elements will pick up default values or empty states on rerun.
                st.session_state.clear() # Clears all session state variables
                st.experimental_rerun() # Forces a rerun of the app


    if submitted:
        status_message_placeholder.empty()
        guidance_placeholder.empty()

        # Compile all input into a single string for the AI
        blood_test_results_input = []
        if cbc_rbc: blood_test_results_input.append(f"RBC Count: {cbc_rbc}")
        if cbc_wbc: blood_test_results_input.append(f"WBC Count: {cbc_wbc}")
        if cbc_hgb: blood_test_results_input.append(f"Hemoglobin (Hgb): {cbc_hgb}")
        if lipid_chol: blood_test_results_input.append(f"Total Cholesterol: {lipid_chol}")
        if lipid_ldl: blood_test_results_input.append(f"LDL Cholesterol: {lipid_ldl}")
        if glucose_fasting: blood_test_results_input.append(f"Fasting Glucose: {glucose_fasting}")
        if glucose_rbs: blood_test_results_input.append(f"Random Blood Sugar (RBS): {glucose_rbs}")
        if glucose_hba1c: blood_test_results_input.append(f"HbA1c: {glucose_hba1c}")
        if liver_alt: blood_test_results_input.append(f"ALT (SGPT): {liver_alt}")
        if liver_ast: blood_test_results_input.append(f"AST (SGOT): {liver_ast}")
        if kidney_creatinine: blood_test_results_input.append(f"Creatinine: {kidney_creatinine}")
        if kidney_urea: blood_test_results_input.append(f"Urea: {kidney_urea}")
        if other_tests_desc: blood_test_results_input.append(f"Other Tests: {other_tests_desc}")

        if not blood_test_results_input:
            status_message_placeholder.warning("⚠️ Please enter at least one blood test result to get interpretation.")
        else:
            full_query_text = "\n".join(blood_test_results_input)
            with st.spinner("🧠 Analyzing your blood test results and generating interpretation... This may take a moment."):
                try:
                    interpretation_output = generator.interpret_blood_test_results(full_query_text)
                    guidance_placeholder.subheader("✨ Your Blood Test Interpretation:")
                    guidance_placeholder.markdown(f"```markdown\n{interpretation_output}\n```")
                    status_message_placeholder.success("✅ Interpretation generated successfully! Scroll down to see the details.")
                except Exception as e:
                    status_message_placeholder.error(f"❌ Failed to interpret results: {e}")
                    status_message_placeholder.info("💡 Please ensure your Google API key is valid and you have an active internet connection. If the issue persists, try restarting the app or checking your API key.")


    st.markdown("---")
    st.markdown("Developed with ❤️ using Python, Streamlit, and Google Gemini API for Pakistani communities. [Link to GitHub Repo (Placeholder)]")
    st.markdown("Disclaimer: This AI tool provides preliminary information only. Always consult a qualified healthcare professional for medical advice, diagnosis, or treatment. In emergencies, seek immediate medical attention.")

if __name__ == "__main__":
    run_streamlit_app()
