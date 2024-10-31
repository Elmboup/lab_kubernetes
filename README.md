# Kubernetes Lab Deployment

## Prerequisites
- Kubernetes cluster (e.g., minikube, GKE, etc.)
- kubectl configured

## Steps to Deploy

1. Build and push the Docker image:
```bash
   docker build -t my-flask-app:latest .
   docker push ehmboup/my-flask-app:latest
```

2. Apply Kubernetes manifests:
```sh
    kubectl apply -f k8s/backend-deployment.yaml
    kubectl apply -f k8s/backend-service.yaml
    kubectl apply -f k8s/database-deployment.yaml
    kubectl apply -f k8s/database-service.yaml
```

3. Apply NetworkPolicy:
If using minikube, run 
```sh 
kubectl apply -f network-policy.yaml
 ```

4. Verify deployments:
```sh
    kubectl get deployments
    kubectl get services
```
5. Access the application:
If using minikube, run 
```sh 
minikube service backend-service
 ```

## Nota : 
- Le service backend-service est configuré en tant que NodePort, avec le port 30000 exposé. Cependant, si http://<ip>:30000 ne fonctionne pas,faite un port forwarding:
```sh
kubectl port-forward svc/backend-service 30000:80
```
