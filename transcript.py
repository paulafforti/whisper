import whisper
import os

os.environ["path"] += ";C:\\Users\\pforti\\scoop\\shims"
model = whisper.load_model("large")

audio = whisper.load_audio("travelex.mp4")
#audio = whisper.pad_or_trim(audio) #tirar quando rodar de verdade
result = model.transcribe(audio,initial_prompt="o audio a seguir é uma entrevista com líder de tecnologia do banco, Blockchain, lean, data lake, six sigma, chatbot, genIa, smart contracts, BACEN, Quantum computing, metaverso, web 3.0, IA, inteligência artificial, DREX, tokenização, open finance, ESG, finanças sustentáveis, cyber, cibersegurança, cloud, on premise, hardware, escalabilidade")
print(result["text"])
