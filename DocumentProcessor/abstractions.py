from abc import ABC, abstractmethod
from typing import  List, Protocol
from dtypes import Document, DocumentType,ExtractedContent, Chunk,

class DocumentRepository(Protocol):
    """Interface for fetching documents from your database"""
    async def get_by_ids(self, ids: List[int]) -> List[Document]:
        """Fetch documents by their IDs"""
        pass

    async def get_by_type(self, doc_type: DocumentType) -> List[Document]:
        """Fetch all documents of a specific type"""
        pass


class ContentExtractor(ABC):
    """Base class for extracting content from different document types"""

    @abstractmethod
    async def extract(self, document: Document) -> ExtractedContent:
        """Extract text content from a document"""
        pass

    @abstractmethod
    def supports(self, doc_type: DocumentType) -> bool:
        """Check if this extractor supports the document type"""
        pass


class TextChunker(ABC):
    """Base class for chunking strategies"""

    @abstractmethod
    def chunk(self, content: ExtractedContent, chunk_size: int = 512) -> List[Chunk]:
        """Split content into chunks"""
        pass


class Embedder(ABC):
    """Base class for generating embeddings"""
    
    @abstractmethod
    async def embed(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts"""
        pass


class ChunkRepository(Protocol):
    """Interface for storing chunks in your database"""
    
    async def save_chunks(self, chunks: List[Chunk]) -> None:
        """Save chunks to PostgreSQL"""
        pass


class VectorRepository(Protocol):
    """Interface for storing vectors in Qdrant/Elastic"""
    
    async def save_vectors(self, chunks: List[Chunk]) -> None:
        """Save chunk embeddings to vector store"""
        pass
