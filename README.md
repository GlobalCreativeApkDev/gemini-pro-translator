# gemini-pro-translator

**Gemini Pro Translator** is a translation application inspired by Google Translate and integrated with Gemini Pro.

# Source Code

The source code of the application **Gemini Pro Translator** is available in [Source Code](https://github.com/GlobalCreativeApkDev/gemini-pro-translator/blob/master/main.py).

# Installation

```
pip install gemini-pro-translator
```

# How to Use the Application?

Pre-requisites:

1. [Python](https://www.python.org/downloads/) installed in your device.
2. .env file in the same directory as <GEMINI_PRO_TRANSLATOR_DIRECTORY> and has the value of GEMINI_API_KEY.

First, open a Terminal or Command Prompt window and run the following command.

```
cd <GEMINI_PRO_TRANSLATOR_DIRECTORY>
python3 main.py
```

**Note:** Replace <GEMINI_PRO_TRANSLATOR_DIRECTORY> with the path to the directory of the application **Gemini Pro Translator**.

Then, the application will start with something looking like in the screenshot below.

![Application](images/Application.png)

You will then be asked to input the following values.

1. Temperature - between 0 and 1 inclusive
2. Top P - between 0 and 1 inclusive
3. Top K - at least 1
4. Max output tokens - at least 1

The following screenshot shows what is displayed after inputting the mentioned values.

![Translator](images/Translator.png)

You will be required to input the following pieces of information.

1. The name of the language you want to translate text from.
2. The path of the file containing the text to be translated.
3. The name of the language you want to translate text to (must be different from the one in step 1).
4. The name of the file you want the translated text to be placed in (include the file name and its extension only).

Once you enter the values mentioned above, the file containing the translated text will be created inside "texts" 
directory. Then, you will be asked whether you still want to continue unit testing or not. If you enter 'Y', you will 
be redirected to an application window like in screenshot above. Else, you will exit the application.

![Translator End](images/Translator%20End.png)

Below demonstrates how the file containing the translated text looks like.

![Translated Text](images/Translated%20Text.png)
