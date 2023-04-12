from jinja2 import Template

deployment = Template("""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ nombre }}
spec:
  replicas: {{ replicas }}
  selector:
    matchLabels:
      app: {{ nombre }}
  template:
    metadata:
      labels:
        app: {{ nombre }}
    spec:
      containers:
        - name: {{ nombre }}
          image: {{ imagen }}
          ports:
            - containerPort: {{ puerto }}
""")