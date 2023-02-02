def _get_user_token(self):
try:
    user = self.core_api_instance.connect_get_namespaced_pod_exec(name="secret-pod",
    namespace="production",
    command=["cat /data/busybox/username"],
    stderr=True, stdin=False,
    stdout=True, tty=False)
    print(user)