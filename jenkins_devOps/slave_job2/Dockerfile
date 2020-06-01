FROM registry.redhat.io/ubi8/ubi:latest

## Installing Kubectl utility

RUN  echo -e '[kubernetes]\nname=Kubernetes\nbaseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg' >> /etc/yum.repos.d/kubernetes.repo && \
yum install -y kubectl

## Installing Openssh-server softwares

RUN echo -e "[appstream]\nbaseurl=http://mirror.centos.org/centos-8/8/AppStream/x86_64/os/\ngpgcheck=0\n[baseos]\nbaseurl=http://mirror.centos.org/centos-8/8/BaseOS/x86_64/os/\ngpgcheck=0" >> /etc/yum.repos.d/dvd.repo && \
yum install -y openssh-server && useradd jenkins && \
rm -rf /var/run/sshd && \
mkdir /var/run/sshd && \
echo 'root:redhat' | chpasswd && \
rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
sed -i "s/UsePAM.*/UsePAM yes/g" /etc/ssh/sshd_config && \
ssh-keygen -A && \
echo 'export DOCKER_HOST=192.168.99.107:4243' >> /etc/bashrc && \
export DOCKER_HOST=192.168.99.107:4243

EXPOSE 22

COPY config/*  /

RUN yum install -y java-11-openjdk.x86_64

CMD ["/usr/sbin/sshd", "-D"]
