# official python runtime image
FROM python:3.11 AS backend-build

# working directory is flaskapp
WORKDIR /flaskapp

# Install all the dependencies needed
RUN python3 -m pip install flask
RUN python3 -m pip install flask-cors
RUN python3 -m pip install pandas
RUN python3 -m pip install seaborn
RUN python3 -m pip install pysqlite3
RUN python3 -m pip install numpy
RUN python3 -m pip install matplotlib

# Copy the current local directory to the container with basically the same name
COPY ./pythonbackend ./pythonbackend

# Run the database initializer script - reads an csvfile and creates an local db out of it
RUN python3 pythonbackend/dbinitializer.py

# Expose the port the Flask app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python3", "pythonbackend/flaskreceiver.py"]
