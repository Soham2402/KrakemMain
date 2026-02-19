from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Protocol


class DocumentType(Enum):
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    MD = "md"


@dataclass
class Document:
    """Represents a document from your database"""
    id: int
    doc_type: DocumentType
    file_path: str  # or S3 URL, or blob storage reference
    metadata: Dict  # any extra metadata you want to preserve


@dataclass
class ExtractedContent:
    """Raw extracted content from a document"""
    document_id: int
    text: str
    metadata: Dict  # page numbers, sections, etc.


@dataclass
class Chunk:
    """A chunk of text with metadata"""
    document_id: int
    text: str
    chunk_index: int
    metadata: Dict
    embedding: Optional[List[float]] = None

