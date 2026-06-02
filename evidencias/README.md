# Taller ORM con SQLAlchemy, PostgreSQL y MariaDB


### Evidencia

![Creación Base de Datos](evidencias/CreacionBaseDeDatos.png)

---

## Evidencias

### Facultad

![Facultad](evidencias/PoblarTablaFacultad.png)

### Carrera

![Carrera](evidencias/PoblarTablaCarrera.png)

### Profesor

![Profesor](evidencias/PoblarTablaProfesor.png)

### Recurso Académico

![Recurso](evidencias/PoblarTablaRecurso.png)

---

# PostgreSQL

Se levantaron los servicios utilizando Docker Compose.

Servicios utilizados:

- PostgreSQL
- pgAdmin

Posteriormente se configuró SQLAlchemy para conectarse a PostgreSQL y se ejecutó la creación y carga de datos.

## Evidencias

### Facultad

![Postgres Facultad](evidencias/PostgresFacultad.png)

### Carrera

![Postgres Carrera](evidencias/PostgresCarrera.png)

### Profesor

![Postgres Profesor](evidencias/PostgresProfesor.png)

### Recursos Académicos

![Postgres Recursos](evidencias/PostgresRecursos.png)

---

# MariaDB

Se configuró SQLAlchemy para conectarse a MariaDB mediante PyMySQL.

Posteriormente se ejecutó nuevamente la creación de tablas y la carga de datos utilizando los mismos scripts ORM.

La verificación se realizó mediante phpMyAdmin.

## Evidencias

### Facultad

![PHP Facultad](evidencias/PHPTablaFacultad.png)

### Carrera

![PHP Carrera](evidencias/PHPTablaCarrera.png)

### Profesor

![PHP Profesor](evidencias/PHPTablaProfesor.png)

### Recursos Académicos

![PHP Recursos](evidencias/PHPTablaRecursos.png)

### Consulta MariaDB

![MariaDB](evidencias/ConsultasMariaDB.png)

---

# Consultas ORM

## Consulta ALL

Obtiene todos los registros de la entidad Facultad.

```bash
python consulta_all.py
```

### Evidencia

![Consulta ALL](evidencias/ConsultaAll.png)

---

## Consulta FILTER

Filtra registros utilizando una condición específica.

```bash
python consulta_filter.py
```

### Evidencia

![Consulta FILTER](evidencias/ConsultaFilter.png)

---

## Consulta ORDER BY

Ordena registros utilizando un atributo determinado.

```bash
python consulta_order_by.py
```

### Evidencia

![Consulta ORDER BY](evidencias/ConsultaOrderBy.png)

---

## Consulta OR

Realiza consultas utilizando el operador lógico OR.

```bash
python consulta_or.py
```

### Evidencia

![Consulta OR](evidencias/ConsultaOR.png)

---

## Consulta AND

Realiza consultas utilizando el operador lógico AND.

```bash
python consulta_and.py
```

### Evidencia

![Consulta AND](evidencias/ConsultaAnd.png)

---

## Consulta Nueva

Presenta los recursos académicos de una facultad específica.

```bash
python consulta_nueva.py
```

### Evidencia

![Consulta Nueva](evidencias/ConsultaNueva.png)

---

# Ejecución del Proyecto

## Crear las tablas

```bash
python crear_base_entidades.py
```

## Poblar las tablas

```bash
python poblar_base1.py
python poblar_base2.py
python poblar_base3.py
python poblar_base4.py
```

## Ejecutar consultas

```bash
python consulta_all.py
python consulta_filter.py
python consulta_order_by.py
python consulta_or.py
python consulta_and.py
python consulta_nueva.py
```

---
