# Use Python slim image for smaller image size
FROM python:3.11-slim


WORKDIR /app

RUN pip install pipenv
COPY ["Pipfile","Pipfile.lock", "./"]

RUN pipenv install --system --deploy

# Copy all the files from the 'depression_predictor' directory into the container
COPY depression_predictor/ ./depression_predictor/



# Expose port 9696 for the application
EXPOSE 9696

# Start the application using Gunicorn, ensuring the path is correct
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "depression_predictor.app:app"]