# Desktop-AI-Assistant
This is an AI assistant which takes speech as input and performs various tasks

# Document-Scanner

This is a smart document scanner made using Python.
This AI Assistant takes the audio input from the user using a microphone and performs tasks as directed.

## Working 
* The code is run and the AI assistant greets the user with a welcome message.
* It displays the input audio as text in the terminal and performs the directed task.
* If the assistant fails to understand the given command, then it displays the text on the terminal.

## STEPS TO RUN THIS PROJECT

1. Download the main.py file and place it in the project folder of the desired name.
2. Install the required packages.
* pyttsx3
* SpeechRecognition
* PyAudio
* openai
* pywin32
* wheel
3. Run the code.
4. Speak 'close' to exit.

### Tasks that the AI can perform

* Searching content in Wikipedia - the user needs to include the word - 'Wikipedia' to get the desired result.
** For example - what is a computer Wikipedia?  
* Launching youtube and Google websites -the user needs to include the word - 'open youtube' or 'open Google' in his speech to get the desired result.
* Displaying images in a specified folder -the user needs to include the word- 'show images' in his speech to get the desired result.
* Displaying the current time - the user needs to include the word- 'the time' in his speech to get the desired result.
* Launching VS Code editor -the user needs to include the word - 'open code' in his speech to get the desired result.
* Mailing -the user needs to include the word - 'email' followed by telling the content and receiver's email address in his speech to get the desired result.

### Libraries used

* pyttsx3 library for text-to-speech conversion
* speech_recognition library for performing speech recognition
* datetime library for date and time
* wikipedia library to access and parse data from Wikipedia
* webbrowser library to access web browser
* os library for using operating system dependent functionality
* smtplib library to send mail

### API used
* Google Web Speech API - for recognising voice input
* Microsoft Speech API (SAPI5) - for voice recognition and synthesis

