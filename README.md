# Jarvis_AI
# Voice Assistant using GoogleBard API


This is a Python-based Voice Assistant that leverages the power of the GoogleBard API for natural language processing and understanding user queries. The assistant can perform a variety of tasks, such as searching on Wikipedia, opening YouTube, opening Google, playing music, sending WhatsApp messages, and more.

### Installation

Before running the Voice Assistant, ensure you have the required libraries installed. Use the following commands to install the dependencies:

```bash
pip install pyttsx3
pip install speech_recognition
pip install wikipedia
pip install pywhatkit
pip install webbrowser
pip install pyaudio
```

Additionally, you need to have GoogleBard installed:

```bash
pip install GoogleBard 
pip install bardapi
```

To get the API key for GoogleBard, follow these steps:

1. Install the necessary libraries as mentioned above.
2. Go to your Bard chat and open developer options.
3. Navigate to Application > Storage > Cookies > https://googlebard.com.
4. Click on the `__Secure-1PSID` cookie to find your API key.

Once you have the API key, you can use it to make queries to the GoogleBard API.

### Features

The Voice Assistant comes with the following features:

1. Greeting: The assistant will greet you based on the current time of the day (morning, afternoon, or evening).

2. Wikipedia Search: You can ask the assistant to search for information on Wikipedia. Just say "Wikipedia" followed by your query.

3. Opening Google: You can ask the assistant to open Google and search for specific queries.

4. Opening YouTube: Ask the assistant to open YouTube and play your desired song.

5. Playing Music: The assistant can play random songs from a local music directory.

6. Opening Visual Studio Code: The assistant can open Visual Studio Code for you.

7. Sending WhatsApp Messages: The assistant can send WhatsApp messages to your contacts. Make sure to define contacts and their numbers in the code.

8. Asking Bard: The assistant can answer general queries using the GoogleBard API.

### Usage

1. Run the script and allow the assistant to access your microphone.
2. The assistant will greet you and wait for your command.
3. Give your command using natural language.

### Disadvantages

While this Voice Assistant is functional, it has some limitations and areas for improvement:

1. **Dependency on Internet Connection:** As the assistant uses online services like GoogleBard and PyWhatKit, it requires an active internet connection. If the connection is slow or unavailable, the assistant's performance may be affected.

2. **Limited Voice Recognition Accuracy:** The accuracy of voice recognition depends on the quality of the user's speech and background noise. In some cases, the assistant may misinterpret commands.

3. **Security Concerns:** The assistant's usage of external APIs may raise privacy and security concerns. Ensure that you trust the APIs and the data they process.

4. **Lack of Customization:** The assistant is hardcoded with specific functionalities, and adding new features or customizations may require substantial modifications to the code.

### Seeking Improvements

If you have any suggestions or improvements to enhance the Voice Assistant, feel free to contribute to the code. The GitHub repository for the project is [Voice Assistant](https://github.com/username/voice-assistant](https://github.com/LikithMeruvu/Jarvis_AI)).

Your contributions are valuable and can help make the Voice Assistant more efficient and user-friendly.

**Note:** The Voice Assistant is a personal project, and its functionalities may vary depending on GoogleBard API usage and other services. Use the Voice Assistant responsibly and abide by the API provider's terms and conditions.

### Acknowledgments

- Special thanks to the creators of GoogleBard and other libraries used in the Voice Assistant.
- Thanks to the open-source community for providing valuable resources and tutorials.

**Disclaimer:** This project is for educational and personal use only. The author does not take responsibility for any misuse or unintended consequences of the Voice Assistant. Use the Voice Assistant responsibly and within the boundaries of applicable laws and regulations.
