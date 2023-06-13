# autozone_assessment

python web app using Flask framework that can be deployed to minikube running on qemu or any other VM on local machine
Running on Localhost:8080

Used VScode, python 3.11, Flask and generated self-signed ssl certificate(saved in certs folder)

$Minikube start vm-driver = qemu
$Minikube status
(minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured)

Once minikube is up and running:

$Git clone https://github.com/sreemkosuru/autozone_assessment.git

Apply k8s manifests:
$kubectl apply -f deployment.yaml
$kubectl apply -f service.yaml
$kubectl apply -f persistentvolumeclaim.yaml
