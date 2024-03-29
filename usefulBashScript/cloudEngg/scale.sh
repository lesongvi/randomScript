#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <cluster-name> <number-of-nodes>"
  exit 1
fi

declare -A CLUSTER_MAP
CLUSTER_MAP=(
    [v]="vicluster"
    [v1]="vicluster1"
)

CLUSTERNAME="${CLUSTER_MAP[$1]:-$1}"
NUMBEROFNODE="${2:-1}"

echo eksctl scale nodegroup --cluster $CLUSTERNAME --name $CLUSTERNAME-eks-nodes --nodes $NUMBEROFNODE --nodes-min $NUMBEROFNODE --nodes-max $NUMBEROFNODE

eksctl scale nodegroup --cluster $CLUSTERNAME --name $CLUSTERNAME-eks-nodes --nodes $NUMBEROFNODE --nodes-min $NUMBEROFNODE --nodes-max $NUMBEROFNODE
