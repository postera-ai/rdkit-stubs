from _typeshed import Incomplete
from rdkit.ML.Cluster import Clusters as Clusters
from rdkit.ML.Cluster.Clustering import (
    MurtaghCluster as MurtaghCluster,
    MurtaghDistCluster as MurtaghDistCluster,
)

WARDS: int
SLINK: int
CLINK: int
UPGMA: int
MCQUITTY: int
GOWER: int
CENTROID: int
methods: Incomplete

def _LookupDist(dists, i, j, n): ...
def _ToClusters(data, nPts, ia, ib, crit, isDistData: int = ...): ...
def ClusterData(data, nPts, method, isDistData: int = ...): ...
