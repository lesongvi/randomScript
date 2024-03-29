#!/bin/bash

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <namespace> <pod-name> [<resource-name>]"
  exit 1
fi

declare -A NAMESPACE_MAP
NAMESPACE_MAP=(
    [vs]="vcluster-service"
    [va]="vcluster-auth"
    [v1s]="vcluster1-service"
    [v1a]="vcluster1-auth"
)

declare -A PODNAME_MAP
PODNAME_MAP=(
    [u]="ui"
    [a]="api"
    [w]="worker"
)


NAMESPACE="${NAMESPACE_MAP[$1]:-$1}"
POD_NAME="${PODNAME_MAP[$2]:-$2}"
RESOURCENAME="${3:-deployments}"

echo kubectl -n "$NAMESPACE" edit "$RESOURCENAME" "$POD_NAME"

kubectl -n "$NAMESPACE" edit "$RESOURCENAME" "$POD_NAME"
