# Installing Istio on GKE Clster 

Create GKE Cluster in Zone

```bash
  gcloud container clusters create app-cluster --zone europe-west2-a --disk-type=pd-standard
```

> Note: `--zone europe-west2-a` define your own zone europe-west2-a is London. `---disk-type=pd-standard` disk is standard instead off SSD

Get k8s cluster credentials 

```bash
  gcloud container clusters get-credentials app-cluster --zone europe-west2-a --project tickerkart
```

Installing istio

```bash
  curl -L https://istio.io/downloadIstio | sh -
  ls -ltra
  cd istio-1.19.0/
  export PATH=$PWD/bin:$PATH
  istioctl install --set profile=default -y
  istioctl verify-install
```
