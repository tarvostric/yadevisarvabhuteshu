import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigs
from findiff import FinDiff

x = np.linspace(-8, 8, 201)
energies, states = eigs(
    -0.5 * (FinDiff(0, x[1] - x[0], 2) + FinDiff(1, x[1] - x[0], 2)).matrix(V.shape)
    + diags(V.reshape(-1)),
    k=20,
    which="SR",
)
