#!/bin/bash

usage() {
  echo "Usage: $0 <cluster> <namespace> <action> [pod] [args]"
  echo "Clusters:"
  echo "  v             - vcluster"
  echo "  v1            - vcluster1"
  echo "  v2            - vcluster2"
  echo "  v3            - vcluster3"
  echo "Namespaces:"
  echo "  agd           - amazon-guardduty"
  echo "  cal           - calico-system"
  echo "  cgw           - common-gateway"
  echo "  cs            - common-service"
  echo "  def           - default"
  echo "  knl           - kube-node-lease"
  echo "  kpb           - kube-public"
  echo "  ksys          - kube-system"
  echo "  ac            - <cluster>-auth"
  echo "  auth          - <cluster>-auth"
  echo "  datastore     - <cluster>-datastore"
  echo "  service       - <cluster>-service"
  echo "  worker        - <cluster>-worker"
  echo "Actions:"
  echo "  get, g        - Get resources"
  echo "  describe, dsc - Describe resources"
  echo "  delete, del   - Delete resources"
  echo "  exec, ex      - Execute command in a pod"
  echo "  logs, lg      - Get logs from a pod"
  echo "Flags:"
  echo "  --help        - Display this help message"
}

if [[ "$1" == "--help" ]]; then
  usage
  exit 0
fi

if [ "$#" -lt 2 ]; then
  usage
  exit 1
fi

declare -A CLUSTER_MAP
CLUSTER_MAP=(
	[v]="vcluster"
	[v1]="vcluster1"
	[v2]="vcluster2"
	[v3]="vcluster3"
)

declare -A STATIC_NAMESPACE_MAP
STATIC_NAMESPACE_MAP=(
	[agd]="amazon-guardduty"
	[cal]="calico-system"
	[cgw]="common-gateway"
	[cs]="common-service"
	[def]="default"
	[knl]="kube-node-lease"
	[kpb]="kube-public"
	[ksys]="kube-system"
)

declare -A CLUSTER_SPECIFIC_NAMESPACE_MAP
CLUSTER_SPECIFIC_NAMESPACE_MAP=(
	[ac]="ac"
	[auth]="auth"
	[datastore]="datastore"
	[service]="service"
	[worker]="worker"
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

ACTION="${ACTION_MAP[$3]:-$3}"

POD=""
if [[ "$ACTION" == "get" || "$ACTION" == "describe" || "$ACTION" == "delete" ]]; then
    POD=" pod"
fi

NAMESPACE=""
if [[ -n "${STATIC_NAMESPACE_MAP[$2]}" ]]; then
    NAMESPACE="${STATIC_NAMESPACE_MAP[$2]}"
elif [[ -n "${CLUSTER_SPECIFIC_NAMESPACE_MAP[$2]}" ]]; then
	CLUSTER="${CLUSTER_MAP[$1]}"
	NAMESPACE="${CLUSTER}-${CLUSTER_SPECIFIC_NAMESPACE_MAP[$2]}"
else
	NAMESPACE="$2"
fi

echo kubectl -n "$NAMESPACE" "$ACTION"$POD ${@:4}

kubectl -n "$NAMESPACE" "$ACTION"$POD ${@:4}

exit 0
