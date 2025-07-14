from fastapi import HTTPException

async def get_or_404(coro, entity_name: str = "Entity"):
    """
    Takes a coroutine that fetches an entity.
    Raises HTTP 404 if result is None.
    """
    entity = await coro
    if entity is None:
        raise HTTPException(status_code=404, detail=f"{entity_name} not found")
    return entity
