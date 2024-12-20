# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit uses
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "senti.py", "--server.port=8501", "--server.address=0.0.0.0"]

