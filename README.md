# Gemini Image-based App Testing Assistant

This Streamlit app integrates Google Gemini API to generate detailed test cases for app functionalities based on uploaded images (screenshots) and optional input text. The app is designed to help testers by generating step-by-step guides to test features of the app efficiently.

## Features
- Upload an image (app screenshot in `.jpg`, `.jpeg`, or `.png` format).
- Enter optional text as a prompt describing the app's functionality or feature.
- Use Google Gemini API to generate detailed test cases, including:
  - **Feature Description**: Brief explanation of what the feature does.
  - **Pre-conditions**: Setup or prerequisites for testing the feature.
  - **Testing Steps**: Clear, numbered steps to follow during testing.
  - **Expected Results**: Expected outcomes for each step.

## Requirements

Before running the app, ensure you have the following dependencies installed:

- `streamlit`
- `google-generativeai`
- `Pillow` (for image handling)

You can install them with:

```bash
pip install streamlit google-generativeai Pillow
```

## API Key Setup

To use Google Gemini API, obtain an API key and set it up in the script:

```python
google_api_key = 'Your API KEY'
```

## Running the App

1. Clone this repository.
2. Install the required dependencies using the above `pip install` command.
3. Run the app using Streamlit:

```bash
streamlit run app.py
```

4. Open the app in your browser at `http://localhost:8501`.

## Usage Instructions

1. Upload an image of your app (screenshot).
2. Enter optional text in the prompt field describing the feature to be tested.
3. Click on the "explain the image to me 👇" button to generate test cases.
4. The detailed response will be displayed below the button.

## Example

Here’s an example of a prompt:

```
Input Prompt: "Login screen with a username and password field."
```

The app will generate test cases for testing the login feature, including expected results.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

This README provides clear instructions on how to set up and use the app. You can adjust the content depending on any specific details of your project.
