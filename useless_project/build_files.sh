#!/bin/bash

# Exit on error
set -e

# Install Python dependencies
pip install -r requirements.txt

# Run collectstatic
python manage.py collectstatic --no-input

# Create a dummy file for the static build output
mkdir -p staticfiles_build/static
