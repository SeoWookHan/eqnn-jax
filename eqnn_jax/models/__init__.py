"""Static model exports for IDE-friendly autocomplete."""

import sys
import models.utils
import models.utils.graph_utils
import models.utils.equivariant_graph_utils
import models.utils.irreps_utils
from models import diffpool, egnn, gnn, mlp, nequip, pointnet, segnn, transformer

# Register submodules under eqnn_jax.models.* so that
# `from eqnn_jax.models.pointnet import X` works at runtime.
_submodules = {
    "diffpool": diffpool,
    "egnn": egnn,
    "gnn": gnn,
    "mlp": mlp,
    "nequip": nequip,
    "pointnet": pointnet,
    "segnn": segnn,
    "transformer": transformer,
    "utils": models.utils,
    "utils.graph_utils": models.utils.graph_utils,
    "utils.equivariant_graph_utils": models.utils.equivariant_graph_utils,
    "utils.irreps_utils": models.utils.irreps_utils,
}
for _name, _mod in _submodules.items():
    sys.modules.setdefault(f"eqnn_jax.models.{_name}", _mod)

__all__ = [
    "diffpool",
    "egnn",
    "gnn",
    "mlp",
    "nequip",
    "pointnet",
    "segnn",
    "transformer",
    "utils",
]
