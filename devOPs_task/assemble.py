from os import path
import os

#if path.exists("./src/index.html"):
#  name="webserver"
#else:
#  name="unknown"

if path.exists("Dockerfile"): 
  r = os.popen("cat Dockerfile | grep name").readlines()[0].strip('\n').split(' ')[1].split('=')
  n, v = r[0], r[1]
  status = os.system('docker build -t kritik15/devops_{}:{} .'.format(n,v))
  if status:
    print("Some error in the dockerfile") 
  else: 

   print("OK\nPushing the image to the repository") 
   push_status = os.system("docker push kritik15/devops_{}:{}".format(n,v))
   if push_status:
      print("Some error occured in pushing the image, check the network connectivity or check the login status")
   else:
      print("Successfully pushed the image")
else:
  d = os.popen('docker images --filter "label=builder" ').readlines()
  if len(d) == int(1):
    print("Builder Image is not avaiable")
  else:
    inter = d[1].split('              ')
    i_name, i_version = inter[0], inter[1]
    content = "FROM {0}:{1}\nLABEL {}={}".format(i_name,i_version,'app','web')
    with open('Dockerfile') as docker_file:
      docker_file.write(content)
    docker_file.close()
    status = os.system('docker build -t kritik15/devops_{}:{}'.format(i_name,i_version))
    if status:
      print("Some error in the builder image")
    else:
      print("OK\nPushing the image to the repository")
      push_status = os.system("docker push kritik15/devops_{}:{}".format(i_name,i_version))
   if push_status:
      print("Some error occured in pushing the image, check the network connectivity or check the login status")
   else:
      print("Successfully pushed the image")
