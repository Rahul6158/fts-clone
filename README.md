Supported Operations:

Text Translation: Allows users to input text in a specific language and translate it into another language from a wide range of supported languages.
Text-to-Speech Conversion: Converts the translated text into an audio file (MP3 format).
Download Options: Provides download links for the translated text in both Word (DOCX) and audio (MP3) formats.
Interface Elements:

Image Display: Shows an image at the top of the application window ("jangirii.png").
Input Area: Includes a text area where users can enter text for translation and conversion to speech.
Word Count: Displays the word count of the entered text.
Language Selection: Provides a dropdown menu to select the target language for translation and speech conversion.
Buttons: The "Translate - Convert to Speech and get Translated document" button triggers the translation and conversion processes.
Translation Process:

Google Translate: Utilizes the Google Translate API (googletrans library) for text translation. It breaks the text into chunks, translates them to the target language, and combines them into the final translated text.
Error Handling: Includes error handling to manage cases where the translation process encounters errors.
Text-to-Speech Conversion:

gTTS Library: Utilizes the gTTS library to convert the translated text into speech (MP3 format) in the selected target language.
Playback: Provides an audio player to listen to the generated speech and an option to download the audio file.
File Downloads:

Download Links: Generates download links for the translated text (in DOCX format) and the audio file (MP3 format) for easy access.
Platform Compatibility:

OS-specific Playback: Includes code to play the generated speech based on the operating system (Windows or Unix/Linux).
