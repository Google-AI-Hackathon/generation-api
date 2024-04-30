# from app.data.voices.voices import voices
# from app.models.TTS.voice import Voice
# from app.models.agent.identity import Identity
# from random import randint

# def get_random_voice(gender=1, last_voice: [Voice] = None):
#     filtred_voices = [voice for voice in voices if (voice.ssml_gender.value == gender) and (voice not in last_voice)]  
#     return filtred_voices[randint(0,len(filtred_voices)-1)]

# # TODO: add the gender of the agent to the function
# # @Kamel: when you add the gender of the agent to the model, you can use it here
# def get_agents_voice(lenght : int , agents: [Identity]):
#     voices = []
#     for i in range(lenght):
#         voices.append(get_random_voice(gender=1, last_voice=voices))
#     return voices