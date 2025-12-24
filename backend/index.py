import asyncio
import os
import uvicorn
from app.services.indexing_service import create_qdrant_collection, index_all_mdx_content
from main import app as main_app # Import the FastAPI app

async def start_indexing():
    print("Starting Qdrant collection creation...")
    create_qdrant_collection()
    print("Starting MDX content indexing...")
    index_all_mdx_content()
    print("Indexing process completed.")

if __name__ == "__main__":
    # Ensure environment variables are loaded if running directly
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
    
    # Run the indexing process
    asyncio.run(start_indexing())

    # Optionally, you can also start the FastAPI app for testing purposes
    # uvicorn.run(main_app, host="0.0.0.0", port=8000)
