
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from diffusers import StableDiffusionPipeline
import torch
import os

from dotenv import load_dotenv
load_dotenv()


if "SLACK_BOT_USER_ID" not in os.environ:
    print("Please set the SLACK_BOT_USER_ID environment variable to the user ID of the Slack bot you want to use.")
    exit(1)

if "MODEL_PATH" not in os.environ:
    print("Please set the MODEL_PATH environment variable to the path of the model you want to use.")
    exit(1)

if "SLACK_BOT_AUTH_TOKEN" not in os.environ:
    print("Please set the SLACK_BOT_AUTH_TOKEN environment variable to the token of the Slack bot you want to use.")
    exit(1)

if "SLACK_APP_AUTH_TOKEN" not in os.environ:
    print("Please set the SLACK_APP_AUTH_TOKEN environment variable to the token of the Slack app you want to use.")
    exit(1)

model_id = os.environ["MODEL_PATH"]
bot_user_id = os.environ["SLACK_BOT_USER_ID"]
app = App(token=os.environ["SLACK_BOT_AUTH_TOKEN"])


@app.event("app_mention")
def ask_for_introduction(client, event, ack):
    user_id = event["user"]
    text = event["text"]

    if text.startswith(f"<@{bot_user_id}> draw me:"):
        prompt = text[23:]
        text = f"Hi <@{user_id}>! 🎉 I will try to draw and i will send the image.\nYou requested:```{prompt}```"
        ack()
        client.chat_postMessage(
            channel=event["channel"],
            text=text,
            thread_ts=event["event_ts"]
        )
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id, torch_dtype=torch.float16)
        pipe = pipe.to("cuda")
        image = pipe(prompt).images[0]
        file_path = f"/tmp/generated_image_{event['event_ts']}.png"
        image.save(file_path)
        client.files_upload(
            channels=event['channel'],
            thread_ts=event['event_ts'],
            file=file_path
        )


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_AUTH_TOKEN"]).start()
