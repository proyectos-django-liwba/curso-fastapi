
from typing import Generic, List, TypeVar
from pydantic import BaseModel, conint

 
 # Parameters for pagination
class PageParams(BaseModel):
    page: conint(ge=1) = 1
    size: conint(ge=1, le=100) = 10
 
 # Generic type for the response schema
T = TypeVar("T")
 

 # Response schema for any paged API
class PagedResponseSchema(BaseModel, Generic[T]):
    total: int
    page: int
    size: int
    results: List[T]
 
 # Method Paginate the query
def paginate(page_params: PageParams, query, ResponseSchema: BaseModel) -> PagedResponseSchema[T]:
    """Paginate the query."""
 
    paginated_query = query.offset((page_params.page - 1) * page_params.size).limit(page_params.size).all()
 
    return PagedResponseSchema(
        total=query.count(),
        page=page_params.page,
        size=page_params.size,
        #results=[ResponseSchema.from_orm(item) for item in paginated_query],
        results=[ResponseSchema.from_orm(item) for item in paginated_query],
    )