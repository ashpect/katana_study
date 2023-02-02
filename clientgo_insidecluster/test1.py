from kubernetes import config
from kubernetes.client.api import core_v1_api
from kubernetes.stream import stream


def exec_commands(api_instance):

    resp = stream(self.core_api_instance.connect_get_namespaced_pod_exec,
                  'ubuntushelltest',
                  'default',
                  command=['touch lalsa.txt'],
                  stderr=True, stdin=True,
                  stdout=True, tty=True,
                #   _preload_content=False
                  )

    while resp.is_open():
        resp.update(timeout=1)
        if resp.peek_stdout():
            print("%s" % resp.read_stdout())
        if resp.peek_stderr():
            print("%s" % resp.read_stderr())

        command = input()

        if command == "exit":
            break
        else:
            resp.write_stdin(command + "\n")

    resp.close()


def main():
    config.load_kube_config("~/.kube/config")
    core_v1 = core_v1_api.CoreV1Api()
    exec_commands(core_v1)


if __name__ == '__main__':
    main()