FROM ubuntu:latest

# Update the package manager and install the necessary packages
RUN apt-get update && apt-get install -y \
    bash \
    curl \
    wget \
    ca-certificates

# Set the default command to run when the container starts
CMD ["bash"]
