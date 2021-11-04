import subprocess
import warnings
import sys, getopt
import os
import re
import gzip
import pandas as pd
from os import path

docker_tools = 'samplix/samplix_analysis_tools:latest'

def print_help():
    print ('docker.py <arguments>\n')
    print('This script is used to initiate or stop the docker container\n If initiating, the newest docker will be pulled automatically.\n')
    print('-i       Input-data path\n')
    print('-r       Refseq-data path\n')
    print('-b       Set to true to load basecalling tools (e.g. activate gpus)\n')
    print('-s       Set to stop to stop the docker container. \n')
    print('-p       Optional. Choose which port to use. Default is port 8089\n')
    print('-x       Set to true to use secure port 4430\n')


def docker_container_ID(stop_arg):
    if stop_arg == 'stop':
        print('Obtaining docker Container ID')
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
                # if line_split[4] == 'status':
                #     list_up.append((line_split[0], line_split[4]))
                #     list_exited.append((line_split[0], line_split[4]))
                #     continue

                if bool(re.match('up', line_split[4])):
                    status = 'up'
                    list_up.append((line_split[0], status, line_split[4]))
                    continue
                if bool(re.match('exited', line_split[4])):
                    status = 'exited'
                    list_exited.append((line_split[0], status, line_split[4]))
                    continue

        if len(list_up) > 1 :
            print('More than one docker container is running')
            print('Which container should be stopped?')

            df = pd.DataFrame(list_up)
            df.columns = ['Container_ID', 'Status', 'Time']
            print(df)

            match = 'false'
            count = 0
            while(match == 'false'):
                if count >= len(list_up):
                    print('Please provide correct Container_ID')
                session_id = input('Container_ID: ')
                for container_id, status, time in list_up:
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
    session_id = docker_container_ID(stop_arg)

    if stop_arg == 'stop':
        print('Stopping docker container:', session_id)
        call_docker = subprocess.run(['docker', 'stop', session_id])
        print('Docker container stopped')

def docker_pull():
    print('Pulling latest docker')
    call_docker = subprocess.run(['docker', 'pull', docker_tools])

def docker_analysis(input_data, refseq_data, port_range, basecalling_tools, secure):
    if basecalling_tools == 'false':
        print('\nInitiating docker Reference and Analysis tools')
        if secure == 'false':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '-v',input_data, '-v', refseq_data, '-p', port_range, docker_tools],stdout=subprocess.PIPE)
        if secure == 'true':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '-v',input_data, '-v', refseq_data,'-e', 'SECURE=true', '-p', port_range, docker_tools],stdout=subprocess.PIPE)
        stdout, stderr = call_docker.communicate()
        docker_session=stdout.decode("utf-8").strip()[0:12]
        print('Docker container initiated:', docker_session)
        print('Port range:', port_range)
        print('Input-data:', input_data)
        print('Refseq-data:', refseq_data)

def validate_args(stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure):
    if stop_arg == '':
        stop_arg = 'start'

    if stop_arg != 'start' and stop_arg != 'stop':
        print('Invalid -s argument. Must be start or stop')
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

    return stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure

def get_dir(input_dir, refseq_dir):
    input_data = input_dir +':/input-data'
    refseq_data = refseq_dir +':/refseq-data'

    return input_data, refseq_data

def docker_basecall(input_data, port_range, basecalling_tools, secure):
    if basecalling_tools == 'true':
        print('\nInitiating docker basecalling_tools')
        if secure == 'false':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '--gpus', 'all', '-v',input_data,'-p', port_range, docker_tools],stdout=subprocess.PIPE)
        if secure == 'true':
            call_docker = subprocess.Popen(['docker', 'run', '-td', '--gpus', 'all', '-v',input_data,'-e','SECURE=true','-p', port_range, docker_tools],stdout=subprocess.PIPE)
        stdout, stderr = call_docker.communicate()
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

def docker_start(stop_arg, input_dir, refseq_dir, basecalling_tools, port, secure):
    if stop_arg == 'start':
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
    try:
        opts, args = getopt.getopt(argv,"hi:r:s:b:p:x:",["help=", "inputdir=", "refseqdir=","stoparg=","basecallingtools=", "port=", "secure="])
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


    stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure = validate_args(stop_arg, basecalling_tools, port, input_dir, refseq_dir, secure)

    docker_start(stop_arg, input_dir, refseq_dir, basecalling_tools, port, secure)
    docker_stop(stop_arg)

if __name__ == "__main__":
   main(sys.argv[1:])
