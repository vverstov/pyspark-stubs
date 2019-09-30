# Stubs for pyspark.mllib.linalg.distributed (Python 3.5)
#

from typing import Any, Generic, Sequence, Optional, Tuple, TypeVar, Union
from pyspark.rdd import RDD
from pyspark.storagelevel import StorageLevel
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.linalg import Vector, Matrix, QRDecomposition
from pyspark.mllib.stat import MultivariateStatisticalSummary
from numpy import ndarray  # type: ignore

VectorLike = Union[Vector, Sequence[Union[float, int]]]

UT = TypeVar("UT")
VT = TypeVar("VT")

class DistributedMatrix:
    def numRows(self) -> int: ...
    def numCols(self) -> int: ...

class RowMatrix(DistributedMatrix):
    def __init__(self, rows: RDD[Vector], numRows: int = ..., numCols: int = ...) -> None: ...
    @property
    def rows(self) -> RDD[Vector]: ...
    def numRows(self) -> int: ...
    def numCols(self) -> int: ...
    def computeColumnSummaryStatistics(self) -> MultivariateStatisticalSummary: ...
    def computeCovariance(self) -> Matrix: ...
    def computeGramianMatrix(self) -> Matrix: ...
    def columnSimilarities(self, threshold: float = ...) -> CoordinateMatrix: ...
    def tallSkinnyQR(self, computeQ: bool = ...) -> QRDecomposition[RowMatrix, Matrix]: ...
    def computeSVD(self, k: int, computeU: bool = ..., rCond: float = ...) -> SingularValueDecomposition[RowMatrix, Matrix]: ...
    def computePrincipalComponents(self, k: int) -> Matrix: ...
    def multiply(self, matrix: Matrix) -> RowMatrix: ...

class SingularValueDecomposition(JavaModelWrapper, Generic[UT, VT]):
    @property
    def U(self) -> Optional[UT]: ...
    @property
    def s(self) -> Vector: ...
    @property
    def V(self) -> VT: ...

class IndexedRow:
    index: int
    vector: VectorLike
    def __init__(self, index: int, vector: VectorLike) -> None: ...

class IndexedRowMatrix(DistributedMatrix):
    def __init__(self, rows: RDD[Union[Tuple[int, VectorLike], IndexedRow]], numRows: int = ..., numCols: int = ...) -> None: ...
    @property
    def rows(self) -> RDD[IndexedRow]: ...
    def numRows(self) -> int: ...
    def numCols(self) -> int: ...
    def columnSimilarities(self) -> CoordinateMatrix: ...
    def computeGramianMatrix(self) -> Matrix: ...
    def toRowMatrix(self) -> RowMatrix: ...
    def toCoordinateMatrix(self) -> CoordinateMatrix: ...
    def toBlockMatrix(self, rowsPerBlock: int = ..., colsPerBlock: int = ...) -> BlockMatrix: ...
    def computeSVD(self, k: int, computeU: bool = ..., rCond: float = ...) -> SingularValueDecomposition[IndexedRowMatrix, Matrix]: ...
    def multiply(self, matrix: Matrix) -> IndexedRowMatrix: ...

class MatrixEntry:
    i: int
    j: int
    value: float
    def __init__(self, i: int, j: int, value: float) -> None: ...

class CoordinateMatrix(DistributedMatrix):
    def __init__(self, entries: RDD[Union[Tuple[int, int, float], MatrixEntry]], numRows: int = ..., numCols: int = ...) -> None: ...
    @property
    def entries(self) -> RDD[MatrixEntry]: ...
    def numRows(self) -> int: ...
    def numCols(self) -> int: ...
    def transpose(self) -> 'CoordinateMatrix': ...
    def toRowMatrix(self) -> RowMatrix: ...
    def toIndexedRowMatrix(self) -> IndexedRowMatrix: ...
    def toBlockMatrix(self, rowsPerBlock: int = ..., colsPerBlock: int = ...) -> BlockMatrix: ...

class BlockMatrix(DistributedMatrix):
    def __init__(self, blocks: RDD[Tuple[Tuple[int, int], MatrixEntry]], rowsPerBlock: int, colsPerBlock: int, numRows: int = ..., numCols: int = ...) -> None: ...
    @property
    def blocks(self) -> RDD[Tuple[Tuple[int, int], Matrix]]: ...
    @property
    def rowsPerBlock(self) -> int: ...
    @property
    def colsPerBlock(self) -> int: ...
    @property
    def numRowBlocks(self) -> int: ...
    @property
    def numColBlocks(self) -> int: ...
    def numRows(self) -> int: ...
    def numCols(self) -> int: ...
    def cache(self) -> 'BlockMatrix': ...
    def persist(self, storageLevel: StorageLevel) -> 'BlockMatrix': ...
    def validate(self) -> None: ...
    def add(self, other: 'BlockMatrix') -> 'BlockMatrix': ...
    def subtract(self, other: 'BlockMatrix') -> 'BlockMatrix': ...
    def multiply(self, other: 'BlockMatrix') -> 'BlockMatrix': ...
    def transpose(self) -> 'BlockMatrix': ...
    def toLocalMatrix(self) -> Matrix: ...
    def toIndexedRowMatrix(self) -> IndexedRowMatrix: ...
    def toCoordinateMatrix(self) -> CoordinateMatrix: ...
