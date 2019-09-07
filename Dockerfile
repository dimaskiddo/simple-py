FROM dimaskiddo/debian:python-3.7
MAINTAINER Dimas Restu Hidayanto <dimas.restu@student.upi.edu>

# Set Some Environment Variable
ENV NAME World

# Change Working Directory to Application Directory
WORKDIR /usr/local/app/

# Copy Dependencies File to Specific Application Directory
COPY requirements.txt /usr/local/app/

# Run Command to Install Application Requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application File to Specific Application Directory
COPY . /usr/local/app/

# Expose Application Port
EXPOSE 8080

# Run Application
CMD ["python", "app.py"]