FROM dimaskiddo/alpine:python-2.7
MAINTAINER Dimas Restu Hidayanto <dimas.restu@student.upi.edu>

# Set Some Environment Variable
ENV NAME World

# Change Working Directory to Application Directory
WORKDIR /usr/local/app/

# Copy Application File to Specific Application Directory
COPY requirements.txt /usr/local/app/
COPY app.py /usr/local/app/

# Run Command to Install Application Requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose Application Port
EXPOSE 8080

# Run Application
CMD ["python", "app.py"]