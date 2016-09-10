# docker exec -it my_container bash

FROM    phusion/baseimage

        # pre-req: generate ssh keys without password
        # enable ssh and copy public key to the container
RUN     rm -f /etc/service/sshd/down \
    &&  /etc/my_init.d/00_regen_ssh_host_keys.sh
COPY    ./dock.pub /tmp/dock.pub
RUN     cat /tmp/dock.pub >> /root/.ssh/authorized_keys \
    &&  rm -f /tmp/dock.pub


        # update system
RUN     apt-get update -qq \

        # install python3
    &&  apt-get install -y --no-install-recommends \
        nano tree curl git man wget \
        python3 python3-dev python3-pip python3-setuptools \
        python3-psycopg2  # postgresql

        # app packages
COPY    ./requirements.txt /tmp/requirements.txt
RUN     pip3 install -r /tmp/requirements.txt  \

        # Clean up APT when done.
    &&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
