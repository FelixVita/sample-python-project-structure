# Data

This might not be needed for all projects.

And even if the project uses data, you'd probably usually want to .gitignore the contents of these folders, as data is usually just a product of running the code, and not something that should be version controlled.

If you plan to use a `data` folder like this , it's a good idea to include a README.md file in the `data` directory to explain what the contents are and where they came from.

## Raw data

Explain where the data came from.

## Processed data

Explain what scripts under the `scripts/` directory transformed which files under `raw/` into which files under `processed/` and `cleaned/`

## Cleaned data

Explain why each file under `cleaned/` exists, with optional references to particular notebooks. (Optional, especially when things are still in flux.)