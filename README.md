# get-started-vision-azure

Project based off of Microsoft's training course [Get started with computer vision in Azure ](https://learn.microsoft.com/en-us/training/modules/get-started-vision-azure/)

## Prerequisites

- `python3`
- `uv` for dependency management
- Azure platform account with Foundry
- AI model with image input capability deployed in Foundry

## Setup

1. Clone this repo.

2. Create a `.env` file with the following content. Replace the strings with valid values:

   ```
   FOUNDRY_KEY="<Your foundry API key>"
   ENDPOINT="<Your foundry endpoint>"
   MODEL_NAME ="<Your model name>"
   ```

## Run

`uv run main.py`

You should see text output from the model summarizing the image.
