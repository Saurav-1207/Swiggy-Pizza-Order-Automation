![alt text](https://github.com/Saurav-1207/Swiggy-Pizza-Order-Automation/blob/a1bbce4314e5b29103fedd29f264cdd938b148e0/Capture.PNG)

# Swiggy Pizza Order Automation Tool

This project is an innovative web-based solution designed to automatically create detailed test cases for pizza ordering through the Swiggy app. Utilizing advanced Google Generative AI and a multimodal approach, this tool processes screenshots and optional context to deliver a well-structured, step-by-step guide for testing various functionalities involved in ordering pizza.

## Table of Contents
- Overview
- Features
- How It Works
- Setup and Installation
- Usage
- Example Output
- Contributing

## Overview

The **Swiggy Pizza Order Automation Tool** uses a sophisticated Language Learning Model (LLM) to produce thorough testing instructions for the pizza ordering process on the Swiggy mobile app. By taking in screenshots and optional context, it generates a detailed list of test cases, which includes:

- **Description**: A concise summary of the test case.
- **Pre-conditions**: Requirements or setup needed before testing.
- **Testing Steps**: A sequence of instructions to perform the test.
- **Expected Result**: The anticipated outcome if the feature functions correctly.

## Features

- **Image Upload**: Users can upload multiple screenshots of the pizza ordering process.
- **Context Input**: An optional field for adding extra context or details.
- **Test Case Generation**: Automatically creates test cases using the Google Generative AI model.
- **Interactive Interface**: A modern, user-friendly web interface built with Streamlit.

## How It Works

1. **Image Upload**: Users upload screenshots related to the pizza ordering process they wish to test.
2. **Context Input**: Users can provide additional details or context as needed.
3. **Prompt Creation**: The tool generates a detailed prompt by combining the provided context with standard instructions.
4. **AI Processing**: The prompt and screenshots are sent to the Google Generative AI model (gemini-1.5-pro) for analysis.
5. **Output Generation**: The AI returns a structured set of test cases, which are then presented through the web interface.

## Setup and Installation

### Prerequisites

- Python 3.7 or newer
- Streamlit
- Pillow (for image processing)
- Google Generative AI SDK

### Installation

1. **Adjust Execution Policy** (For Windows PowerShell):
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   - For Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Clone the Repository**:
   ```bash
   git clone https://github.com/Saurav-1207/Swiggy-Pizza-Order-Automation.git
   ```

5. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure Google Generative AI Key**:
   - Replace `"YOUR_API_KEY"` in the code with your actual API key or set it as an environment variable.

7. **Run the Application**:
   ```bash
   streamlit run frontend.py
   ```

## Contributing

We welcome contributions! To propose changes, please fork the repository and submit a pull request. For major modifications, open an issue to discuss them first.

Feel free to adjust the repository URL and any other details as necessary.

---

Let me know if you need further adjustments!
