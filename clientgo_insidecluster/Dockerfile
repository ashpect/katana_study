FROM python:alpine3.7
RUN mkdir -p /k8s_python_code
COPY app2.py /
RUN pip install kubernetes
CMD python /app2.py