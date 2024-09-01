# groqchatbot 🤖

groqchatbot is a high-performance conversational chatbot built using Streamlit and Groq's Language Processing Unit (LPU). It leverages the LangChain framework to provide a seamless and interactive chat experience. This chatbot can answer questions, provide information, and engage in friendly conversations with users.

## Features ✨

- **Fast and Efficient**: Powered by Groq's LPU for low latency and high performance.
- **Customizable**: Modify system prompts and choose from various models.
- **Interactive UI**: Built with Streamlit for an intuitive user interface.
- **Conversational Memory**: Maintains context with a configurable memory length.

## Installation 🛠️

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SauravSrivastav/groqchatbot.git
    cd groqchatbot
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Groq API Key**:
    - Sign up on the [Groq website](https://console.groq.com/keys) and generate an API key.
    - Set the API key as an environment variable:
        ```bash
        export GROQ_API_KEY=your_groq_api_key
        ```

## Running the Application 🚀

1. **Start the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your browser** and navigate to `http://localhost:8501` to interact with the chatbot.

## Usage Instructions 📖

1. **Enter your Groq API Key** in the sidebar.
2. **Customize the system prompt** to guide the chatbot's behavior.
3. **Choose a model** from the dropdown menu.
4. **Adjust the conversational memory length** using the slider.
5. **Ask a question** in the text input box and get responses from the chatbot.

## Detailed Code Explanation 🧩

### Main Application (`app.py`)

#### Imports and Setup
```python:conversational-chatbot-groq/app.py
startLine: 1
endLine: 17
```

- Import necessary libraries and modules.
- Set up the main function for the Streamlit application.

#### Sidebar Configuration
```python:conversational-chatbot-groq/app.py
startLine: 24
endLine: 32
```

- Provide instructions for obtaining the Groq API key.
- Input field for the user to enter their API key.

#### Display and Customization
```python:conversational-chatbot-groq/app.py
startLine: 35
endLine: 49
```

- Display the Groq logo.
- Set the title and greeting message.
- Add customization options for system prompts and model selection.

#### Model Manuals and Memory Configuration
```python:conversational-chatbot-groq/app.py
startLine: 67
endLine: 83
```

- Provide user manuals for each model.
- Configure conversational memory length.

#### Chat Interaction
```python:conversational-chatbot-groq/app.py
startLine: 85
endLine: 95
```

- Initialize session state for chat history.
- Save context for previous messages.

#### Initialize Groq Chat and Handle User Input
```python:conversational-chatbot-groq/app.py
startLine: 98
endLine: 143
```

- Initialize the Groq LangChain chat object.
- Construct a chat prompt template.
- Create a conversation chain and handle user questions.
- Display chatbot responses and handle errors.

## Contributing 🤝

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
## 📞 Contact Us

Have questions or suggestions? Reach out to us:

- 📧 Email: [Sauravsrivastav2205@gmail.com](mailto:Sauravsrivastav2205@gmail.com)
- 💼 LinkedIn: [in/sauravsrivastav2205](https://www.linkedin.com/in/sauravsrivastav2205)
- 🐙 GitHub: [https://github.com/SauravSrivastav](https://github.com/SauravSrivastav)

---
Happy Chatting! 🎉
