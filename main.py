"""
This file contains code for the application "Gemini Pro Translator".
Author: GlobalCreativeApkDev
"""

# Importing necessary libraries
import google.generativeai as gemini
import sys
import os
from dotenv import load_dotenv
from mpmath import mp, mpf

mp.pretty = True


# Creating static functions to be used in this application.


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating main function used to run the application.


def main() -> int:
    """
    This main function is used to run the application.
    :return: an integer
    """

    load_dotenv()
    gemini.configure(api_key=os.environ['GEMINI_API_KEY'])

    # Asking user input values for generation config
    temperature: str = input("Please enter temperature (0 - 1): ")
    while not is_number(temperature) or float(temperature) < 0 or float(temperature) > 1:
        temperature = input("Sorry, invalid input! Please re-enter temperature (0 - 1): ")

    float_temperature: float = float(temperature)

    top_p: str = input("Please enter Top P (0 - 1): ")
    while not is_number(top_p) or float(top_p) < 0 or float(top_p) > 1:
        top_p = input("Sorry, invalid input! Please re-enter Top P (0 - 1): ")

    float_top_p: float = float(top_p)

    top_k: str = input("Please enter Top K (at least 1): ")
    while not is_number(top_k) or int(top_k) < 1:
        top_k = input("Sorry, invalid input! Please re-enter Top K (at least 1): ")

    float_top_k: int = int(top_k)

    max_output_tokens: str = input("Please enter maximum input tokens (at least 1): ")
    while not is_number(max_output_tokens) or int(max_output_tokens) < 1:
        max_output_tokens = input("Sorry, invalid input! Please re-enter maximum input tokens (at least 1): ")

    int_max_output_tokens: int = int(max_output_tokens)

    # Set up the model
    generation_config = {
        "temperature": float_temperature,
        "top_p": float_top_p,
        "top_k": float_top_k,
        "max_output_tokens": int_max_output_tokens,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = gemini.GenerativeModel(model_name="gemini-pro",
                                   generation_config=generation_config,
                                   safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    while True:
        clear()
        language_from: str = input("What language do you want to translate text from? ")
        convo.send_message("Is " + str(language_from) + " a communication language (one word response only)? ")
        language_from_check_answer: str = str(convo.last.text).upper()
        while language_from_check_answer != "YES":
            language_from = input("Sorry, invalid input! What language do you want to translate text from? ")
            convo.send_message("Is " + str(language_from) + " a communication language (one word response only)? ")
            language_from_check_answer = str(convo.last.text).upper()

        text_file_name: str = input("Please enter the path to the file containing the text you want to translate: ")
        text_file = open(text_file_name, "r")
        text_to_be_translated: str = text_file.read()
        text_file.close()
        language_to: str = input("What language do you want to translate text to "
                                 "(must be a different language to what you entered earlier)? ")
        convo.send_message("Is " + str(language_to) + " a communication language (one word response only)? ")
        language_to_check_answer: str = str(convo.last.text).upper()
        while language_to_check_answer != "YES" or language_to == language_from:
            language_to = input("Sorry, invalid input! What language do you want to translate text to "
                                "(must be a different language to what you entered earlier)? ")
            convo.send_message("Is " + str(language_to) + " a communication language (one word response only)? ")
            language_to_check_answer = str(convo.last.text).upper()

        convo = model.start_chat(history=[
        ])
        convo.send_message("Please translate the following text from "
                           + str(language_from) + " to " + str(language_to) + "\n\n" + str(text_to_be_translated))
        translated_text: str = str(convo.last.text)
        translated_file_name: str = input("Please enter the name of the file you want the translated text to be in "
                                          "(file name and extension only please): ")
        translated_file = open(os.path.join("texts", str(translated_file_name)), "w")
        translated_file.write(translated_text)
        translated_file.close()

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_translating: str = input("Do you want to continue translating text? ")
        if continue_translating != "Y":
            return 0


if __name__ == '__main__':
    main()
