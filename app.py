import streamlit as st
import os
from groq import Groq
import random

from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from requests.exceptions import HTTPError


def main():
    """
    This function is the main entry point of the application. It sets up the Groq client, the Streamlit interface, and handles the chat interaction.
    """
    
    # Provide instructions on obtaining the Groq API key
    st.sidebar.title("API Key Instructions")
    st.sidebar.write("To use this chatbot, you need a GROQ API Key. You can obtain it by signing up on the Groq website and generating an API key in your account settings.")
    st.sidebar.write("You can generate your API key here: [Groq API Key](https://console.groq.com/keys)")
    groq_api_key = st.sidebar.text_input("Enter your GROQ API Key:", type="password")

    if not groq_api_key:
        st.error("Please enter your GROQ API Key to proceed.")
        return

    # Display the Groq logo
    spacer, col = st.columns([5, 1])  
    with col:  
        st.image('https://github.com/SauravSrivastav/groqchatbot/blob/main/data/groqcloud_darkmode.png')

    # The title and greeting message of the Streamlit application
    st.title("Chat with Groq!")
    st.write("Hello! I'm your friendly Groq chatbot. I can help answer your questions, provide information, or just chat. I'm also super fast! Let's start our conversation!")

    # Add customization options to the sidebar
    st.sidebar.title('Customization')
    st.sidebar.write("System prompts guide the chatbot's behavior. Here are some examples:")
    st.sidebar.write("- 'You are a helpful assistant.'")
    st.sidebar.write("- 'You are an expert in cryptocurrency.'")
    st.sidebar.write("- 'You are a friendly and engaging conversationalist.'")
    system_prompt = st.sidebar.text_input("System prompt:", value="You are a helpful assistant.")

    st.sidebar.write("Choose a model and read the user manual for guidance:")
    model = st.sidebar.selectbox(
        'Choose a model',
        [
            'gemma2-9b-it',  # Gemma 2 9B: Developed by Google, supports a context window of 8,192 tokens.
            'gemma-7b-it',  # Gemma 7B: Developed by Google, supports a context window of 8,192 tokens.
            'llama3-groq-8b-8192-tool-use-preview',  # Llama 3 Groq 8B Tool Use (Preview): Developed by Groq, supports a context window of 8,192 tokens.
            'llama-3.1-70b-versatile',  # Llama 3.1 70B (Preview): Developed by Meta, supports a context window of 131,072 tokens.
            'llama-3.1-8b-instant',  # Llama 3.1 8B (Preview): Developed by Meta, supports a context window of 131,072 tokens.
            'llama-guard-3-8b',  # Llama Guard 3 8B: Developed by Meta, supports a context window of 8,192 tokens.
            'llama3-70b-8192',  # Meta Llama 3 70B: Developed by Meta, supports a context window of 8,192 tokens.
            'llama3-8b-8192',  # Meta Llama 3 8B: Developed by Meta, supports a context window of 8,192 tokens.
            'mixtral-8x7b-32768',  # Mixtral 8x7B: Developed by Mistral, supports a context window of 32,768 tokens.
        ]
    )

    # Provide user manual for each model
    model_manuals = {
        'gemma2-9b-it': "Gemma 2 9B: Developed by Google, supports a context window of 8,192 tokens. Ideal for general-purpose conversations.",
        'gemma-7b-it': "Gemma 7B: Developed by Google, supports a context window of 8,192 tokens. Suitable for lightweight tasks.",
        'llama3-groq-8b-8192-tool-use-preview': "Llama 3 Groq 8B Tool Use (Preview): Developed by Groq, supports a context window of 8,192 tokens. Great for tool integration.",
        'llama-3.1-70b-versatile': "Llama 3.1 70B (Preview): Developed by Meta, supports a context window of 131,072 tokens. Best for extensive context and detailed responses.",
        'llama-3.1-8b-instant': "Llama 3.1 8B (Preview): Developed by Meta, supports a context window of 131,072 tokens. Fast and efficient for quick responses.",
        'llama-guard-3-8b': "Llama Guard 3 8B: Developed by Meta, supports a context window of 8,192 tokens. Focused on security and privacy.",
        'llama3-70b-8192': "Meta Llama 3 70B: Developed by Meta, supports a context window of 8,192 tokens. High performance for complex tasks.",
        'llama3-8b-8192': "Meta Llama 3 8B: Developed by Meta, supports a context window of 8,192 tokens. Balanced for general use.",
        'mixtral-8x7b-32768': "Mixtral 8x7B: Developed by Mistral, supports a context window of 32,768 tokens. Excellent for long-form content generation.",
    }
    st.sidebar.write(model_manuals[model])

    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value = 5)

    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    user_question = st.text_input("Ask a question:")

    # session state variable
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
    else:
        for message in st.session_state.chat_history:
            memory.save_context(
                {'input':message['human']},
                {'output':message['AI']}
                )


    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
            groq_api_key=groq_api_key, 
            model_name=model
    )


    # If the user has asked a question,
    if user_question:

        # Construct a chat prompt template using various components
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=system_prompt
                ),  # This is the persistent system prompt that is always included at the start of the chat.

                MessagesPlaceholder(
                    variable_name="chat_history"
                ),  # This placeholder will be replaced by the actual chat history during the conversation. It helps in maintaining context.

                HumanMessagePromptTemplate.from_template(
                    "{human_input}"
                ),  # This template is where the user's current input will be injected into the prompt.
            ]
        )

        # Create a conversation chain using the LangChain LLM (Language Learning Model)
        conversation = LLMChain(
            llm=groq_chat,  # The Groq LangChain chat object initialized earlier.
            prompt=prompt,  # The constructed prompt template.
            verbose=True,   # Enables verbose output, which can be useful for debugging.
            memory=memory,  # The conversational memory object that stores and manages the conversation history.
        )
        
        try:
            # The chatbot's answer is generated by sending the full prompt to the Groq API.
            response = conversation.predict(human_input=user_question)
            message = {'human':user_question,'AI':response}
            st.session_state.chat_history.append(message)
            st.write("Chatbot:", response)
        except HTTPError as e:
            if e.response.status_code == 503:
                st.error("Service is currently unavailable. Please try again later.")
            else:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
