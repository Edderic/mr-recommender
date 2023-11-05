# mr-recommender
Mask/Respirator Recommender

## Installation

### Poetry

Poetry is used to manage Python dependencies. [Installation guide](https://python-poetry.org/docs/#installation).

Useful commands below. The following commands assume you are current working directory is that of `mr-recommender`.

`poetry install` will install dependencies listed in `pyproject.toml` into some environment.
`poetry shell` will load the environment.

## Environment Variables

Ensure you have the following variables set:

`MR_RECOMMENDER_GOOGLE_SHEETS_CLIENT_SECRET_PATH`: This points to a JSON file that has the credentials to access tho Google Sheets API. Ask Edderic for details so he can share it with you securely.
