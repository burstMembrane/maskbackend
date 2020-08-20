# Use the official image as a parent image.
FROM tensorflow/tensorflow:1.15.0-gpu-py3

RUN pip install scipy==1.3.3
RUN pip install requests==2.22.0
RUN pip install Pillow==6.2.1

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8000


