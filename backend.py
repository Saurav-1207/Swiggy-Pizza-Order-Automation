import google.generativeai as genai
from PIL import Image

# Backend configuration for Google Generative AI
def configure_genai(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-pro")

# Function to process images and generate content using AI
def generate_test_cases(model, prompt, image_list):
    try:
        # Convert image list to the format required by the model
        image_inputs = [img for img in image_list]
        # Generate the test cases using the prompt and image inputs
        response = model.generate_content([prompt] + image_inputs)
        return response.text
    except Exception as e:
        raise e

# Function to create the prompt
def create_prompt(context_text=""):
    prompt = '''
        You are an experienced QA specialist known for developing detailed and effective test cases. Your task is to generate comprehensive test cases for the Swiggy app based on the provided screenshots. The steps involved in ordering a pizza are outlined below:

        1. **Select Address**: Choose or input the delivery address where the pizza will be sent.
        2. **Search Item**: Look up the pizza or other items you wish to order.
        3. **Select Restaurant**: Pick a restaurant that has the pizza you want.
        4. **Select Item**: Choose the exact pizza or items you want from the restaurant.
        5. **View Cart**: Review the items in your cart before moving on to payment.
        6. **Payment Method**: Select and apply your preferred payment method for completing the order.

        For each of these steps, create a detailed test case that includes:
            - **Description**: A brief overview of the test case's focus.
            - **Pre-conditions**: Any requirements or setup needed before running the test.
            - **Testing Steps**: A precise list of instructions to execute the test.
            - **Expected Result**: What should happen if the feature is functioning as intended.

        Use the screenshots provided to identify the necessary elements and procedures for each test case. Make sure each test case is clearly structured and easy for a QA team to follow. Include any additional context provided in the test cases as necessary.
    '''
    
    if context_text:
        prompt += f" {context_text}"
    
    return prompt
