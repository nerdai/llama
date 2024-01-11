"""Index registry."""

from typing import Dict, Type

from llama.core.data_structs.struct_type import IndexStructType
from llama.core.indices.base import BaseIndex
from llama.core.indices.document_summary.base import DocumentSummaryIndex
from llama.core.indices.empty.base import EmptyIndex
from llama.core.indices.keyword_table.base import KeywordTableIndex
from llama.core.indices.knowledge_graph.base import KnowledgeGraphIndex
from llama.core.indices.list.base import SummaryIndex
from llama.core.indices.multi_modal import MultiModalVectorStoreIndex
from llama.core.indices.struct_store.pandas import PandasIndex
from llama.core.indices.struct_store.sql import SQLStructStoreIndex
from llama.core.indices.tree.base import TreeIndex
from llama.core.indices.vector_store.base import VectorStoreIndex

INDEX_STRUCT_TYPE_TO_INDEX_CLASS: Dict[IndexStructType, Type[BaseIndex]] = {
    IndexStructType.TREE: TreeIndex,
    IndexStructType.LIST: SummaryIndex,
    IndexStructType.KEYWORD_TABLE: KeywordTableIndex,
    IndexStructType.VECTOR_STORE: VectorStoreIndex,
    IndexStructType.SQL: SQLStructStoreIndex,
    IndexStructType.PANDAS: PandasIndex,
    IndexStructType.KG: KnowledgeGraphIndex,
    IndexStructType.EMPTY: EmptyIndex,
    IndexStructType.DOCUMENT_SUMMARY: DocumentSummaryIndex,
    IndexStructType.MULTIMODAL_VECTOR_STORE: MultiModalVectorStoreIndex,
}
