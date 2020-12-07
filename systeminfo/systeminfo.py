import platform,socket,re,uuid,json,logging


def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def print_system_info():
    info = json.loads(getSystemInfo())

    print("platform: {0}\nplatform release: {1}\nplatform-version: {2}\narchitecture: {3}\n"
          "hostname: {4}\nip address: {5}\nmac-address: {6}\nprocessor: {7}"
          .format(info['platform'], info['platform-release'], info['platform-version'], info['architecture'],
                  info['hostname'], info['ip-address'], info['mac-address'], info['processor']))
