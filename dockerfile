FROM python:3.10-slim
ENV TOKEN='7645600372:AAEwYRnp7NVZuP9UZCfBCG1ix5w4Z2Ve99w'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "newbot.py" ]
