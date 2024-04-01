#!/bin/bash

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <namespace>"
  exit 1
fi

declare -A NAMESPACE_MAP
NAMESPACE_MAP=(
    [vs]="vcluster-service"
    [va]="vcluster-auth"
    [v1s]="vcluster1-service"
    [v1a]="vcluster1-auth"
)

NAMESPACE="${NAMESPACE_MAP[$1]:-$1}"

echo kubectl -n "$NAMESPACE" get pods ${@:2}

kubectl -n "$NAMESPACE" get pods ${@:2}

exit 0
