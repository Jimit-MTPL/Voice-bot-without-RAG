import whisper
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
import os

base_model_path = os.path.expanduser('~/.cache/whisper/large.pt')
base_model = whisper.load_model(base_model_path)

Settings.llm = Ollama(model="llama3.2:1b")