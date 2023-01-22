#kubectl create -f nginx-deployment.yaml
#Creates a deployment using AppsV1Api from file nginx-deployment.yaml.


from os import path

import yaml

from kubernetes import client, config

    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    
#config.load_kube_config()
config.load_incluster_config()

print("hello")
print(path.dirname(__file__))
print("hello2")
print("hello3")
with open(path.join(path.dirname(__file__), "nginx-deployment.yaml")) as f:
    print("hello4")
    dep = yaml.safe_load(f)
    k8s_apps_v1 = client.AppsV1Api()
    print(k8s_apps_v1)
    resp = k8s_apps_v1.create_namespaced_deployment(
        body=dep, namespace="default")
    print("Deployment created. status='%s'" % resp.metadata.name)