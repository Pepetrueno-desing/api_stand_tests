# API Stand Tests — Urban Grocers

Proyecto de automatización de pruebas para la API de Urban Grocers.

---

## 📋 Descripción

Suite de pruebas automatizadas con **pytest** para validar los endpoints de la API:

- **Creación de usuarios** (`POST /api/v1/users/`)
- **Búsqueda de kits por productos** (`POST /api/v1/products/kits/`)
- **Consulta de logs** (`GET /api/logs/main/`)

La suite incluye **10 tests** que validan el campo `firstName` de la creación de usuarios: longitudes mínimas y máximas, caracteres especiales, números, espacios, campos faltantes y tipos incorrectos.

**Resultado actual:** `9 passed, 1 failed` — el fallo corresponde a un **bug real de la API** documentado más abajo.

---

## 🛠️ Requisitos

- Python 3.13+
- pip
- pytest
- requests
- Acceso al servidor de TripleTen

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone git@github.com:Pepetrueno-desing/api_stand_tests.git
cd api_stand_tests

# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# Instalar dependencias
pip install -r requirements.txt
📁 Estructura del proyecto
text
api_stand_tests/
├── .gitignore
├── README.md
├── requirements.txt
├── configuration.py
├── data.py
├── sender_stand_request.py
└── test_create_user.py
Archivo	Propósito
configuration.py	URLs y rutas (URL_SERVICE, CREATE_USER_PATH, PRODUCTS_KITS_PATH, LOG_MAIN_PATH, USERS_TABLE_PATH)
data.py	Datos de prueba (headers, user_body, product_ids)
sender_stand_request.py	Funciones de interacción con la API (post_new_user, post_products_kits)
test_create_user.py	Suite de 10 tests automatizados
requirements.txt	Dependencias del proyecto
▶️ Ejecución
bash
pytest test_create_user.py -v
Resultado esperado:

text
10 collected
9 passed, 1 failed
⚠️ El fallo no es un error del proyecto, sino un bug de la API detectado por los tests.

🧪 Cobertura de pruebas
#	Test	Caso cubierto	Resultado
1	test_create_user_2_letter_in_first_name_get_success_response	Nombre con 2 letras (mínimo válido)	✅ PASSED
2	test_create_user_15_letter_in_first_name_get_success_response	Nombre con 15 letras (máximo válido)	✅ PASSED
3	test_create_user_1_letter_in_first_name_get_error_response	Nombre con 1 letra (bajo el mínimo)	✅ PASSED
4	test_create_user_16_letter_in_first_name_get_error_response	Nombre con 16 letras (sobre el máximo)	✅ PASSED
5	test_create_user_has_space_in_first_name_get_error_response	Nombre con espacios	❌ FAILED → Bug
6	test_create_user_has_special_symbol_in_first_name_get_error_response	Caracteres especiales	✅ PASSED
7	test_create_user_has_number_in_first_name_get_error_response	Números en el nombre	✅ PASSED
8	test_create_user_no_first_name_get_error_response	Falta el parámetro firstName	✅ PASSED
9	test_create_user_empty_first_name_get_error_response	firstName vacío	✅ PASSED
10	test_create_user_number_type_first_name_get_error_response	firstName con tipo número	✅ PASSED
🐛 Bug detectado
🐞 La API acepta espacios en firstName
Campo	Detalle
Test	test_create_user_has_space_in_first_name_get_error_response
Esperado	400 Bad Request (los espacios no son válidos en firstName)
Obtenido	201 Created (la API creó el usuario)
Impacto	Se pueden crear usuarios con nombres que contienen espacios, violando la regla de negocio
Reportado	S3-64 en Jira
Severidad	Media
Este bug fue documentado y reportado como parte del flujo de trabajo de QA, demostrando la capacidad de identificar discrepancias entre la especificación y el comportamiento real de la API.

🔍 Endpoints explorados
Endpoint	Método	Uso
/api/v1/users/	POST	Crear usuario (cubierto por los tests)
/api/v1/products/kits/	POST	Buscar kits por productos (explorado manualmente)
/api/logs/main/	GET	Consultar logs del servidor (explorado manualmente)
/api/db/resources/user_model.csv	GET	Obtener tabla de usuarios (explorado manualmente)
📚 Aprendizajes
Automatización de API con pytest + requests.

Estructura de proyectos QA: separación de configuration.py, data.py, sender_stand_request.py y test_*.py.

Funciones auxiliares para construcción de datos: get_user_body, negative_assert_symbol, negative_assert_no_firstname.

Validación de respuestas: status_code, response.json() y campos específicos.

Manejo de tokens: obtención del authToken desde la respuesta de creación de usuario y uso en headers Authorization: Bearer {authToken}.

Casos positivos y negativos: tests que esperan 201 y tests que esperan 400.

Detección de bugs: identificar cuándo la API no cumple la especificación.

Uso de .copy() para no modificar diccionarios originales en pruebas.

Validación de mensajes de error exactos con assert.

👤 Autor
Juan Mendoza (Juancho) — QA Automation Engineer en formación
🔗 GitHub · LinkedIn