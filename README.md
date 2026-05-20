# get-started-vision-azure with Moondream

Project based off of Microsoft's training course [Get started with computer vision in Azure ](https://learn.microsoft.com/en-us/training/modules/get-started-vision-azure/) but instead of using an Azure model, I used a model from [moondream.](https://moondream.ai/)

## Prerequisites

- `python3`
- `uv` for dependency management
- Account with [moondream and API keys setup](https://moondream.ai/me/api-keys)

## Setup

1. Clone this repo.

2. Create a `.env` file with the following content. Replace the strings with valid values:

   ```
   API_KEY="<Your foundry API key>"
   ```

## Run

`uv run main.py`

You should see text output from the model summarizing the image.
