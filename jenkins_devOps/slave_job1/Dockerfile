FROM registry.redhat.io/ubi8/ubi:latest

LABEL jenkins=slave
LABEL config=docker
LABEL app=linux

ENV DOCKER_HOST=192.168.99.107:4243

RUN echo -e "[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n[appstream]\nbaseurl=http://mirror.centos.org/centos-8/8/AppStream/x86_64/os/\ngpgcheck=0\n[baseos]\nbaseurl=http://mirror.centos.org/centos-8/8/BaseOS/x86_64/os/\ngpgcheck=0" >> /etc/yum.repos.d/docker.repo && \
yum install -y  docker-ce --nobest && \
yum install openssh-server -y && \
rm -rf /var/run/sshd && \
mkdir /var/run/sshd && \
echo 'root:redhat' | chpasswd && \
rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
sed -i "s/UsePAM.*/UsePAM yes/g" /etc/ssh/sshd_config && \
ssh-keygen -A

RUN yum install -y java-11-openjdk.x86_64

EXPOSE 22
RUN echo 'export DOCKER_HOST=192.168.99.107:4243' >> /etc/bashrc && \
export DOCKER_HOST=192.168.99.107:4243

CMD /usr/sbin/sshd -D 
