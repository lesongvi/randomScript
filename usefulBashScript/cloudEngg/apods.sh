#!/bin/bash

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <namespace> <action> [pod] [args]"
  exit 1
fi

declare -A NAMESPACE_MAP
NAMESPACE_MAP=(
    [vs]="vcluster-service"
    [va]="vcluster-auth"
    [v1s]="vcluster1-service"
    [v1a]="vcluster1-auth"
)

declare -A ACTION_MAP
ACTION_MAP=(
	[get]="get"
	[g]="get"
	[describe]="describe"
	[dsc]="describe"
	[delete]="delete"
	[del]="delete"
	[exec]="exec"
	[ex]="exec"
	[logs]="logs"
	[lg]="logs"
)

ACTION="${ACTION_MAP[$2]:-$2}"

POD=""
if [[ "$ACTION" == "get" || "$ACTION" == "describe" || "$ACTION" == "delete" ]]; then
    POD=" pod"
fi

NAMESPACE="${NAMESPACE_MAP[$1]:-$1}"

echo kubectl -n "$NAMESPACE" "$ACTION"$POD ${@:3}

kubectl -n "$NAMESPACE" "$ACTION"$POD ${@:3}

exit 0
