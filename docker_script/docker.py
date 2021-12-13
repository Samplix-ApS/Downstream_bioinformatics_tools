import subprocess
import sys, getopt
import os
import re

try:
    import pandas as pd
except ModuleNotFoundError:
    pip_install = subprocess.run([sys.executable, '-m', 'pip', 'install', 'pandas'])
    if pip_install.returncode != 0:
        print('Please install python package: pandas')
        quit()
    else:
        import pandas as pd

try:
    import torch
except ModuleNotFoundError:
    pip_install = subprocess.run([sys.executable, '-m', 'pip', 'install', 'torch'])
    if pip_install.returncode != 0:
        print('Please install python package: torch')
        quit()
    else:
        import torch

docker_tools = 'samplix/samplix_analysis_tools:latest'

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def validate_CUDA():
    CUDA_available = torch.cuda.is_available()
    if CUDA_available != True:
        print('\n###################################################')
        print('WARNING! Cannot detect CUDA installation.\nNVIDIA GPUs are necessary to use Basecalling tools.\nPlease install the necessary drivers.')
        print('\n###################################################')
        quit()

def print_help():
    print ('docker.py <arguments>\n')
    print('This script is used to initiate or stop the docker container\n If initiating, the newest docker will be pulled automatically.\n')
    print('-i       Input-data path\n')
    print('-r       Refseq-data path\n')
    print('-b       Set to true to load basecalling tools (e.g. activate gpus)\n')
    print('-s       Set to stop to stop the docker container. \n')
    print('-p       Optional. Choose which port to use. Default is port 8089\n')
    print('-x       Set to true to use secure port 4430\n')
    print('--bash   Set to true to enter bash mode. Type exit to exit bash\n')


def docker_container_ID():
    #print('Obtaining docker Container ID')
    call_docker = subprocess.Popen(['docker', 'ps', '-a'],stdout=subprocess.PIPE)
    stdout, stderr = call_docker.communicate()
    docker_ps=stdout.decode("utf-8")
    docker_ps=docker_ps.split('\n')

    list_up = []
    list_exited = []
    for line in docker_ps:
        if len(line) > 1:
            line_replace = re.sub('(?<=[^ ])( )(?=[^ ])', '_', line.lower())
            line_split = line_replace.split()
            if bool(re.match('up', line_split[4])):
                status = 'up'
                port_1 = re.search('(?<=.:)(.*?)(?=\->)',line_split[5]).group()
                port_2 = re.search('(?<=\->)(.*?)(?=\/)',line_split[5]).group()
                port_range = ':'.join([port_2, port_1])
                list_up.append((line_split[0], status, line_split[4], port_range))
                continue
            if bool(re.match('exited', line_split[4])):
                status = 'exited'
                list_exited.append((line_split[0], status, line_split[4]))
                continue

    if len(list_up) == 0:
        print('Docker does not seem to be running.')
        quit()

    df = pd.DataFrame(list_up)
    df.columns = ['Container_ID', 'Status', 'Time', 'Port_range']
    print(df)

    if len(list_up) > 1 :
        print('More than one docker container is running')
        print('Which container should be stopped?')

        match = 'false'
        count = 0
        while(match == 'false'):
            if count >= len(list_up):
                print('Please provide correct Container_ID')
            session_id = input('Container_ID: ')
            for container_id, status, time, port_range in list_up:
                count += 1
                if container_id == session_id:
                    match = 'true'

        return session_id

    try:
        session_id = list_up[0][0]
    except IndexError:
        print('Docker does not seem to be running.')
        quit()

    return session_id

def docker_stop(stop_arg):
    if stop_arg == 'stop':
        session_id = docker_container_ID()
        print('Stopping docker container:', session_id)
        call_docker = subprocess.run(['docker', 'stop', session_id])
        print('Docker container stopped')

def docker_pull():
    print('Pulling latest docker')
    call_docker = subprocess.run(['docker', 'pull', docker_tools])

def return_code_start(process):
    if process.returncode == 125:
        print('\n######################################################################')
        print('DOCKER INITIATION FAILED\n')
        print('Docker exit code 125: Error in Docker daemon')
        try:
            with HiddenPrints():
                docker_container_ID()
            print('\nDocker is already running:')
            docker_container_ID()
        except ValueError as e:
                print(e)
        print('\n######################################################################')
        quit()
    elif process.returncode == 126:
        print('DOCKER INITIATION FAILED')
        print('Docker exit code 126: Permission problem or command is not executable')
        quit()

def docker_analysis(input_data, refseq_data, port_range, basecalling_tools, secure):
    if basecalling_tools == 'false':
        validate_dir(input_data, 'input-data')
        validate_dir(refseq_data, 'refseq-data')
        print('\nInitiating docker Reference and Analysis tools')
        if secure == 'false':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '-v',input_data, '-v', refseq_data, '-p', port_range, docker_tools],stdout=subprocess.PIPE)
        if secure == 'true':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '-v',input_data, '-v', refseq_data,'-e', 'SECURE=true', '-p', port_range, docker_tools],stdout=subprocess.PIPE)
        stdout, stderr = call_docker.communicate()
        return_code_start(call_docker)
        docker_session=stdout.decode("utf-8").strip()[0:12]
        print('Docker container initiated:', docker_session)
        print('Port range:', port_range)
        print('Input-data:', input_data)
        print('Refseq-data:', refseq_data)

def validate_args(stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure, bash):
    if stop_arg == '':
        stop_arg = 'false'

    if stop_arg.lower() != 'stop' and stop_arg != 'false':
        print('Invalid -s argument. Must be stop')
        quit()

    if basecalling_tools == '':
        basecalling_tools = 'false'

    if basecalling_tools != 'true' and basecalling_tools != 'false':
        print('Invalid -b argument. Must be true, false, or no argument given')
        quit()

    if port != '':
        try:
            port_int = int(port)
        except ValueError:
            print('Port is not an integer')
            quit()


    if input_dir != '':
        if os.path.exists(input_dir) == False:
            print('Input directory does not exist')
            quit()
        else:
            input_dir = os.path.abspath(input_dir)

    if refseq_dir != '':
        if os.path.exists(refseq_dir) == False:
            print('Reference directory does not exist')
            quit()
        else:
            refseq_dir = os.path.abspath(refseq_dir)

    if secure == '' or secure.lower() == 'false':
        secure = 'false'
    elif secure.lower() == 'true':
        secure = 'true'
    else:
        print('Unknown argument for secure. Use "true" to set to true. Exiting program')
        quit()

    if bash == '' or bash.lower() == 'false':
        bash = 'false'
    elif bash.lower() == 'true':
        bash = 'true'
    else:
        print('Unknown argument for bash. Use "true" to set to true. Exiting program')
        quit()

    return stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure, bash

def get_dir(input_dir, refseq_dir):
    if input_dir != '':
        input_data = input_dir +':/input-data'
    else:
        input_data = 'None'
    if refseq_dir != '':
        refseq_data = refseq_dir +':/refseq-data'
    else:
        refseq_data = 'None'

    return input_data, refseq_data

def validate_dir(dir, string_dir):
    if dir == 'None':
        print('\nNo', string_dir, 'directory given. Exiting')
        quit()

def docker_basecall(input_data, port_range, basecalling_tools, secure):
    if basecalling_tools == 'true':
        validate_dir(input_data, 'input-data')
        validate_CUDA()
        print('\nInitiating docker basecalling_tools')
        if secure == 'false':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '--gpus', 'all', '-v',input_data,'-p', port_range, docker_tools],stdout=subprocess.PIPE)
        if secure == 'true':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '--gpus', 'all', '-v',input_data,'-e','SECURE=true','-p', port_range, docker_tools],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = call_docker.communicate()
        return_code_start(call_docker)
        docker_session=stdout.decode("utf-8").strip()[0:12]
        print('Docker container initiated:', docker_session)
        print('Port range:', port_range)
        print('Input-data:', input_data)

def get_port_range(port, secure):
    if secure == 'true':
        if port == '':
            port = '4430'
        port_range = port +':4430'

        return port_range

    if secure == 'false':
        if port == '':
            port = '8089'
        port_range = port +':8080'

        return port_range

def docker_bash(bash):
    if bash == 'true':
        session_id = docker_container_ID()
        print('Initating docker bash in', session_id)
        print('Type exit to exit bash')
        call_docker = subprocess.run(['docker', 'exec','-it', session_id, 'bash'])



def docker_start(stop_arg, input_dir, refseq_dir, basecalling_tools, port, secure, bash):
    if stop_arg == 'false' and bash == 'false':
        input_data, refseq_data = get_dir(input_dir, refseq_dir)

        port_range = get_port_range(port, secure)

        docker_pull()

        docker_analysis(input_data, refseq_data, port_range, basecalling_tools, secure)

        docker_basecall(input_data, port_range, basecalling_tools,secure)


def main(argv):
    input_dir = ''
    refseq_dir= ''
    stop_arg = ''
    basecalling_tools=''
    port = ''
    secure = ''
    bash = ''
    try:
        opts, args = getopt.getopt(argv,"hi:r:s:b:p:x:a:",["help=", "inputdir=", "refseqdir=","stoparg=","basecallingtools=", "port=", "secure=", "bash="])
    except getopt.GetoptError:
        print('Please use the correct arguments.')
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-i", "--inputdir") :
            input_dir = arg
        elif opt in ("-r", "--refseqdir"):
            refseq_dir= arg
        elif opt in ("-s", "--stoparg"):
            stop_arg = arg.lower()
        elif opt in ("-b", "--basecallingtools"):
            basecalling_tools = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-x", "--secure"):
            secure = arg
        elif opt in ("-a", "--bash"):
            bash = arg


    stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure, bash = validate_args(stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure, bash)

    docker_start(stop_arg, input_dir, refseq_dir, basecalling_tools, port, secure, bash)
    docker_bash(bash)
    docker_stop(stop_arg)

if __name__ == "__main__":
   main(sys.argv[1:])
