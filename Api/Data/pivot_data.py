# dependencias
from sqlalchemy import Table, Column, ForeignKey, Integer
# importaciones
from Api.Data.conection import ConexionBD


# tabla intermedia o pivote
tasks_tags = Table(
    "tasks_tags",
    ConexionBD.Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)