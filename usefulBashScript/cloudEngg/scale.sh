!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <cluster-name> <number-of-nodes>"
  exit 1
fi

declare -A CLUSTER_MAP
CLUSTER_MAP=(
    [g]="genaihvnapp"
    [g1]="genaihvnapp1"
)

CLUSTERNAME="${CLUSTER_MAP[$1]:-$1}"
NUMBEROFNODE="${2:-1}"

userAnswer=""

if (( NUMBEROFNODE > 1 )); then
  while [[ "$userAnswer" != "yes" && "$userAnswer" != "no" ]];
  do
    echo "You are attempting to scale 3 nodes for the cluster $CLUSTERNAME, are you sure? (yes/no)"
    read userAnswer
  done
fi

if [ "$userAnswer" == "no" ]; then
  echo "User chose to not continue scaling ;)"
  exit
else
  echo "I hope you know what you are doing"
fi


echo eksctl scale nodegroup --cluster $CLUSTERNAME --name $CLUSTERNAME-eks-nodes --nodes $NUMBEROFNODE --nodes-min $NUMBEROFNODE --nodes-max $NUMBEROFNODE

eksctl scale nodegroup --cluster $CLUSTERNAME --name $CLUSTERNAME-eks-nodes --nodes $NUMBEROFNODE --nodes-min $NUMBEROFNODE --nodes-max $NUMBEROFNODE
