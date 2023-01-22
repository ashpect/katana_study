#equivalent to kubectl get pods --all-namespaces

from kubernetes import client, config

#loads cubeconfig file in .cube directory
config.load_kube_config()
#config.load_incluster_config()

#core v1 api to list npods for all namespaces
v1 = client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

