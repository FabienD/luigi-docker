from dependency_injector import containers, providers

import docker


class Container(containers.DeclarativeContainer):
    
    docker_client = providers.Factory(
        docker.DockerClient,
        #base_url='unix://var/run/docker.sock',
        base_url='tcp://dockerproxy:2375', # Use docker proxy
    )
