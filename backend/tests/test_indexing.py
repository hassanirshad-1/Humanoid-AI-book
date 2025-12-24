import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from app.services.indexing_service import parse_mdx_content

def test_parse_mdx_content_structure():
    """Test that parse_mdx_content correctly splits markdown and extracts metadata."""
    mock_mdx = """---
title: Lesson 1
---

# Heading 1
Some content here.

## Heading 2
More content here.
"""
    # Mock settings and file operations
    with patch("app.services.indexing_service.settings") as mock_settings:
        mock_settings.MDX_DOCS_PATH = Path("/mock/docs")
        
        file_path = Path("/mock/docs/chapter-01-intro/lesson1.mdx")
        
        with patch("builtins.open", mock_open(read_data=mock_mdx)):
            # We also need to mock relative_to
            with patch.object(Path, "relative_to", return_value=Path("chapter-01-intro/lesson1.mdx")):
                chunks = parse_mdx_content(file_path)
    
    assert len(chunks) > 0
    # Check if metadata is populated
    metadata = chunks[0]["metadata"]
    assert metadata["chapter"] == "chapter-01-intro"
    assert metadata["lesson"] == "lesson1"
    assert "header1" in metadata or "header2" in metadata or metadata["heading_path"] != ""
