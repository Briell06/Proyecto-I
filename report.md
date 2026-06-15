# IMPORTANTE: Si quiere ver el proyecto sin tener que instalar dependencias y con datos de prueba para que no tenga que insertarlos manualmente, puede visitar la página online accediendo a [https://briell.pythonanywhere.com/](https://briell.pythonanywhere.com/), allí puede también editar, leer crear y borrar eventos y recursos para probar el sistema, aunque tenga en cuenta que es un sistema de prueba y cualquier cambio que haga allí no afectará su instalación local, ya que son bases de datos completamente independientes, así que no se preocupe por romper nada, si quiere probar el sistema sin instalarlo, simplemente visite el enlace y disfrute de la experiencia

# Sistema de Gestión de Aeropuerto

Sistema Django para la coordinación de operaciones de vuelo, asignación de recursos y programación de personal.
Implementa detección automática de conflictos, validación de restricciones operacionales y reglas de negocio
aeroportuarias.

## Introducción

El transporte aéreo moderno exige una sincronización milimétrica de recursos logísticos, humanos y de infraestructura. La gestión de un aeropuerto implica coordinar variables dinámicas en tiempo real, donde un retraso en una pista o la asignación incorrecta de una puerta de embarque puede desencadenar un efecto dominó con pérdidas económicas millonarias y riesgos para la seguridad operacional.

Este proyecto surge como respuesta a la necesidad de automatizar y optimizar la toma de decisiones en la programación de vuelos. El "Sistema de Gestión de Aeropuerto" ha sido desarrollado para actuar como un núcleo de validación inteligente, asegurando que cada operación cumpla estrictamente con las normativas internacionales, los tiempos de descanso y mantenimiento, y la compatibilidad física de los recursos disponibles.

### Justificación de la Arquitectura

La elección de un enfoque monolítico basado en Django se justifica por la alta cohesión de las reglas de negocio y la necesidad de transacciones atómicas. En un dominio donde la consistencia de los datos es crítica (por ejemplo, evitar que dos vuelos reserven la misma pista al mismo tiempo), el uso de un Object-Relational Mapper (ORM) robusto como el de Django garantiza el aislamiento de las transacciones y previene condiciones de carrera (_race conditions_). Además, el patrón Modelo-Vista-Plantilla (MVT) agiliza el acoplamiento de la interfaz de usuario con la lógica del backend, permitiendo una iteración rápida sin la sobrecarga arquitectónica de una API desacoplada en fases tempranas del desarrollo.

## Características

- **Gestión de pistas, puertas, aeronaves y personal**
- **Programación de vuelos con validación automática de conflictos**
- **Sistema de restricciones de recursos** (Co-requisitos y Exclusión Mutua)
- **Búsqueda inteligente de horarios disponibles**
- **Ventana de mantenimiento de 24 horas para aeronaves**
- **Requisitos dinámicos de copilotos según duración del vuelo**
- **Prevención de reservas dobles de recursos**
- **Búsqueda y filtrado de vuelos y recursos**

## Tecnologías

- Django 5.2.7: Esta fue la decisión mas importante, ya que me permitió desarrollar el proyecto de manera rápida y eficiente, gracias a su potente ORM, sistema de plantillas y facilidad para gestionar relaciones entre modelos. La escogí por su robustez, comunidad activa (StackOverflow) y mi experiencia previa con el framework, lo que me permitió enfocarme más en la lógica de negocio y menos en la configuración y detalles técnicos.
- Tailwindcss: Esta es la librería de CSS que utilicé para el diseño de la interfaz, me gusta mucho porque es muy fácil de usar y ya tengo mucha experiencia debido a proyectos de react y Angular en los que he utilizado tailwind y me permitió crear una interfaz moderna y responsive sin tener que escribir mucho código CSS puro, sino que con solo agregar clases sencillas a los elementos html ya tenía lo que necesitaba, no pude instalarlo como dependencia ya que era un poco tedioso de hacer en django, ya que no tiene soporte oficial, sino que la comunidad ha creado sus propios paquetes para hacerlo, por lo que simplemente lo añadí como CDN al home.html que es el documento html raíz del proyecto.
- Python 3.8+: Simplemente es el lenguaje obligatorio y principal del proyecto
- MySQL (producción): Como hice el despliegue en PythonAnywhere, tuve que usar MySQL ya que es la base de datos que ofrecen en su plan gratuito, aunque el proyecto está diseñado para ser compatible con cualquier base de datos soportada por Django, incluyendo PostgreSQL y SQLite, MongoDB, MariaDB etc.
- SQLlite (desarrollo): Ligera y rápida para desarrollo local, no requiere configuración adicional, ideal para pruebas y desarrollo rápido.

## Instalación Automática

1. Ejecutar el archivo main.py

```bash
python main.py
```

1. Una vez termine de instalar las dependencias y configurar la base de datos, acceder a [http://localhost:8000/](http://localhost:8000/)

## Instalación Manual

### 1. Clonar repositorio

```bash
git clone https://github.com/Briell06/proyecto.git
cd "proyecto"
```

### 2. Configurar entorno virtual

### Windows

```bash
#crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual
.venv\Scripts\activate

# instalar dependencias
pip install -r requirements.txt
```

### Linux/macOS

```bash
# crear el entorno virtual
python3 -m venv .venv

# activar el entorno virtual
source .venv/bin/activate

# instalar dependencias
pip install -r requirements.txt
```

### 3. Configurar base de datos

#### Windows

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python3 manage.py migrate
```

#### Linux/macOS

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python3 manage.py migrate
```

### 4. Crear usuario administrador

#### Windows

```bash
python manage.py createsuperuser
```

#### Linux/macOS

```bash
python3 manage.py createsuperuser
```

### 5. Iniciar servidor

#### Windows

```bash
python manage.py runserver
```

#### Linux/macOS

```bash
python3 manage.py runserver
```

Acceder a [http://localhost:8000/](http://localhost:8000/)

## Uso

### Flujo de trabajo

1. **Crear recursos** (en orden):
   - Pistas: `/pistas/crear/`
   - Puertas: `/puertas/crear/`
   - Personal: `/personal/crear/` (pilotos y copilotos)
   - Aeronaves: `/aeronaves/crear/`

2. **Configurar restricciones** (opcional): `/restricciones/crear/`
   - Define correquisitos entre recursos que deben usarse juntos
   - Define exclusiones mutuas entre recursos incompatibles
   - Consulta ejemplos en la sección "Reglas de negocio"

3. **Crear vuelo**: `/vuelos/crear/`
   - Asignar pista, puerta, aeronave, piloto y copilotos
   - El sistema valida la disponibilidad y restricciones automáticamente

4. **Buscar horario disponible**: `/buscar-horario/`
   - Selecciona recursos y duración del vuelo
   - El sistema encuentra el próximo slot disponible automáticamente

5. **Consultar disponibilidad**: `/disponibilidad/`
   - Verificar recursos libres en un rango de tiempo específico

6. **Administración**: `/admin/`
   - Gestión avanzada de todos los recursos

### Ejemplo de vuelo

```text
Número: AA123
Origen: New York
Destino: Miami
Salida: 2025-10-20 10:00
Llegada: 2025-10-20 13:00
Estado: Programado
```

Seleccionar pista, puerta, aeronave, piloto y copilotos (mínimo 1 para vuelo de 3 horas).

## Reglas de negocio

### Sistema de Restricciones de Recursos

El sistema implementa dos tipos de restricciones que validan automáticamente las combinaciones de recursos en cada
vuelo:

#### 1. Co-requisitos (Inclusión Obligatoria)

Cuando se usa un recurso primario, **DEBE** incluirse un recurso complementario específico.

**Ejemplos implementables en el dominio de aeropuerto:**

- **Pista grande requiere puerta grande**: Si se asigna la Pista 01L (para aviones grandes como Boeing 747), DEBE
  asignarse una puerta grande (A1-A5) capaz de recibir aviones de esa categoría.
- **Aeronave internacional requiere personal de aduana**: Si se usa una aeronave configurada para vuelos
  internacionales, DEBE incluirse personal de aduana en el vuelo.

- **Piloto senior requiere aeronave certificada**: Si se asigna un piloto certificado en aeronaves especiales (ej:
  Boeing 787), DEBE usarse una aeronave de ese tipo específico.

**Cómo crear un co-requisito:**

1. Ve a `/restricciones/crear/`
2. Selecciona "Co-requisito" como tipo
3. Define el recurso primario (el que dispara la regla)
4. Define el recurso requerido (el que debe estar presente)

#### 2. Exclusión Mutua

Cuando se usa un recurso primario, **NO PUEDE** usarse un recurso específico en el mismo vuelo.

**Ejemplos implementables en el dominio de aeropuerto:**

- **Pistas paralelas en uso simultáneo**: Si se asigna la Pista 01L, NO PUEDE usarse la Pista 01R (pistas paralelas que
  no pueden operar simultáneamente por seguridad).

- **Puertas adyacentes**: Si un vuelo usa la Puerta A1, NO PUEDE usar la Puerta A2 (puertas adyacentes reservadas para
  aviones grandes que requieren espacio extra).

- **Incompatibilidad de aeronave-puerta**: Si se asigna un Boeing 747 (avión grande), NO PUEDE usarse la Puerta C1 (
  puerta pequeña para aviones regionales).

**Cómo crear una exclusión mutua:**

1. Ve a `/restricciones/crear/`
2. Selecciona "Exclusión Mutua" como tipo
3. Define el recurso primario
4. Define el recurso excluido (el que no puede estar presente)

#### Validación Automática

Todas las restricciones activas se validan automáticamente cuando:

- Se crea un nuevo vuelo
- Se actualiza un vuelo existente
- Se modifican los recursos asignados

Si se viola una restricción, el sistema mostrará un mensaje de error claro indicando qué regla se violó y qué recurso
falta o sobra.

### Búsqueda Inteligente de Horarios ("Buscar Hueco")

Función avanzada que encuentra automáticamente el próximo horario disponible para un vuelo.

**Cómo funciona:**

1. Especificas los recursos que necesitas (pista, puerta, aeronave, piloto)
2. Defines la duración del vuelo en horas
3. El sistema busca en los próximos 30 días
4. Valida que TODOS los recursos estén disponibles simultáneamente
5. Verifica que no se violen restricciones activas
6. Considera el período de mantenimiento de 24 horas de aeronaves

**Acceso:** `/buscar-horario/`

El algoritmo busca en incrementos de 1 hora y retorna el primer slot completamente válido encontrado.

### Requisitos de copilotos

- Vuelos ≤ 4 horas: 1 copiloto
- Vuelos 4-8 horas: 2 copilotos
- Vuelos > 8 horas: 3 copilotos

### Mantenimiento de aeronaves

Las aeronaves requieren 24 horas entre vuelos para mantenimiento obligatorio.

### Validaciones

- Longitud de pista: 800-5000 metros
- Capacidad de aeronave: 1-700 pasajeros
- Año de fabricación: 1990-presente
- Experiencia del personal: 0-50 años
- Duración máxima de vuelo: 20 horas

### Mecanismo de Validación en el Ciclo de Vida del Modelo

Para garantizar que ninguna regla de negocio sea vulnerada (ya sea desde la interfaz web, la API o el panel de administración), las validaciones se centralizan en el método `clean()` del modelo `Flight`, interceptando los datos antes de su persistencia en la base de datos (`save()`).

#### Implementación del Bloque Try-Except y Manejo de Excepciones

El sistema utiliza la estructura de control `try-except` combinada con `ValidationError` de Django para capturar fallos lógicos de manera elegante. El flujo de validación sigue este orden estricto:

- **Validación de Rangos Físicos**: Se comprueba que los atributos cuantitativos estén dentro de los límites operacionales (ej. longitud de pista $\ge 800$m y $\le 5000$m). Si falla, se levanta un error mapeado al campo específico.
- **Cálculo de Copilotos**: Se evalúa la duración del vuelo ($V_{llegada} - V_{salida}$). Mediante una estructura condicional, se determina el número mínimo de copilotos requeridos. Si el conteo de la relación _Many-to-Many_ es inferior al requerido, se interrumpe el guardado.
- **Control de Excepciones de Concurrencia**: Al interactuar con la base de datos para verificar exclusiones mutuas, cualquier anomalía en los tipos de datos o inconsistencia relacional es capturada por un bloque genérico `except Exception as e`, el cual registra el error en los logs del servidor y expone un mensaje amigable al usuario, evitando la caída del hilo de ejecución del servidor web (Error 500).

## Modelos principales

- **Runway**: Pistas de aterrizaje/despegue
- **Gate**: Puertas de embarque
- **Aircraft**: Aeronaves de la flota
- **Personnel**: Pilotos y copilotos
- **Flight**: Vuelos programados
- **ResourceConstraint**: Restricciones de recursos (Correquisitos y Exclusión Mutua)

### Diagrama de Relaciones y Estructura del ORM

El corazón del sistema radica en su consistencia relacional. A continuación, se detalla cómo se estructuran y vinculan los modelos principales a través del ORM de Django:

1. **Modelos Base independientes**: `Runway` (Pistas), `Gate` (Puertas), y `Aircraft` (Aeronaves) actúan como entidades maestras. Cada una almacena propiedades físicas cruciales para la validación (como la longitud de la pista o la capacidad de pasajeros de la aeronave).
2. **Modelos de Personal (`Personnel`)**: Diseñado de manera flexible para categorizar el rol mediante opciones (_choices_), distinguiendo estrictamente entre pilotos y copilotos para satisfacer las restricciones de tripulación.
3. **El Modelo Central (`Flight`)**: Es la entidad transaccional del sistema. Concentra relaciones de tipo Clave Foránea (`ForeignKey`) hacia `Runway`, `Gate`, `Aircraft` y el piloto principal, además de una relación de Muchos a Muchos (`ManyToManyField`) hacia `Personnel` para gestionar el equipo de copilotos.
4. **Modelo de Restricciones (`ResourceConstraint`)**: Implementa un patrón de diseño meta-configurable. En lugar de codificar las reglas de exclusión en manualmente, este modelo almacena dinámicamente qué recurso (`GenericForeignKey` o IDs relacionados) activa una regla de co-requisito o exclusión mutua sobre otro.

## Endpoints

- `/` - Dashboard principal
- `/pistas/` - Gestión de pistas
- `/puertas/` - Gestión de puertas
- `/aeronaves/` - Gestión de aeronaves
- `/personal/` - Gestión de personal
- `/vuelos/` - Gestión de vuelos
- `/restricciones/` - Gestión de restricciones de recursos
- `/buscar-horario/` - Búsqueda inteligente de horarios
- `/disponibilidad/` - Consulta de disponibilidad

## Configuración

Archivo principal: `config/settings.py`

- `DEBUG = True` - Activar solo en desarrollo
- `LANGUAGE_CODE = "es-mx"` - Localización en español
- `TIME_ZONE = "America/Havana"` - Zona horaria

## Aprendizaje

Lo que más aprendí al diseñar un sistema complejo con múltiples modelos relacionados, fue a aplicar principios de diseño de software y buenas prácticas de desarrollo. También mejoré mis habilidades en Django, ya que tenía experiencia previa con este framework y se me hizo bastante óptimo y familiar para desarrollar este proyecto, especialmente en la gestión de relaciones entre modelos (Lo que más me costó xdd) y el potencial que tienen las funciones para crear porciones de código reutilizables que te evitan repetición de código y bugs innecesarios, también lo útil que es el bloque try except a la hora te interceptar errores que pueden tumbar un programa y en lugar de eso gestionarlos y minimizarlos.

Proyecto desarrollado para la Universidad de la Habana en la carrera de Ciencias de la Computación, primer semestre.

© Briell Quintana Hernández 2025
