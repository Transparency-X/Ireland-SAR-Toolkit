# Ireland SAR Toolkit v2.1 Dockerfile
# Build: docker build -t ireland-sar-toolkit .
# Run: docker run -it --rm -v $(pwd)/output:/app/output ireland-sar-toolkit

FROM python:3.11-slim

# Create non-root user
RUN useradd -m -s /bin/bash sartoolkit

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the toolkit
COPY . .

# Set up directories
RUN mkdir -p output forensic responses && chown -R sartoolkit:sartoolkit /app

# Switch to non-root user
USER sartoolkit

# Default command
CMD ["bash"]
