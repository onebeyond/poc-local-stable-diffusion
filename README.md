# poc-local-stable-diffusion

- [poc-local-stable-diffusion](#poc-local-stable-diffusion)
  - [environment variables](#environment-variables)
  - [Model provisioning](#model-provisioning)
  - [Running the app](#running-the-app)

PoC of local implementation of stable diffusion with slack

## environment variables

You need to setup a `.env` file with this information:

- **SLACK_BOT_AUTH_TOKEN** is the token that we get from Slack when we register our Slack app. This token is used to authenticate our app, and it allows us to access the Slack API.

- **SLACK_APP_AUTH_TOKEN** is the token that we get from Slack when we register our Slack app. This token is used to authenticate our app, and it allows us to access the Slack API.

- **SLACK_BOT_USER_ID** is the token that we get from Slack when we register our Slack app. This token is used to authenticate our app, and it allows us to access the Slack API.

- **MODEL_PATH** is the path to the model that we want to use for our Slack bot. This is the path to the model that we want to use for our Slack bot.

## Model provisioning

Just head to [huggingface.co](https://huggingface.co) and download the model and put it in the `model` folder defined at `MODEL_PATH`.

This proof of concept uses the `stabilityai/stable-diffusion-2-1` model.

## Running the app

You need to have python 3.10 installed at least, we recommend the use of a virtual environment to handle it

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

> ⚠️ You need a capable CUDA GPU to run this model, if you don't have one, you can use Google Colab/Azure AI or any cloud provided GPU instance to run it.
