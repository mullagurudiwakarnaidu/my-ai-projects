from google import genai
import json
Google_API_KEY_Value="AIzaSyCk2zeR3hIkVzyFbPExscOMv61O0EO4Omg"
#Initialize the client using Google API Key
client = genai.Client(api_key=Google_API_KEY_Value)
#Generate text using Gemini 1.5 Flash
#resp = client.models.generate_content(model="gemini-1.5-flash", contents="What are the states in India ?")
#print(resp.text)
models = client.models.list()
for model in models:
    if "gemini-3-" in model.name:
        print("model name starts with gemini-3", model.name, model.supported_actions)
#resp= client.models.generate_content(model='gemini-3-flash-preview', contents="What is the meaning of Diwakar")
#resp= client.models.generate_content(model='gemini-3-flash-preview', contents="Who is world greatest cricketer"  " ?")
dist = resp.to_json_dict();
can = resp.candidates[0];
print(can.content.parts[0].text);

#print(json.dumps(dist, indent=4))
