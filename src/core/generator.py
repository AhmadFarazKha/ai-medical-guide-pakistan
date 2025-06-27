import json
import os
import requests

class MedicalGuideGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url_text_generation = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key="
        self.headers = {'Content-Type': 'application/json'}

    def _call_gemini_api(self, prompt: str) -> str:
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        }

        full_api_url = f"{self.api_url_text_generation}{self.api_key}"

        try:
            response = requests.post(full_api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            result = response.json()

            if result.get("candidates") and len(result["candidates"]) > 0 and \
               result["candidates"][0].get("content") and \
               result["candidates"][0]["content"].get("parts") and \
               len(result["candidates"][0]["content"]["parts"]) > 0:
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                error_detail = result.get('error', {}).get('message', 'No specific error message.')
                raise Exception(f"Unexpected API response structure or error: {error_detail}. Full response: {json.dumps(result)}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network or API request error: {e}. Please check your internet connection and API key.")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to decode JSON response from API: {e}. Response text: {response.text if 'response' in locals() else 'No response'}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred during API call: {e}")

    def interpret_blood_test_results(self, blood_test_data: str) -> str:
        prompt = (f"You are an AI assistant providing preliminary interpretation of blood test results. "
                  f"It is CRUCIAL to state clearly that this is NOT a medical diagnosis, nor a substitute for professional medical advice or treatment. "
                  f"Always advise the user to consult a qualified doctor or healthcare professional for accurate diagnosis and treatment. "
                  f"Interpret the given blood test results for a user in Pakistan, considering common local health contexts and typical ranges (if applicable, state general implications, NOT specific diagnoses).\n\n"
                  f"Blood Test Results:\n{blood_test_data}\n\n"
                  "Your response should include:\n"
                  "1. **IMPORTANT DISCLAIMER** (prominently at the beginning: 'This is not a diagnosis. Consult a doctor.').\n"
                  "2. Preliminary interpretation for each major parameter provided (e.g., 'If RBC count is high/low, it *could* indicate...').\n"
                  "3. Common possible implications or conditions (without diagnosing).\n"
                  "4. Strong advice on 'Next Steps: Consult a Doctor' explaining why it's essential.\n"
                  "5. General lifestyle or preventative tips relevant to common findings (e.g., for high cholesterol, general advice on diet/exercise).")
        return self._call_gemini_api(prompt)
