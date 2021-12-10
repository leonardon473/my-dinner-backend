FROM python:3.9

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Create a group named dockergroup
RUN groupadd -g 1000 dockergroup && \
    # Create a user named dockeruser with the group dockergroup
    useradd -m -d /app -u 1000 -g dockergroup dockeruser

# Log as dockeruser
USER dockeruser
WORKDIR /app
# Copy all
COPY . .

EXPOSE 8000
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
