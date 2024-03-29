#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <cluster-name>"
  exit 1
fi

declare -A CLUSTER_MAP
CLUSTER_MAP=(
    [v]="vicluster"
    [v1]="vicluster1"
)

CLUSTERNAME="${CLUSTER_MAP[$1]:-$1}"

echo aws eks --region ap-northeast-1 update-kubeconfig --name $CLUSTERNAME

aws eks --region ap-northeast-1 update-kubeconfig --name $CLUSTERNAME
