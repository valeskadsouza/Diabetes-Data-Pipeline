FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY diabetic_data.csv .
COPY diabetes_loader.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD sleep 30 && python diabetes_loader.py
