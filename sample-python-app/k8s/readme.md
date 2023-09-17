kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f istio-ilb-gateway.yaml


Test Your Setup:

At this point, your service should be accessible through the Istio ILB Gateway. To test this, get the IP address of your ILB Gateway and send a GET request to your service:


kubectl get svc istio-ingressgateway -n istio-system

Use the IP address obtained from the above command to construct the URL for your service. For example:



curl http://<ILB-IP-ADDRESS>/get
