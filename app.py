import time
from voice_generation import respond
from create_chat_engine import interact_with_llm
from ffmpeg_setup import set_ffmpeg_path
from voice_recognition import listen_for_command

def main():
    set_ffmpeg_path()
    while True:
        command = listen_for_command()
        output = interact_with_llm(command)
        print(output)
        if output:
            respond(output)
        #time.sleep(1)

if __name__ == "__main__":
    main()
