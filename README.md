# ML-Census-Model-Deployment-with-GKE

1. Using the Cloud Shell or AI Notebook terminal, you can run the following command lines to build and push the final image to GCR:\
   $ cd ml-census\
   $ docker build -t gcr.io/{project_id}/model_deployment .\
   $ docker push gcr.io/{project_id}/model_deployment
2. Cope files in the configuration directory and paste them into your gcs bucket.
3. In model_deployment.yaml, modify config.yaml with appropriate paths to the configuration files.
4. Also, change gcr.io/dsstream-sandbox/model_deployment:latest to gcr.io/{project_id}/model_deployment:latest
5. Create and attach a GKE cluster to your project:\
   $ gcloud config set project anh-sandbox
   $ gcloud container clusters create census-ai --cluster-version 1.18.17-gke.1901\ <br />
     --machine-type n1-standard-1 --num-nodes 1 --issue-client-certificate --enable-basic-auth --zone {zone_name} <br />
   $ cloud container clusters get-credentials census-ai --zone {zone_name}
6. Verify if there is your cluster:\
   $ kubectl get nodes <br />
