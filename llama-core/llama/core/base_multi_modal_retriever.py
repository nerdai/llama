"""base multi modal retriever."""
from abc import abstractmethod
from typing import List

from llama.core.base_retriever import BaseRetriever
from llama.core.image_retriever import BaseImageRetriever
from llama.core.indices.query.schema import QueryType
from llama.core.schema import NodeWithScore


class MultiModalRetriever(BaseRetriever, BaseImageRetriever):
    """Multi Modal base retriever."""

    @abstractmethod
    def text_retrieve(self, str_or_query_bundle: QueryType) -> List[NodeWithScore]:
        """Retrieve text nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    def text_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Retrieve image nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    def image_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Retrieve image nodes given image query.

        Implemented by the user.

        """

    @abstractmethod
    async def atext_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Async Retrieve text nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    async def atext_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Async Retrieve image nodes given text query.

        Implemented by the user.

        """

    @abstractmethod
    async def aimage_to_image_retrieve(
        self, str_or_query_bundle: QueryType
    ) -> List[NodeWithScore]:
        """Async Retrieve image nodes given image query.

        Implemented by the user.

        """
