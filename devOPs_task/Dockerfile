FROM registry.redhat.io/ubi8/ubi:latest

LABEL app=web

ENV DOCROOT=/var/www/html 

RUN yum install -y httpd --nodocs && \
    yum clean all

COPY src/* $(DOCROOT)

EXPOSE 80 

RUN rm -rf /run/httpd && mkdir /run/httpd

USER root  

CMD /usr/sbin/httpd -DFOREGROUND
