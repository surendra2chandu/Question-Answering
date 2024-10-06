# Use the latest CUDA 11.6 runtime image for Ubuntu 20.04
FROM nvidia/cuda:11.6.2-runtime-ubuntu20.04

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3-pip git

# Set the working directory inside the container
WORKDIR /llm

# Copy your project files into the container
COPY llm /src

# Install vLLM and other dependencies
RUN pip3 install vllm fastapi uvicorn

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run your script
CMD ["python3", "llm/src/main.py"]

#