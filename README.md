<p align="center">
  <img src="img/logo1.png" alt="Logo 1" width="200"/>
</p>

# <span style="color: #FF5A5F">Análisis Integral de Datos de Airbnb</span>

## <span style="color: #FF5A5F">Descripción del Proyecto</span>

Este repositorio contiene un análisis exploratorio, estadístico e inferencial sobre más de **220,000 registros de alojamientos en Airbnb**, correspondientes al período 2010-2020, distribuidos en seis ciudades: **Madrid, Milán, Londres, Nueva York, Sídney y Tokio**. El objetivo del análisis es entender cómo varían los precios, la disponibilidad y otros factores clave del mercado de alquileres a corto plazo, tanto para **viajeros** como para **inversionistas potenciales**.

## <span style="color: #FF5A5F">Metodología de Análisis</span>

### <span style="color: #FF5A5F99">1. Limpieza y Preparación de Datos</span>

Los datos fueron fusionados a partir de archivos CSV individuales por ciudad mediante un pipeline automatizado. La limpieza incluyó:

- **Imputación de valores nulos**, con estrategias específicas por columna (ver tabla abajo).
- **Conversión de precios a dólares estadounidenses (USD)** usando un tipo de cambio fijo.
- **Normalización de texto** en columnas como `host_name`, `neighbourhood`, y `city`.
- **Eliminación o transformación de variables poco fiables** (`price`, `reviews_per_month`, etc.).

| Columna                          | % Nulos Inicial | Tratamiento               | Notas                |
| -------------------------------- | --------------- | ------------------------- | -------------------- |
| `neighbourhood_group`            | 68.86%          | Imputado como "Unknown"   | ⚠️ Poco fiable       |
| `last_review`                    | 30.74%          | Lógica + fallback         | ✅ Usar con cautela  |
| `reviews_per_month`              | 24.71%          | Imputado con 0.0 y lógica | ⚠️ Señal débil       |
| `availability_365`               | 5.21%           | Media global para Tokio   | ✅ Usar con cuidado  |
| `calculated_host_listings_count` | 5.21%           | Llenado con 0 en Tokio    | ⚠️ Considerar aparte |
| `host_name`                      | 0.32%           | Limpieza + "Unknown"      | ✅                   |
| `price_USD`                      | Nuevo campo     | Unificación de precios    | ✅                   |

> El conjunto está limpio a nivel sintáctico y estructural, pero se recomienda validación semántica (disponibilidad y geolocalización).

### <span style="color: #FF5A5F99">2. Análisis Estadístico y Descriptivo</span>

Se realizaron análisis **univariados**, **bivariados** y **multivariados** sobre las principales variables:

- Distribuciones de precios por ciudad y tipo de alojamiento.
- Relación entre número de reviews y disponibilidad.
- Comparativas entre barrios y ciudades.

Las herramientas utilizadas incluyen **Pandas**, **Seaborn**, **Matplotlib**, **NumPy**, **SciPy** y **Scikit-learn**.

### <span style="color: #FF5A5F99">3. Validación de Hipótesis</span>

Se contrastaron varias hipótesis, especialmente en la ciudad de **Madrid**:

- **H1: Los alojamientos con alta disponibilidad tienen mayor precio promedio.**  
  ✅ Aceptada parcialmente: alta disponibilidad (≥180 días) se asocia con precios más altos.

- **H2: Existen diferencias de precio entre barrios.**  
  ✅ Aceptada completamente: barrios como Retiro y Centro son más caros.

- **H3: Los alojamientos con más reviews son más caros.**  
  ❌ Rechazada: no hay evidencia significativa.

- **H4: El tipo de alojamiento influye en el precio.**  
  ✅ Aceptada completamente: los hoteles son los más caros.

**Implicaciones:**

- **Para anfitriones**: optimización de precios por zona y tipo.
- **Para huéspedes**: maximizar valor al comparar zonas.
- **Para inversores**: identificar oportunidades según rentabilidad y ubicación.

## <span style="color: #FF5A5F">Herramientas y Tecnologías</span>

### <span style="color: #FF5A5F99">Análisis de Datos</span>

- **Python**: Lenguaje principal de análisis
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas
- **SciPy**: Tests estadísticos avanzados
- **Scikit-learn**: Algoritmos de machine learning

### <span style="color: #FF5A5F99">Visualización</span>

- **Matplotlib**: Gráficos estáticos
- **Seaborn**: Visualizaciones estadísticas
- **Power BI**: Dashboards interactivos

## <span style="color: #FF5A5F">Dashboards de Power BI</span>

<p align="center">
  <img src="img/dashboard1.png" alt="Dashboard General" width="700"/>
</p>
Se desarrollaron dashboards interactivos  en Power BI que incluyen:

- Datos globales comparativos entre ciudades.
- Análisis individual por ciudad (filtros por tipo, zona, precio...).
- Tendencias de disponibilidad, densidad de alojamientos y precios medios.

> 📁 El archivo `.pbix` se encuentra incluido en el repositorio.

## <span style="color: #FF5A5F">Estructura del Proyecto</span>

```
airbnb-analysis/
├── data/ # Todos los csv de las diferentes ciudades + archivo comprimido del clean data
├── eda/ # Diferentes notebooks con limpieza, análisis e hipótesis
├── img/ # Logos y dashboards
├── processed_data/ # Datos tras ejecutar el script del data merger
├── scripts/ # Data merger
└── README.md
```

## <span style="color: #FF5A5F">Resultados y Hallazgos</span>

Este análisis permite una visión rica y detallada de cómo funcionan los alquileres de corto plazo en seis grandes ciudades. La combinación de herramientas estadísticas, visuales y de negocio lo hace útil tanto para análisis académico como para toma de decisiones en turismo y real estate.

Los resultados detallados del análisis, incluyendo validación de hipótesis y insights principales, se encuentran documentados en los notebooks de análisis y reportes específicos del proyecto.

Proporciona insights valiosos para:

- Anfitriones que buscan optimizar sus precios
- Viajeros que desean entender patrones de mercado
- Investigadores interesados en economía colaborativa
- Tomadores de decisiones en turismo urbano
