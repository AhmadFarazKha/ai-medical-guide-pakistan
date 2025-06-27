import os
import asyncio
from dotenv import load_dotenv
from src.core.generator import MedicalGuideGenerator
from src.utils.file_operations import create_directories_if_not_exist

async def main():
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
        print("Error: API_KEY not found in .env file. Please set it up.")
        return

    generator = MedicalGuideGenerator(api_key=google_api_key)

    print("\n--- AI Blood Test Interpreter (CLI Version) ---")
    print("This is a basic CLI for testing; use app.py for full GUI.")

    while True:
        user_input = input("Enter blood test results (e.g., 'Hgb: 14, WBC: 7.2', type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            response = await generator.interpret_blood_test_results(user_input)
            print("\nAI Interpretation:")
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
