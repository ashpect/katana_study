Steps to replicate :

    1. Create minikube cluster and run a ubuntu server which will act as main server.
    2. Apply pod_read.yaml or pod_list.yaml or create_deploy.yaml as per your need to provide incluster perms.
    3. Exec into the ubuntu server (main pod) and create files app.py , create_deployment.py or ip_pod.py as per your need. Copy paste the code as written in the repo.
    4. Make sure to have a docker image of a simple nginxserver or whatever you like , put that image in nginx-deployment.yaml and copy this file in main pod.
    5. Download python dependency and run create_deploy.py in main pod. Make sure to give the right path in create_deploy.py
    Your pod should run.
