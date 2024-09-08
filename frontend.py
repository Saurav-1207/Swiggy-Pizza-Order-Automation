import streamlit as st
from PIL import Image
from backend import configure_genai, generate_test_cases, create_prompt

# Set the page configuration for a modern look
st.set_page_config(
    page_title="🍕 Swiggy Pizza Order Automation Tool",
    page_icon="🍕",
    layout="centered",  # Centralized layout for a clean appearance
)

# Initialize the Generative AI model
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
model = configure_genai(API_KEY)  # Model initialized here

# Title with emoji and clean design
st.title("🍕 Swiggy Pizza Order Automation Tool")

# Add a welcoming description for the app
st.markdown("""
    #### Streamline your test case creation for ordering pizza on Swiggy!  
    Upload your screenshots and let AI generate detailed test cases to simplify your QA process.
""")

# Section for uploading images with an improved label
st.markdown("#### Upload Screenshots")
uploaded_files = st.file_uploader(
    "Upload screenshots (JPEG or PNG)", 
    type=["jpg", "jpeg", "png"], 
    accept_multiple_files=True,
    help="You can upload multiple images to provide more context for test cases."
)

# Optional context input with placeholder for better guidance
context_text = st.text_input(
    "Provide additional test case context (optional):", 
    placeholder="E.g., focus on payment method, specific filters, etc."
)

# If files are uploaded, show the images in a grid for a modern look
if uploaded_files:
    image_list = [Image.open(uploaded_file) for uploaded_file in uploaded_files]

    # Display the images in a grid layout
    st.markdown("### Uploaded Images Preview")
    cols = st.columns(len(image_list))  # Create dynamic columns
    for idx, image in enumerate(image_list):
        with cols[idx]:
            st.image(image, caption=f"Image {idx+1}", use_column_width=True)

    # Button to generate the test cases with a clear call to action
    if st.button('🚀 Generate Test Cases'):
        with st.spinner('AI is working on generating test cases...'):
            try:
                # Prepare the prompt based on the input context
                prompt = create_prompt(context_text)
                
                # Call backend to generate test cases, passing model
                result = generate_test_cases(model, prompt, image_list)
                
                # Show success message and the results
                st.success("Test Cases Generated Successfully! 🎉")
                st.markdown("### Generated Test Cases:")
                st.markdown(result, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred while generating test cases: {e}")
else:
    st.info("Upload screenshots to begin.")

# Footer for branding and professionalism
st.markdown(
    """
    ---
    *Powered by Google Generative AI*  
    Designed to simplify your pizza ordering test case creation! 🍕  
    """
)


