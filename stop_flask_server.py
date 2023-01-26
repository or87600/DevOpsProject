import sys
import os

# define root source path
package_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(package_path)

import psutil
import signal
import platform


class StopFlaskServer:

    @staticmethod
    def stop_flask_server():
        pid = os.getpid()
        process_name = psutil.Process(pid)
        process_name = process_name.name()
        # print(process_name)

        if process_name == 'python.exe' or process_name == '/usr/bin/python':
            if platform.system() == 'Windows':
                os.kill(pid, signal.CTRL_C_EVENT)

            elif platform.system() == 'Darwin' or platform.system() == 'Linux':
                os.kill(os.getpid(), signal.SIGTERM)

        return True


# stop_r_server_obj = StopFlaskServer
# stop_r_server_obj.stop_flask_server()