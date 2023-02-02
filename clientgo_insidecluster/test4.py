import time

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream


def exec_commands(api_instance):
    name = 'ubuntushelltest'
    resp = None
    try:
        resp = api_instance.read_namespaced_pod(name=name,
                                                namespace='default')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)

    # Calling exec interactively
    exec_command = ['/bin/sh']
    #print("Test1")
    resp = stream(api_instance.connect_get_namespaced_pod_exec,
                  name,
                  'default',
                  command=exec_command,
                  stderr=True, stdin=True,
                  stdout=True, tty=False,
                  _preload_content=False)
    commands = [
        'echo "This message will be echoed. ><"',
        'ls'
    ]

    while resp.is_open():
        resp.update(timeout=1)
        if commands:
            c = commands.pop(0)
            #print(c, "TEST2")
            print("Running command... %s\n" % c)
            resp.write_stdin(c + "\n")
            test = resp.readline_stdout(timeout=3)
            print(test)
        else:
            break

    resp.write_stdin("date\n")
    sdate = resp.readline_stdout(timeout=3)
    print("Server date command returns: %s" % sdate)
    resp.write_stdin("whoami\n")
    user = resp.readline_stdout(timeout=3)
    print("Server user is: %s" % user)

    resp.close()


def main():
    config.load_kube_config()
    try:
        c = Configuration().get_default_copy()
    except AttributeError:
        c = Configuration()
        c.assert_hostname = False
    Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()

    exec_commands(core_v1)


if __name__ == '__main__':
    main()