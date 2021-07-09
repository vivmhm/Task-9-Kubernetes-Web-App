#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")

cmd = cmd.lower()
chklstr = cmd.split()
chkstr = [ "build","generate","deploy","can","you","get","a","pods","for","me","please","normal","pod", 
"show","the","again","create","with","deployment","deployments","normal","one","scale","list","destroy",
"scale up","scale down","decrease","increase","is","which","whose","has","can","could","more","remove",
"delete","detach","name","everything","test2","again","in","test","describe","k8s","kubernetes","services",
"svc","replica","expose","launch" ]

for i in range(0,len(chklstr)):
	if chklstr[i] in chkstr:
		chklstr[i] = ""
chksstr = " ".join(chklstr)
chksstr = chksstr.split()

if ("create" in chksstr or "deploy" in chksstr or "launch" in chksstr or "make" in chksstr) and len(chksstr)<4:
	command = "kubectl create deployment " + chksstr[1] + " --image=httpd --kubeconfig /usr/share/httpd/admin.conf"

elif ("create" in chksstr or "deploy" in chksstr or "launch" in chksstr) and (len(chksstr)<5 and "id" in chksstr):
	command = "kubectl create deployment " + chksstr[1] + " --image=" + chksstr[3] + " --kubeconfig /usr/share/httpd/admin.conf"

elif ("get" in chksstr or "show" in chksstr) and len(chksstr)<2:
	command = "kubectl get pods --kubeconfig /usr/share/httpd/admin.conf"

elif "describe" in chksstr:
	command = "kubectl describe pods --kubeconfig /usr/share/httpd/admin.conf"

elif "expose" in chksstr:
	command = "kubectl expose deployment " + chksstr[1] + " --type='NodePort' --port " + chksstr[2] + " --kubeconfig /usr/share/httpd/admin.conf"

elif "cluster" in chksstr or "cluster's" in chksstr or "cluster-info" in chksstr or "info" in chksstr or "details" in chksstr:
	command = "kubectl cluster-info --kubeconfig /usr/share/httpd/admin.conf"

elif ("replicas" in chksstr or "replica" in chksstr or "copies" in chksstr or "copy" in chksstr) and len(chksstr)>3:
	command = "kubectl scale deployment " + chksstr[3] + " --replicas=" + chksstr[1] + " --kubeconfig /usr/share/httpd/admin.conf"

elif "scale" in chksstr:
	command = "kubectl scale deployment " + chksstr[1] + " --replicas=" + chksstr[2] + " --kubeconfig /usr/share/httpd/admin.conf"

elif "delete" in chksstr and ("svc" in chksstr or "service" in chksstr):
	command = "kubectl delete svc " + chksstr[2] + " --kubeconfig /usr/share/httpd/admin.conf"

elif "delete" in chksstr or "remove" in chksstr:
	command = "kubectl delete pod " + chksstr[1] + " --kubeconfig /usr/share/httpd/admin.conf"

elif "service" in chksstr or "svc" in chksstr or "services" in chksstr:
	command = "kubectl get svc --kubeconfig /usr/share/httpd/admin.conf"

else:
        print("Please check not a correct command")
		
o = subprocess.getoutput(command)
print(o)

