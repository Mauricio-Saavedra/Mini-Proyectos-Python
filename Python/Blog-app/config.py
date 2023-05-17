POSTGRESQL = "postgresql+psycopg2://postgres:1234567@localhost:5432/postgres"
#Dónde todo es->"ConexiónConLibreria :// usuario:contraseña @servidor:puerto / nombre_del_archivo"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    #Base de datos:
    SQLALCHEMY_DATABASE_URI = POSTGRESQL

    #CKEditor
    CKEDITOR_PKG_TYPE = 'full'