# Configuraciones de Locomoción en Robots Móviles

**Autor:** Tadeo Alvarez Nájera  
**Matrícula:** 2630002  
**Fecha:** Octubre 2026

---

## 1. Conceptos básicos

### ¿Qué es un robot móvil?

Un robot móvil es una máquina autónoma o teleoperada capaz de desplazarse por su entorno para cumplir una tarea. A diferencia de un brazo robótico fijo, un robot móvil lleva su sistema de locomoción consigo, lo que le permite cambiar de posición y orientación en el espacio de trabajo. Su diseño integra sensores para percibir el entorno, un sistema de control para tomar decisiones y actuadores para ejecutar el movimiento.

### Diferencia entre un robot móvil y un robot manipulador fijo

Un **robot manipulador fijo** está anclado a una base y su alcance está limitado por la geometría de sus articulaciones. Trabaja en una zona de trabajo predefinida y no puede desplazarse. Un **robot móvil**, en cambio, puede trasladarse a diferentes ubicaciones, lo que amplía enormemente su campo de acción. Mientras un manipulador fijo se especializa en tareas de precisión en un punto concreto (soldadura, ensamblaje), un robot móvil se especializa en tareas que requieren desplazamiento (transporte, inspección, vigilancia).

### Función del sistema de locomoción

El sistema de locomoción es el conjunto de mecanismos que permite al robot desplazarse. Su función principal es convertir la energía almacenada (eléctrica, neumática o hidráulica) en movimiento controlado. Determina la **maniobrabilidad**, la **estabilidad**, la **capacidad de carga** y la **eficiencia energética** del robot. La elección del sistema de locomoción es una de las decisiones de diseño más críticas, porque condiciona qué movimientos puede realizar el robot y en qué tipo de terreno puede operar.

### ¿Qué significa movilidad omnidireccional?

Un robot tiene **movilidad omnidireccional** (también llamada holonómica) cuando puede moverse en cualquier dirección del plano sin necesidad de cambiar su orientación. Es decir, puede desplazarse hacia adelante, atrás, lateralmente o en diagonal manteniendo su frente apuntando en la misma dirección. Los robots con configuraciones no holonómicas, como el diferencial o el Ackermann, deben girar primero para poder desplazarse en una nueva dirección.

### Relación entre disposición de ruedas y movimientos

La disposición de las ruedas determina los **grados de libertad** del robot y las **restricciones cinemáticas** que lo limitan. Por ejemplo:
- **Dos ruedas motrices en un eje común (diferencial):** el robot puede avanzar, retroceder y girar, pero no desplazarse lateralmente sin girar primero.
- **Tres o más ruedas Omni distribuidas:** el robot puede moverse en cualquier dirección sin rotar.
- **Cuatro ruedas Mecanum:** mismo principio, pero con mayor estabilidad y capacidad de carga.
- **Dirección Ackermann:** las ruedas delanteras giran para cambiar la orientación, como en un automóvil.

### ¿Dónde se utilizan robots móviles?

- **Logística y almacenes:** robots de transporte como los de Amazon Robotics.
- **Exploración:** rovers espaciales (Perseverance, Curiosity).
- **Agricultura:** robots de siembra, cosecha y monitoreo de cultivos.
- **Servicios:** robots de limpieza, reparto y asistencia en hospitales.
- **Industria:** AGVs (vehículos de guiado automático) en líneas de producción.
- **Investigación:** plataformas educativas como TurtleBot o ROS-based robots.

---

## 2. Robot diferencial con rueda de castor

### ¿Cómo están colocadas las ruedas motrices?

El robot diferencial tiene **dos ruedas motrices independientes** montadas en un mismo eje, una a cada lado del chasis. Cada rueda está conectada a su propio motor, lo que permite controlar su velocidad de forma independiente. Además, se añade una **rueda de castor** (o rueda loca) en la parte delantera o trasera para proporcionar un tercer punto de apoyo y mantener el equilibrio. La rueda de castor es pasiva: no tiene motor ni dirección propia, simplemente gira y se orienta libremente según el movimiento del robot.

```
          Rueda de castor
                ○
               / \
              /   \
             /     \
            /       \
      ○━━━━━━━━━━━━━━━━━━━○
   Rueda                Rueda
  izquierda            derecha
```

### ¿Para qué sirve la rueda de castor?

La rueda de castor sirve como **punto de apoyo pasivo**. Sin ella, el robot tendría solo dos puntos de contacto y se volcaría hacia adelante o hacia atrás. La rueda de castor permite que el robot mantenga una postura estable sin restringir el movimiento: al ser pasiva, no impone restricciones cinemáticas adicionales y se adapta a cualquier dirección de desplazamiento.

### Avance en línea recta

Para avanzar en línea recta, ambas ruedas motrices giran a la **misma velocidad y en el mismo sentido** (ambas hacia adelante o ambas hacia atrás). La rueda de castor sigue el movimiento sin ofrecer resistencia significativa.

### Giro a la izquierda o derecha

- **Giro a la izquierda:** la rueda derecha gira más rápido que la izquierda (o la izquierda gira en sentido contrario). El robot describe una curva hacia la izquierda.
- **Giro a la derecha:** la rueda izquierda gira más rápido que la derecha. El robot curva hacia la derecha.

### ¿Qué sucede cuando una rueda gira más rápido que la otra?

Cuando una rueda gira más rápido que la otra, el robot describe una **trayectoria curva**. El centro de giro se desplaza hacia el lado de la rueda más lenta. La diferencia de velocidades determina el **radio de curvatura**: a mayor diferencia, menor radio de giro. Si una rueda se detiene y la otra gira, el robot pivota alrededor de la rueda detenida.

### Giro sobre su propio eje

Para girar sobre su propio eje (rotación en el lugar), las ruedas izquierda y derecha giran a la **misma velocidad pero en sentidos opuestos**. Una avanza y la otra retrocede, lo que hace que el robot rote alrededor del punto medio entre ambas ruedas.

### Ventajas de la configuración diferencial

- **Simplicidad mecánica:** solo requiere dos motores y una rueda pasiva.
- **Control sencillo:** la cinemática es fácil de modelar y programar.
- **Giro sobre su eje:** puede rotar en el lugar sin necesidad de espacio adicional.
- **Bajo costo:** es la configuración más económica de implementar.

### Limitaciones

- **No puede desplazarse lateralmente:** para moverse de lado debe girar primero.
- **Dependencia de la fricción:** en superficies resbaladizas, las ruedas pueden patinar y perder precisión en la odometría.
- **Inestabilidad en pendientes:** la rueda de castor puede perder contacto en terrenos irregulares.
- **Giros poco precisos:** según estudios, los giros pueden ser imprecisos por la naturaleza pasiva de la rueda de castor.

### Aplicaciones

- Robots educativos (TurtleBot, Pioneer).
- Robots de limpieza (aspiradoras automáticas).
- AGVs para transporte en almacenes.
- Robots de vigilancia y patrullaje.

### Análisis de movimiento: tabla de comportamientos

| Rueda izquierda | Rueda derecha |                Movimiento del robot                |
|-----------------|---------------|----------------------------------------------------|
| Avanza          | Avanza        | Avance en línea recta                              |
| Detenida        | Avanza        | Giro a la izquierda (pivote sobre rueda izquierda) |
| Avanza          | Detenida      | Giro a la derecha (pivote sobre rueda derecha)     |
| Avanza          | Retrocede     | Giro sobre su propio eje (sentido horario)         |
| Retrocede       | Avanza        | Giro sobre su propio eje (sentido antihorario)     |
| Retrocede       | Retrocede     | Retroceso en línea recta                           |

---

## 3. Robots omnidireccionales con ruedas Omni

### ¿Cómo está construida una rueda Omni?

Una rueda Omni (también llamada rueda sueca) está formada por un **cuerpo principal** que gira alrededor de su eje, y una serie de **pequeños rodillos** montados en su periferia. Estos rodillos están dispuestos perpendicularmente al plano de la rueda, de modo que pueden girar libremente alrededor de su propio eje. El cuerpo principal transmite la fuerza motriz en una dirección, mientras que los rodillos permiten el deslizamiento libre en la dirección perpendicular.

```
        Rodillos (giran libremente)
           ↕  ↕  ↕  ↕
       ┌─────────────────┐
      /   ○   ○   ○   ○   \
     │    ○   ○   ○   ○    │
      \   ○   ○   ○   ○   /
       └─────────────────┘
       Cuerpo de la rueda
```

### ¿Para qué sirven los rodillos?

Los rodillos sirven para **desacoplar el movimiento** de la rueda en dos direcciones ortogonales. Cuando la rueda gira, los rodillos transmiten fuerza en la dirección de avance. Cuando el robot intenta moverse lateralmente, los rodillos giran libremente y permiten ese deslizamiento sin resistencia. Esta característica es lo que hace que la rueda sea **holonómica**: puede moverse en cualquier dirección sin restricciones.

### Dirección de fuerza y deslizamiento libre

- **Dirección de fuerza:** la rueda Omni puede generar fuerza en la dirección paralela al plano de la rueda (su dirección de rodadura).
- **Dirección de deslizamiento libre:** los rodillos permiten el movimiento libre en la dirección perpendicular al plano de la rueda (dirección lateral).

### Configuración de tres ruedas

En un robot omnidireccional de tres ruedas, las ruedas se distribuyen **equiespaciadas a 120°** alrededor del chasis. Cada rueda está orientada de modo que su dirección de fuerza apunta tangencialmente al círculo que forman.

```
        Rueda 1
            ↑
           / \
          /   \
         /     \
Rueda 2 ←───────→ Rueda 3
```

**Movimientos posibles:**
- **Avance/retroceso:** las tres ruedas giran en la dirección adecuada para generar una resultante hacia adelante o atrás.
- **Desplazamiento lateral:** las tres ruedas combinan sus velocidades para generar una resultante perpendicular al frente.
- **Movimiento diagonal:** combinación de avance y lateral.
- **Giro sobre su eje:** las ruedas giran de modo que las fuerzas tangenciales generan un par de rotación.

**¿Qué sucede con velocidades diferentes?** Cuando las tres ruedas giran a velocidades diferentes, la resultante vectorial de las fuerzas produce un movimiento en cualquier dirección y con cualquier orientación. El control consiste en calcular las velocidades de cada rueda para obtener la velocidad deseada del chasis (traslación y rotación).

### Configuración de cuatro ruedas

En la configuración de cuatro ruedas Omni, las ruedas se colocan normalmente en los **cuatro vértices** de un chasis rectangular, con orientaciones alternadas. La combinación de velocidades permite generar movimiento en cualquier dirección.

**Diferencias con tres ruedas:**
- **Mayor estabilidad:** cuatro puntos de apoyo ofrecen una base más estable.
- **Mayor capacidad de carga:** se distribuye mejor el peso.
- **Control más complejo:** hay cuatro variables de control en lugar de tres, aunque el principio es el mismo.
- **Mayor costo:** requiere cuatro motores en lugar de tres.

**Ventajas:** mejor tracción, mayor estabilidad, capacidad de carga superior.  
**Limitaciones:** mayor complejidad mecánica y de control, mayor costo, mayor peso.

---

## 4. Robot omnidireccional con ruedas Mecanum

### ¿Cómo están construidas?

Una rueda Mecanum es similar a una rueda Omni, pero sus rodillos están montados **en ángulo de 45°** respecto al eje de la rueda. El cuerpo principal gira alrededor del eje horizontal, y los rodillos periféricos giran alrededor de ejes inclinados. Esta inclinación es lo que genera las componentes de fuerza que permiten el movimiento omnidireccional.

### Diferencia entre rueda Mecanum y rueda Omni

|          Característica         |              Rueda Omni            |                Rueda Mecanum               |
|---------------------------------|------------------------------------|--------------------------------------------|
| **Orientación de los rodillos** | Perpendicular al plano de la rueda | A 45° respecto al eje de la rueda          |
| **Dirección de fuerza**         | Paralela al plano de la rueda      | Componentes en dos direcciones ortogonales |
| **Complejidad**                 | Menor                              | Mayor                                      |
| **Eficiencia**                  | Mayor                              | Menor (más pérdidas por fricción)          |
| **Costo**                       | Menor                              | Mayor                                      |

### ¿Por qué se utilizan cuatro ruedas?

Generalmente se utilizan cuatro ruedas Mecanum porque cada rueda produce componentes de fuerza en dos direcciones, y la combinación de las cuatro permite generar una resultante en cualquier dirección. Con cuatro ruedas se obtiene mayor estabilidad y capacidad de carga que con tres, y la configuración en "X" (vista desde arriba) es la que permite la cancelación de fuerzas laterales no deseadas.

### Orientación respecto al chasis

Las ruedas Mecanum deben montarse de modo que los rodillos de las ruedas diagonales apunten en la misma dirección. Vista desde arriba, las líneas diagonales que forman los rodillos deben formar una "X". Esto significa que:
- La rueda delantera izquierda y la trasera derecha tienen rodillos que apuntan en una dirección.
- La rueda delantera derecha y la trasera izquierda tienen rodillos que apuntan en la dirección opuesta.

```
        Delantera izquierda          Delantera derecha
              ↖                           ↗
               \                         /
                \                       /
                 \                     /
                  \                   /
                   \                 /
                    \               /
                     \             /
                      \           /
                       \         /
                        \       /
                         \     /
                          \   /
                           \ /
                            X
                           / \
                          /   \
                         /     \
                        /       \
                       /         \
                      /           \
                     /             \
                    /               \
                   /                 \
                  /                   \
                 /                     \
                /                       \
               ↙                         ↘
        Trasera izquierda            Trasera derecha
```

### Combinación de movimientos

|            Movimiento          | Delantera izquierda | Delantera derecha | Trasera izquierda | Trasera derecha |
|--------------------------------|---------------------|-------------------|-------------------|-----------------|
| **Avanzar**                    | ↑ Adelante          | ↑ Adelante        | ↑ Adelante        | ↑ Adelante      |
| **Retroceder**                 | ↓ Atrás             | ↓ Atrás           | ↓ Atrás           | ↓ Atrás         |
| **Desplazarse a la izquierda** | ↓ Atrás             | ↑ Adelante        | ↑ Adelante        | ↓ Atrás         |
| **Desplazarse a la derecha**   | ↑ Adelante          | ↓ Atrás           | ↓ Atrás           | ↑ Adelante      |
| **Girar a la izquierda**       | ↓ Atrás             | ↑ Adelante        | ↓ Atrás           | ↑ Adelante      |
| **Girar a la derecha**         | ↑ Adelante          | ↓ Atrás           | ↑ Adelante        | ↓ Atrás         |

Las flechas indican el sentido de giro de cada rueda. La combinación de fuerzas longitudinales y transversales produce el movimiento resultante.

---

## 5. Robot con dirección Ackermann

### Distribución de ruedas

En la geometría Ackermann, el vehículo tiene **cuatro ruedas**: dos delanteras y dos traseras. Las ruedas **delanteras son las directrices** (giran para cambiar la orientación del vehículo) y las **traseras son las motrices** (proporcionan la tracción). Este esquema es el utilizado en automóviles convencionales.

### ¿Por qué las ruedas interiores y exteriores no giran con el mismo ángulo?

Durante una curva, la rueda interior recorre un arco de menor radio que la rueda exterior. Si ambas giraran con el mismo ángulo, la rueda interior tendería a deslizarse. La geometría de Ackermann resuelve esto haciendo que la rueda interior gire un ángulo mayor que la exterior. Esto se logra mediante un mecanismo de dirección (generalmente un paralelogramo articulado) que hace que los ejes de las ruedas apunten a un **punto común** llamado Centro de Rotación Instantáneo (ICR).

```
                    Punto de giro (ICR)
                         ●
                        / \
                       /   \
                      /     \
                     /       \
                    /         \
                   /           \
                  /             \
                 /               \
                /                 \
               /                   \
              /                     \
             /                       \
            /                         \
           /                           \
          /                             \
         /                               \
        ○                                 ○
      Rueda                              Rueda
     interior                           exterior
```

### Radio de giro

El **radio de giro** es la distancia desde el centro de rotación instantáneo hasta el eje del vehículo. Cuanto mayor sea el radio, más amplia será la curva. En la geometría Ackermann, el radio de giro está determinado por la distancia entre ejes y el ángulo de dirección: a mayor ángulo, menor radio de giro.

### ¿Por qué no puede desplazarse lateralmente?

Un vehículo Ackermann es **no holonómico**: sus ruedas solo pueden rodar en la dirección en que están orientadas. Para cambiar de posición lateral, el vehículo debe avanzar o retroceder describiendo una curva. No puede moverse de lado sin desplazarse longitudinalmente. Esta es una restricción cinemática fundamental de la configuración.

### Semejanzas con la dirección de un automóvil

La geometría Ackermann es exactamente la que utilizan los automóviles convencionales. Las ruedas delanteras giran para dirigir el vehículo, las traseras proporcionan la tracción, y la diferencia de ángulos entre la rueda interior y exterior permite tomar curvas sin deslizamiento lateral.

### Ejemplos de robots con configuración Ackermann

- **BLUE (Bot for Localization on Unstructured Environments):** robot de la Universidad de Alicante con geometría Ackermann.
- **Robots de reparto autónomo:** algunos vehículos de reparto de última milla utilizan esta configuración.
- **Rovers agrícolas:** tractores autónomos y robots de campo.

---

## 6. Comparación de configuraciones

|       Configuración      |    Número típico de ruedas    |  Movimiento lateral  | Giro sobre su eje | Complejidad mecánica | Complejidad de control |                  Aplicaciones                  |
|--------------------------|-------------------------------|----------------------|-------------------|----------------------|------------------------|------------------------------------------------|
| **Diferencial + castor** | 2 motrices + 1 castor         | No                   | Sí                | Baja                 | Baja                   | Robots educativos, aspiradoras, AGVs           |
| **Omni de 3 ruedas**     | 3                             | Sí                   | Sí                | Media                | Media                  | Robots de fútbol, plataformas de investigación |
| **Omni de 4 ruedas**     | 4                             | Sí                   | Sí                | Media-alta           | Media-alta             | Robots de logística, plataformas móviles       |
| **Mecanum**              | 4                             | Sí                   | Sí                | Alta                 | Alta                   | Robots de competencia, transporte preciso      |
| **Ackermann**            | 4 (2 directrices, 2 motrices) | No                   | No                | Media                | Media                  | Vehículos autónomos, rovers agrícolas          |

### Selección de configuración por caso

|                               Caso                                   |       Configuración elegida        |                                 Razón                                   |
|----------------------------------------------------------------------|------------------------------------|-------------------------------------------------------------------------|
| Robot pequeño para aprender programación y control                   | **Diferencial + castor**           | Simplicidad mecánica y de control, bajo costo, fácil de programar       |
| Robot para almacén con espacios reducidos                            | **Mecanum** o **Omni de 4 ruedas** | Puede desplazarse lateralmente sin girar, ideal para pasillos estrechos |
| Plataforma que necesita moverse lateralmente sin cambiar orientación | **Mecanum** o **Omni**             | Movilidad holonómica completa                                           |
| Vehículo autónomo que debe circular como un automóvil                | **Ackermann**                      | Comportamiento similar al de un coche, estabilidad en carretera         |
| Robot para competencia con cambios rápidos de dirección              | **Mecanum** o **Omni**             | Máxima maniobrabilidad, cambios instantáneos de dirección               |
| Robot móvil sencillo que utilice únicamente dos motores              | **Diferencial + castor**           | Solo requiere dos motores, la rueda de castor es pasiva                 |

---

## 7. Análisis del movimiento

### Diferencial: ¿Qué debe hacer cada rueda para girar sobre su propio eje?

Para girar sobre su propio eje, la rueda izquierda y la rueda derecha deben girar a la **misma velocidad pero en sentidos opuestos**. Una avanza mientras la otra retrocede. Esto genera un par de rotación alrededor del centro del eje de las ruedas, haciendo que el robot rote en el lugar sin desplazarse.

### Omni: ¿Por qué los rodillos permiten generar movimiento lateral?

Los rodillos de la rueda Omni están montados **perpendicularmente** al plano de la rueda. Cuando el robot intenta moverse lateralmente, los rodillos giran libremente alrededor de su propio eje y permiten que la rueda se deslice en esa dirección sin oponer resistencia. Al mismo tiempo, la rueda puede transmitir fuerza en la dirección de rodadura. La combinación de ambas direcciones (fuerza en una dirección, deslizamiento libre en la perpendicular) es lo que permite generar movimiento en cualquier dirección.

### Mecanum: ¿Por qué el robot puede desplazarse lateralmente aunque ninguna rueda esté orientada directamente hacia el costado?

Los rodillos de la rueda Mecanum están inclinados a **45°** respecto al eje de la rueda. Cuando la rueda gira, la fuerza se descompone en dos componentes: una longitudinal y una transversal. Al combinar las cuatro ruedas con sus rodillos orientados en "X", las componentes transversales de las ruedas opuestas se suman o cancelan según la dirección de giro, generando una resultante lateral. Aunque ninguna rueda apunte directamente hacia el costado, la **suma vectorial** de las fuerzas de las cuatro ruedas produce el movimiento lateral deseado.

### Ackermann: ¿Por qué el vehículo necesita avanzar o retroceder para cambiar de posición lateral?

Porque sus ruedas son **no holonómicas**: solo pueden rodar en la dirección en que están orientadas. No tienen rodillos que permitan el deslizamiento lateral. Para cambiar de posición lateral, el vehículo debe **describir una curva**: avanza o retrocede mientras las ruedas delanteras están giradas, lo que genera un desplazamiento lateral neto. Sin movimiento longitudinal, no hay cambio de posición lateral.

---

## 8. Aplicación en un robot real: Baxter Mobility Base

|        Característica        |                                                             Descripción                                                                      |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Nombre del robot**         | Baxter Mobility Base                                                                                                                         |
| **Fabricante**               | Dataspeed Inc.                                                                                                                               |
| **Tipo de locomoción**       | Omnidireccional con ruedas Mecanum                                                                                                           |
| **Número y tipo de ruedas**  | 4 ruedas Mecanum                                                                                                                             |
| **Sensores principales**     | Detección de obstáculos por ultrasonido (360°), interruptores de contacto (bumpers), IMU de 9 DOF, cámara descendente para navegación por QR |
| **Actuadores de movimiento** | 4 motores independientes (uno por rueda) con controladores encoder/servo de alto rendimiento                                                 |
| **Aplicación**               | Logística, seguridad, manufactura, retail, control de calidad, telepresencia, mantenimiento                                                  |

**¿Por qué es adecuada la configuración Mecanum para este robot?** Baxter Mobility Base necesita moverse en entornos de oficina y fábrica con pasillos estrechos, puertas y espacios reducidos. La configuración Mecanum le permite desplazarse en cualquier dirección sin cambiar su orientación, lo que es esencial para navegar con precisión en espacios limitados. Además, la base incluye una suspensión independiente en las cuatro ruedas para maximizar la tracción en superficies como alfombra, baldosa, cemento y asfalto. La capacidad de moverse lateralmente mientras mantiene el frente apuntando hacia adelante es crucial para tareas como transporte de material, inspección de estanterías y telepresencia.

---

## 9. Reflexión final

### ¿Qué configuración te pareció más sencilla de comprender?

La configuración **diferencial con rueda de castor** me resultó la más sencilla de comprender. Su principio es intuitivo: dos ruedas que giran a diferentes velocidades producen un giro, y la rueda de castor simplemente acompaña el movimiento. No requiere rodillos especiales ni geometrías complejas, y la relación entre la velocidad de las ruedas y el movimiento del robot es directa y fácil de visualizar.

### ¿Cuál ofrece mayor libertad de movimiento?

La configuración **Mecanum** (y en general las omnidireccionales) ofrece la mayor libertad de movimiento. Puede desplazarse en cualquier dirección del plano sin cambiar su orientación, combinando traslación y rotación de forma independiente. Esto la hace ideal para entornos complejos donde se requiere precisión y maniobrabilidad.

### ¿Qué configuración utilizarías para construir tu primer robot móvil?

Usaría la **diferencial con rueda de castor**. Es la más económica, sencilla de construir y de programar. Requiere solo dos motores y un controlador básico, y la cinemática es fácil de modelar. Una vez que domine esta configuración, podría avanzar hacia configuraciones omnidireccionales si necesito mayor maniobrabilidad.

### ¿Por qué no existe una sola configuración de ruedas adecuada para todos los robots?

Porque cada aplicación tiene requisitos diferentes de **maniobrabilidad**, **estabilidad**, **capacidad de carga**, **costo**, **mantenimiento** y **tipo de terreno**. Un robot de competencia necesita máxima agilidad; un vehículo autónomo necesita estabilidad a alta velocidad; un robot de almacén necesita moverse lateralmente en pasillos estrechos. La elección de la configuración es un **trade-off** entre estos factores, y no hay una solución universal. El diseño mecatrónico consiste precisamente en seleccionar la configuración que mejor se adapte a los requisitos específicos de cada aplicación.

---

## 10. Referencias

1. Ciendua. (2016). *Diseño de robot móvil con configuración diferencial y rueda de castor*. Universidad de La Salle. https://ciencia.lasalle.edu.co

2. Honpine. (2026). *AGV Drive Wheels vs Steering Wheels vs Casters: Complete Technical Comparison Guide*. https://www.honpine.com

3. UC3M. *Configuraciones de robots móviles*. Universidad Carlos III de Madrid. https://e-archivo.uc3m.es

4. IET Conference Proceedings. (2025). *Design and simulation analysis of three omni-directional wheels chassis for spherical robot*. https://digital-library.theiet.org

5. Politecnico di Torino. *3 Omni wheel drive consists in a platform usually driven by 3 omni wheels spaced at 120 deg*. https://webthesis.biblio.polito.it

6. REV Robotics. (2024). *Mecanum Wheel Setup and Behavior*. https://docs.revrobotics.com

7. Studica. (2026). *FTC Mecanum Drive Programming Tips*. https://www.studica.ca

8. RUA Universidad de Alicante. *Segmentación y clasificación del entorno para el control de robot BLUE con geometría Ackermann*. https://rua.ua.es

9. Repositorio URP. *Selección de configuración de robot móvil*. https://repositorio.urp.edu.pe

10. MDPI. (2025). *Robustness Test on Differential-Drive Platform*. https://www.mdpi.com

11. Generation Robots. *Baxter Mobility Base Datasheet*. https://www.generationrobots.com

12. Carnegie Mellon University. *Mobile Robot Wheel Configurations*. https://www.cs.cmu.edu

13. IEEE. *Four Wheeled Mobile Robots: A Review*. https://ieeexplore.ieee.org

14. Shabalina, K., Sagitov, A., & Magid, E. (2019). *Comparative analysis of mobile robot wheels design*. Kazan Federal University.

15. Springer Handbook of Robotics. *Wheeled Mobile Robots*. https://www.handbookofrobotics.org

16. University of Oslo. *Selection of a locomotion configuration for autonomous mobile robots*. https://www.duo.uio.no

17. KTH Royal Institute of Technology. *Kinematics of Mecanum and Universal Omni wheels*. https://kth.diva-portal.org

18. Caltech. *Kinematics and Odometry for a Differential Drive Vehicle*. https://robotics.caltech.edu

19. UNAM. *Modelos cinemáticos de robots móviles*. https://biorobotics.fi-p.unam.mx

20. MathWorks. *Mobile Robot Kinematics Equations*. https://jp.mathworks.com