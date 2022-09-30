#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Head node operator.
"""

import logging

from ops.main import main

from hpctinterfaces.relation import interface_registry
from hpctops.charm.node import NodeCharm


logger = logging.getLogger(__name__)


class HpctSlurmNodeCharm(NodeCharm):
    """Operator for cluster Slurm node."""

    def __init__(self, *args):
        super().__init__(*args)

        self.interfaces = {
            "ldap-client-ready": interface_registry.load(
                "relation-subordinate-ready", self, "ldap-client-ready"
            ),
            "slurm-client-ready": interface_registry.load(
                "relation-subordinate-ready", self, "slurm-client-ready"
            ),
            "slurm-server-ready": interface_registry.load(
                "relation-subordinate-ready", self, "slurm-server-ready"
            ),
        }

        self.setup_subordinate_relations_and_syncs(
            ["ldap-client-ready", "slurm-client-ready", "slurm-server-ready"]
        )


if __name__ == "__main__":
    main(HpctSlurmNodeCharm)
