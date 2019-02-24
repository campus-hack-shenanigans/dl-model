"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="so this fuck the wauless too oh me back the way the cold en to stop this back motherfuck every man on all to slook that this back in a ball all the dont some em and the pun deed in a pid a a latte so fuck met man I said all the way to the bood no I wanna stop the back up come me pack up a fuckin too rup it with I thing all be here ut the dont go to here of the man you gonna see shady touch so sid ever man for the pant as this cloos the mister back a stick made pit on the rat some my horas you tought the car that I dont take and I dont get and do the fliped all and I just dont give a fuck fuck")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3,
    speaking_rate=1.25,
    pitch=-10.0)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')