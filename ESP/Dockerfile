# Use the official TensorFlow GPU image with Jupyter
FROM tensorflow/tensorflow:latest-gpu-jupyter

# Set the working directory
WORKDIR /ESP

# Install system dependencies
RUN apt-get update && apt-get install -y vim \
    iputils-ping \
    dnsutils \
    net-tools \
    curl
#    build-essential \
#    python3-dev \
#    libhdf5-dev \
#    libhdf5-serial-dev \
#    libhdf5-103 \
#    zlib1g-dev \
#    libjpeg-dev \
#    liblapack-dev \
#    libblas-dev \
#    gfortran \
#    pkg-config \
#    cmake \
#    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install --prefer-binary --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the entrypoint
# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
