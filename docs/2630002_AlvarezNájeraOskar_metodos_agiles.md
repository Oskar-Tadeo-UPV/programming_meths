# Metodologías Ágiles: Guía Integral de Scrum, Kanban y Design Thinking

**Autor:** Tadeo Alvarez Nájera  
**Matrícula:** 2630002  
**Fecha:** Octubre 2026

---

## 1. Resumen Ejecutivo

### ¿Qué es "ágil"?

Ágil no es una metodología única ni un conjunto de reglas rígidas: es una filosofía de trabajo y una mentalidad organizacional. El término proviene del **Manifiesto Ágil**, un documento redactado en 2001 por 17 profesionales del desarrollo de software que buscaban una alternativa a los procesos pesados y burocráticos que caracterizaban la industria en ese entonces. En esencia, agilidad significa la capacidad de adaptarse rápidamente al cambio, entregar valor de forma incremental y mantener una comunicación constante con el cliente.

### ¿Por qué surge?

A finales de los años 90, los enfoques predictivos (como el modelo en cascada) fallaban con frecuencia porque asumían que los requisitos eran estables y que el cambio podía controlarse mediante planificación exhaustiva. La realidad demostró lo contrario: los proyectos de software son inherentemente complejos y volátiles. El Manifiesto Ágil surgió como respuesta a esa frustración: las empresas estaban tan centradas en documentar y planificar que perdían de vista lo verdaderamente importante: **complacer a los clientes**.

### Alcance del documento

Este documento cubre:
- Los **valores y principios** del Manifiesto Ágil y su impacto en la gestión del trabajo.
- Un **panorama comparativo** de tres marcos fundamentales: Scrum, Kanban y Design Thinking.
- Los **conceptos, roles, artefactos, eventos y métricas** esenciales de Scrum.
- Los **fundamentos, tablero, métricas de flujo y políticas** de Kanban.
- Las **fases, técnicas y aplicación práctica** del Design Thinking.
- **Conclusiones y referencias** para profundizar.

---

## 2. Principios Ágiles

### 2.1 Los cuatro valores del Manifiesto Ágil

El Manifiesto Ágil establece cuatro valores fundamentales. Aunque reconoce el valor de los elementos de la derecha, prioriza explícitamente los de la izquierda:

| Priorizamos…                    | Sobre…                   |
|---------------------------------|--------------------------|
| **Individuos e interacciones**  | Procesos y herramientas  |
| **Software funcionando**        | Documentación extensiva  |
| **Colaboración con el cliente** | Negociación de contratos |
| **Respuesta ante el cambio**    | Seguimiento de un plan   |

Estos valores no niegan la importancia de los procesos, la documentación o la planificación, sino que reordenan las prioridades. En la práctica, esto significa que un equipo ágil puede tener documentación, pero no la convierte en un fin en sí mismo; puede tener un plan, pero lo ajusta cuando la realidad lo exige.

### 2.2 Los doce principios ágiles

Los doce principios que acompañan al Manifiesto operacionalizan estos valores:

1. **Satisfacción del cliente** mediante entrega temprana y continua de software con valor.
2. **Aceptar el cambio** de requisitos, incluso en etapas tardías del desarrollo.
3. **Entregar software funcional con frecuencia**, en ciclos cortos (semanas, no meses).
4. **Colaboración diaria** entre personas de negocio y desarrolladores.
5. **Construir proyectos en torno a individuos motivados**, dándoles confianza y apoyo.
6. **La conversación cara a cara** es el método más eficiente de comunicación.
7. **Software funcionando** como principal medida de progreso.
8. **Desarrollo sostenible**: ritmo constante e indefinido.
9. **Excelencia técnica** y buen diseño mejoran la agilidad.
10. **Simplicidad**: maximizar el trabajo no realizado es esencial.
11. **Equipos autoorganizados** generan las mejores arquitecturas y diseños.
12. **Reflexión periódica** del equipo para ajustar su comportamiento.

### 2.3 Impacto en la gestión del trabajo

Estos principios transforman la gestión de tres maneras fundamentales:

- **De la planificación predictiva a la adaptativa:** en lugar de fijar un plan detallado para meses, se planifica a corto plazo y se ajusta según el feedback. La incertidumbre se gestiona mediante iteraciones cortas, no mediante documentación exhaustiva.
- **De la jerarquía a la autoorganización:** el equipo decide cómo hacer su trabajo. El liderazgo se convierte en facilitación y eliminación de impedimentos, no en asignación de tareas.
- **De la medición de esfuerzo a la medición de valor:** el progreso se mide por software funcionando y valor entregado al usuario, no por horas invertidas o documentos generados.

---

## 3. Panorama de Marcos Ágiles

### 3.1 Scrum

Scrum es un marco ligero para gestionar desarrollo complejo mediante entregas iterativas e incrementales. Se estructura en torno a **3 roles, 5 eventos y 3 artefactos**. Es especialmente útil cuando:

- Existe un **Product Backlog** relativamente estable y priorizable.
- Se trabaja con **plazos definidos** por las partes interesadas (aunque el alcance pueda ajustarse).
- El equipo puede comprometerse con **sprints de duración fija** (generalmente de 2 a 4 semanas).
- Se requiere **predictibilidad** y la organización valora la transparencia y la inspección periódica.

### 3.2 Kanban

Kanban es un método visual de gestión del flujo de trabajo que permite optimizar y mejorar continuamente la entrega visualizando tareas, limitando el trabajo en progreso (WIP) y centrándose en la eficiencia del flujo. Es la elección natural cuando:

- El trabajo llega de forma **continua e impredecible** (alta variabilidad, trabajo por tickets).
- No existen **plazos fijos** ni sprints, sino un flujo constante de entrada.
- El equipo necesita **flexibilidad para repriorizar** en cualquier momento.
- El cuello de botella o la **acumulación de trabajo** es un problema recurrente.

### 3.3 Design Thinking

Design Thinking no es un marco de gestión de proyectos, sino un **enfoque de innovación centrado en el ser humano** para resolver problemas complejos. Sus cinco fases (Empatizar, Definir, Idear, Prototipar, Probar) buscan comprender profundamente al usuario antes de construir soluciones. Es la elección cuando:

- El **problema no está bien definido** o no se comprende al usuario.
- Se necesita **innovación disruptiva**, no solo optimización incremental.
- Se requiere **validar supuestos** sobre necesidades del usuario antes de invertir en desarrollo.
- El equipo busca **reducir el riesgo de construir lo incorrecto** (producto que nadie necesita).

### 3.4 Comparación rápida

|      Criterio      |               Scrum               |              Kanban               |          Design Thinking          |
|--------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| **Enfoque**        | Iteraciones con sprints           | Flujo continuo                    | Innovación centrada en el usuario |
| **Cadencia**       | Sprints de duración fija          | Continua                          | Iterativa por fases               |
| **Cambios**        | No durante el sprint              | En cualquier momento              | Continuos según feedback          |
| **Métricas clave** | Velocity, burndown                | Lead time, cycle time, throughput | Validación de prototipos          |
| **Ideal para**     | Backlog estable, plazos definidos | Alta variabilidad, tickets        | Problemas mal definidos           |

---

## 4. Ventajas y Riesgos de los Enfoques Ágiles

|                        Beneficio                         |                          Limitación / Riesgo                              |                   Trade-off típico                    |
|----------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------|
| Entrega temprana y frecuente de valor al usuario         | Puede generar **fatiga de ceremonias** si no se adapta al contexto        | Más reuniones a cambio de mayor transparencia         |
| Adaptabilidad al cambio de requisitos                    | **Menor predictibilidad** de fechas y alcance a largo plazo               | Flexibilidad vs. certeza de entrega                   |
| Mayor satisfacción del cliente por colaboración continua | Requiere **cliente disponible y comprometido** durante todo el proyecto   | Involucramiento constante vs. disponibilidad limitada |
| Equipos autoorganizados y motivados                      | **Resistencia cultural** en organizaciones jerárquicas                    | Autonomía vs. control directivo                       |
| Mejora continua mediante retrospectivas                  | Sin disciplina, las retrospectivas se vuelven **rutinarias y sin acción** | Reflexión vs. acción concreta                         |
| Transparencia en el progreso                             | Riesgo de **manipulación de métricas** (gaming)                           | Métricas honestas vs. presión por resultados          |
| Simplicidad y foco en lo esencial                        | Puede subestimar **requisitos no funcionales** o deuda técnica            | Velocidad vs. calidad técnica                         |

---

## 5. Scrum: Marco de Trabajo Iterativo

### 5.1 Conceptos Base

**Propósito:** Scrum es un marco ligero que ayuda a personas, equipos y organizaciones a generar valor mediante soluciones adaptativas para problemas complejos. No es un proceso prescriptivo: define roles, eventos y artefactos mínimos, y espera que los equipos adapten los detalles a su contexto.

**Pilares de Scrum:**
- **Transparencia:** todo el trabajo es visible para el equipo.
- **Inspección:** los artefactos y el progreso se examinan regularmente.
- **Adaptación:** cuando se detecta una desviación, se ajusta lo antes posible.

**Valores de Scrum:** Compromiso, Coraje, Foco, Apertura y Respeto.

**Cuándo usarlo:** cuando se trabaja en productos complejos con requisitos cambiantes, se necesita entregar valor incrementalmente y el equipo puede comprometerse con iteraciones de duración fija. Es menos adecuado para trabajo de soporte o mantenimiento continuo (donde Kanban brilla) o para problemas que requieren exploración profunda del usuario (donde Design Thinking es más apropiado).

### 5.2 Roles

#### Product Owner (PO)

**Responsabilidad principal:** maximizar el valor que el producto genera para usuarios, clientes y negocio. Es el único responsable de gestionar el **Product Backlog**.

**Funciones clave:**
- Definir la visión del producto y priorizar el backlog según valor.
- Escribir historias de usuario con criterios de aceptación claros.
- Tomar decisiones de trade-off sobre alcance, presupuesto y plazo.
- Aceptar o rechazar trabajo según la Definition of Done.

**Errores frecuentes:**
- Omitir el refinamiento del backlog y llegar a la planificación con requisitos vagos.
- Delegar la priorización en comités o múltiples stakeholders.
- No decir "no" a solicitudes fuera de alcance.
- Compartir el rol entre varias personas, generando conflictos de decisión.

#### Scrum Master (SM)

**Responsabilidad principal:** facilitar el proceso Scrum y eliminar los impedimentos que bloquean al equipo.

**Funciones clave:**
- Asegurar que los eventos Scrum se lleven a cabo de forma efectiva y productiva.
- Coach al equipo y a la organización en la adopción de Scrum.
- Proteger al equipo de interrupciones externas.
- Facilitar la remoción de impedimentos.

**Errores frecuentes:**
- Actuar como **jefe técnico** o líder de equipo en lugar de facilitador.
- Convertirse en **intermediario** entre el PO y el equipo, perdiendo transparencia.
- No tener autoridad real para eliminar impedimentos organizacionales.
- Asumir simultáneamente el rol de PO y SM en el mismo equipo.

#### Development Team (Developers)

**Responsabilidad principal:** entregar un Incremento funcional al final de cada Sprint.

**Funciones clave:**
- Estimar y planificar el trabajo del Sprint.
- Autoorganizarse para cumplir el Sprint Goal.
- Crear y mantener el Sprint Backlog.
- Asegurar la calidad mediante la Definition of Done.

**Errores frecuentes:**
- **No autoorganizarse**: esperar que alguien externo asigne las tareas.
- **Subestimar sistemáticamente** el esfuerzo necesario.
- Trabajar de forma aislada en lugar de colaborar.
- Ignorar la deuda técnica para cumplir con el Sprint Goal.

### 5.3 Artefactos

#### Product Backlog

**Definición:** lista priorizada y emergente de todo lo que puede necesitar el producto. Es la fuente única de trabajo para el equipo.

**Criterios de calidad:**
- **Priorizado por valor**: los ítems más valiosos primero.
- **Refinado**: los ítems del próximo Sprint deben ser claros y estimables.
- **Granularidad adecuada**: épicas descompuestas en historias manejables.
- **Estimado por el equipo**: no impuesto por el PO.

#### Sprint Backlog

**Definición:** subconjunto del Product Backlog seleccionado para el Sprint, junto con el plan de acción para entregarlo.

**Criterios de calidad:**
- **Coherente con el Sprint Goal**: cada ítem contribuye al objetivo del Sprint.
- **Visible para todo el equipo**: actualizado diariamente.
- **Propiedad del equipo**: el equipo lo posee y lo ajusta.

#### Increment

**Definición:** suma de todos los ítems completados durante el Sprint, en estado "Done" y funcional.

**Criterios de calidad:**
- **Potencialmente desplegable**: debe funcionar de forma independiente.
- **Cumple la Definition of Done**: no hay ítems a medias.
- **Integrado**: no es una colección de piezas sueltas.

#### Definition of Done vs. Criterios de Aceptación

|     Aspecto     |             Definition of Done (DoD)              |                 Criterios de Aceptación                  |
|-----------------|---------------------------------------------------|----------------------------------------------------------|
| **Ámbito**      | Aplica a **todo** el Incremento                   | Aplica a **una** historia o ítem específico              |
| **Propósito**   | Definir qué significa "terminado"                 | Definir qué significa "correcto"                         |
| **Autor**       | El equipo Scrum en conjunto                       | Product Owner, con input del equipo                      |
| **Estabilidad** | Relativamente estable, evoluciona                 | Cambia por historia                                      |
| **Ejemplo**     | "Código probado, revisado, desplegado en staging" | "El usuario puede iniciar sesión con email y contraseña" |

### 5.4 Eventos

|          Evento          |                             Objetivo                            |                  Duración sugerida                |                            Antipatrón típico                        |
|--------------------------|-----------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------------------------|
| **Sprint**               | Contenedor de todos los demás eventos; generar Incremento       | 2–4 semanas                                       | Sprints demasiado largos o que no producen Incremento funcional     |
| **Sprint Planning**      | Definir el Sprint Goal y seleccionar ítems del backlog          | 2 horas por semana de Sprint (máx. 8h para 1 mes) | Convertirse en una sesión de microgestión donde el PO asigna tareas |
| **Daily Scrum**          | Inspeccionar el progreso hacia el Sprint Goal y adaptar el plan | 15 minutos                                        | Convertirse en una reunión de estatus para el manager               |
| **Sprint Review**        | Inspeccionar el Incremento y adaptar el Product Backlog         | 1 hora por semana de Sprint (máx. 4h)             | Convertirse en una demo sin feedback real del stakeholder           |
| **Sprint Retrospective** | Inspeccionar el proceso y definir mejoras                       | 45 min por semana de Sprint (máx. 3h)             | No generar acciones concretas; quejas sin solución                  |

**Antipatrones generales en eventos:**
- **Daily como reporte:** cada miembro responde al SM en lugar de coordinar con el equipo.
- **Review como demo unidireccional:** los stakeholders no participan ni dan feedback.
- **Retrospective sin seguimiento:** se identifican problemas pero no se implementan mejoras.

### 5.5 Métricas

#### Velocity

**Definición:** cantidad promedio de trabajo (en story points) completado por el equipo en un Sprint.

**Cómo interpretarla:** ayuda a predecir cuánto trabajo puede asumir el equipo en futuros Sprints. Es una herramienta de **planificación**, no de evaluación de desempeño.

**Cómo NO usarla:** nunca comparar velocity entre equipos (los puntos son relativos a cada equipo). No usar como métrica de productividad individual ni como objetivo a aumentar artificialmente.

#### Burndown Chart

**Definición:** gráfico que muestra el trabajo restante (eje Y) a lo largo del tiempo (eje X) durante un Sprint.

**Cómo interpretarla:** una línea descendente estable indica buen ritmo. Una línea plana seguida de una caída abrupta sugiere trabajo "casi terminado" que se cierra al final, lo que puede indicar problemas de flujo o de Definition of Done.

**Cómo NO usarla:** no usar para presionar al equipo a "quemar" más rápido. No comparar burndowns entre sprints sin considerar cambios en el alcance.

#### Work in Progress (WIP)

**Definición:** cantidad de trabajo iniciado pero no terminado en un momento dado.

**Cómo interpretarla:** un WIP elevado indica multitarea, cambios de contexto frecuentes y riesgo de cuellos de botella. Limitar el WIP mejora el flujo y reduce el tiempo de entrega.

**Cómo NO usarla:** no usar el WIP como excusa para no iniciar trabajo urgente. No ignorar el WIP en la planificación del Sprint.

> **Ley de Little:** `Throughput = WIP / Cycle Time`. Reducir el WIP es la forma más fiable de mejorar la entrega.

---

## 6. Kanban: Gestión Visual del Flujo

### 6.1 Fundamentos: Principios y Prácticas

Kanban se basa en seis prácticas generales que transforman el comportamiento del equipo:

1. **Visualizar el trabajo:** hacer visible el flujo mediante un tablero con columnas que representan estados del proceso. Cada tarjeta es una unidad de trabajo.

2. **Limitar el WIP:** establecer límites explícitos en cada columna. Esto evita la sobrecarga, reduce el multitasking y revela cuellos de botella.

3. **Gestionar el flujo:** medir y optimizar el movimiento del trabajo a través del sistema. Se busca un flujo continuo, no recursos al 100% de utilización.

4. **Hacer las políticas explícitas:** definir y visibilizar acuerdos sobre cómo se gestiona el trabajo: criterios de entrada/salida de columnas, clases de servicio, reglas de priorización.

5. **Implementar bucles de retroalimentación:** establecer cadencias de revisión (diaria, semanal, mensual) para inspeccionar el flujo y ajustar.

6. **Mejorar evolutivamente:** cambiar el sistema de forma incremental, basándose en datos y experimentación, no en grandes transformaciones.

**Valores de Kanban:** transparencia, respeto, equilibrio, colaboración, orientación al cliente, flujo, liderazgo, entendimiento y acuerdo.

### 6.2 Tablero Kanban para un Equipo de Desarrollo

**Propuesta de columnas:**

|     Columna     | Límite WIP sugerido |                              Justificación                             |
|-----------------|---------------------|------------------------------------------------------------------------|
| **Backlog**     | Sin límite          | Es una cola de entrada, no trabajo activo                              |
| **Ready**       | 5–8 ítems           | Suficientes para 1–2 días de trabajo; evita acumulación excesiva       |
| **In Progress** | 3–4 ítems           | Número de desarrolladores o pares; permite colaboración sin multitarea |
| **Code Review** | 2–3 ítems           | Cuello de botella frecuente; limitarlo fuerza a priorizar revisiones   |
| **Testing**     | 2–3 ítems           | Evita que se acumule trabajo sin validar                               |
| **Done**        | Sin límite          | Los ítems completados se retiran periódicamente                        |

**Razonamiento de los límites:**
- El WIP de "In Progress" debe reflejar la **capacidad real** del equipo, no el número de personas. Con 5 desarrolladores, un límite de 3–4 fomenta la colaboración en lugar del trabajo aislado.
- Los límites en "Code Review" y "Testing" son críticos porque son las etapas donde el trabajo suele estancarse. Un límite bajo obliga al equipo a **"swarmear"** (varios miembros ayudan a desatascar).
- Los límites se ajustan empíricamente: si el equipo constantemente los excede, es señal de que son demasiado bajos o de que hay un problema de capacidad.

### 6.3 Métricas de Flujo

#### Lead Time

**Definición:** tiempo total desde que un ítem es solicitado (entra al backlog) hasta que se entrega.

**Interpretación:** mide la experiencia del cliente. Un lead time alto indica que el trabajo espera demasiado antes de empezar o que el proceso es lento.

#### Cycle Time

**Definición:** tiempo desde que un ítem comienza a trabajarse (entra en "In Progress") hasta que se completa.

**Interpretación:** mide la eficiencia del proceso productivo. Es más útil que el lead time para diagnosticar problemas internos. Se debe analizar como **distribución**, no como promedio, para entender la variabilidad.

#### Throughput

**Definición:** número de ítems completados por unidad de tiempo (semana, sprint, mes).

**Interpretación:** mide la capacidad de entrega del sistema. Es el complemento natural del cycle time: si el throughput baja, el cycle time sube (Ley de Little).

#### Diagrama de Flujo Acumulado (CFD)

**Definición:** gráfico que muestra, en el eje Y, el número acumulado de ítems en cada estado del flujo, a lo largo del tiempo (eje X).

**Cómo leerlo:**
- **Bandas anchas** indican acumulación de trabajo en ese estado (cuello de botella).
- **Bandas que se ensanchan** indican que el WIP está creciendo más rápido que el throughput.
- **La pendiente de la banda superior** (Done) indica el throughput.
- **La distancia vertical** entre la banda de entrada (Backlog) y la de Done es el WIP total.
- Un CFD con bandas **paralelas y estables** indica un flujo saludable.

### 6.4 Políticas y Clases de Servicio

**Políticas explícitas** son acuerdos visibles que definen cómo se gestiona el trabajo: criterios de entrada/salida, reglas de priorización, procedimientos de escalado.

**Clases de servicio** son categorías de trabajo con políticas diferenciadas según el impacto del retraso:

|    Clase de Servicio    |                    Descripción                   |              Ejemplo           |                    Política típica                      |
|-------------------------|--------------------------------------------------|--------------------------------|---------------------------------------------------------|
| **Expedite**            | Urgencia máxima; impacto inmediato si se retrasa | Bug crítico en producción      | Límite WIP de 1; salta la cola; se asigna de inmediato  |
| **Fixed Delivery Date** | Fecha de entrega comprometida e inamovible       | Lanzamiento regulatorio        | Se planifica hacia atrás desde la fecha; prioridad alta |
| **Standard**            | Trabajo normal, priorizado por valor             | Nuevas funcionalidades         | Flujo normal, FIFO con priorización por valor           |
| **Intangible**          | Trabajo de bajo impacto inmediato                | Refactorización, deuda técnica | Se planifica cuando hay capacidad; puede posponerse     |

**Cuándo aplicarlas:** cuando el equipo recibe trabajo de distintas fuentes con diferentes niveles de urgencia y no puede tratarlo todo por igual. Las clases de servicio permiten **optimizar el flujo sin sacrificar la respuesta a lo urgente**.

### 6.5 ¿Cuándo usar Kanban vs. otros enfoques?

|                            Situación                            |                    Enfoque recomendado                |
|-----------------------------------------------------------------|-------------------------------------------------------|
| Trabajo por tickets, llegada continua e impredecible            | **Kanban**                                            |
| Alta variabilidad en el tamaño y tipo de tareas                 | **Kanban**                                            |
| Equipo de soporte, mantenimiento u operaciones                  | **Kanban**                                            |
| Backlog estable, plazos definidos, necesidad de predictibilidad | **Scrum**                                             |
| Problema mal definido, necesidad de exploración del usuario     | **Design Thinking** (complementario a Scrum o Kanban) |
| Proyecto con hitos regulatorios y necesidad de documentación    | **Scrum** (con adaptaciones) o enfoque híbrido        |

---

## 7. Design Thinking: Innovación Centrada en el Usuario

### 7.1 Visión General

Design Thinking es un enfoque de innovación que combina empatía, creatividad y racionalidad para resolver problemas complejos. A diferencia de los marcos ágiles de gestión (Scrum, Kanban), DT se centra en **descubrir qué construir**, no en cómo gestionar su construcción.

**Principios de Design Thinking:**
- **Empatía con el usuario:** comprender necesidades, motivaciones y frustraciones reales.
- **Colaboración interdisciplinaria:** equipos diversos aportan perspectivas complementarias.
- **Experimentación temprana:** prototipar para aprender, no para entregar.
- **Iteración:** las ideas se refinan mediante ciclos de feedback.
- **Mentalidad de "sí, y…":** construir sobre las ideas de otros en lugar de descartarlas.

**Encaje con el desarrollo de software:** DT se aplica típicamente en la **fase de descubrimiento** del producto, antes o en paralelo con el desarrollo. Ayuda a definir el Product Backlog de Scrum o las épicas de Kanban con mayor precisión. Un equipo que practica DT reduce el riesgo de construir funcionalidades que nadie necesita.

### 7.2 Fases de Design Thinking

|      Fase      |                   Objetivo                    |                       Técnicas sugeridas                      |               Entregables mínimos               |
|----------------|-----------------------------------------------|---------------------------------------------------------------|-------------------------------------------------|
| **Empatizar**  | Comprender profundamente al usuario           | Entrevistas, observación directa, focus groups, encuestas     | Mapas de empatía, notas de campo                |
| **Definir**    | Sintetizar insights en un problema accionable | Personas, mapas de viaje, declaraciones POV, 5 Whys           | Declaración de problema, persona principal      |
| **Idear**      | Generar un amplio rango de soluciones         | Brainstorming, Crazy 8s, mapas mentales, SCAMPER              | Lista priorizada de ideas, bocetos conceptuales |
| **Prototipar** | Materializar ideas para aprender              | Wireframes, mockups, prototipos de baja/alta fidelidad        | Prototipo navegable o boceto funcional          |
| **Probar**     | Validar supuestos con usuarios reales         | Pruebas de usabilidad, entrevistas de validación, observación | Informe de hallazgos, lista de iteraciones      |

**Nota clave:** las fases no son lineales. Es común volver de "Probar" a "Definir" o de "Prototipar" a "Idear" según lo que se aprenda.

### 7.3 Mini-Caso: Rediseño del Proceso de Inscripción de Materias

**Contexto:** Una universidad quiere mejorar la experiencia de inscripción de materias, que actualmente genera frustración en los estudiantes por filas virtuales, caídas del sistema y falta de claridad sobre la oferta.

#### Fase 1: Empatizar
**Actividades:** 12 entrevistas a estudiantes de distintos semestres; observación de sesiones de inscripción en tiempo real; encuesta a 80 estudiantes.
**Hallazgos clave:** los estudiantes no saben cuándo se abren los cupos; el sistema se cae por saturación; no hay forma de saber qué materias son obligatorias vs. optativas; la información está dispersa en PDFs y correos.

#### Fase 2: Definir
**Actividades:** síntesis de hallazgos en un mapa de empatía; construcción de dos personas (estudiante de primer semestre y estudiante de último semestre); declaración POV: "Los estudiantes necesitan claridad sobre la oferta y disponibilidad de materias en tiempo real para inscribirse sin ansiedad ni pérdida de tiempo".
**Entregable:** declaración de problema validada con el equipo.

#### Fase 3: Idear
**Actividades:** sesión de brainstorming con 15 participantes (estudiantes, personal administrativo, desarrolladores); técnica Crazy 8s para generar 40+ ideas; agrupación por afinidad y votación.
**Ideas seleccionadas:** panel de disponibilidad en tiempo real; sistema de notificaciones push cuando se abre un cupo; recomendador de materias según avance curricular; inscripción por bloques con prioridad por semestre.

#### Fase 4: Prototipar
**Prototipo de baja fidelidad (texto):**

```
┌─────────────────────────────────────┐
│  MI INSCRIPCIÓN          [Perfil]   │
├─────────────────────────────────────┤
│  📅 Próxima apertura: 15 nov 08:00  │
│  ⏰ Tiempo restante: 2d 14h         │
├─────────────────────────────────────┤
│  RECOMENDADAS PARA TI               │
│  ┌─────────────────────────────┐    │
│  │ Cálculo III        [ABIERTA]│    │
│  │ Cupos: 12/40                │    │ 
│  │ Horario: L-M 10:00-12:00    │    │
│  └─────────────────────────────┘    │
│  ┌─────────────────────────────┐    │
│  │ Física II            [LLENA]│    │
│  │ Lista de espera: 5          │    │
│  └─────────────────────────────┘    │
├─────────────────────────────────────┤
│ 🔔 Notifícame cuando se abra cupo   │
└─────────────────────────────────────┘
```

**Descripción del prototipo:** pantalla de inicio que muestra la cuenta regresiva para la apertura, materias recomendadas según el avance curricular, estado de cupos en tiempo real y opción de notificación push.

#### Fase 5: Probar
**Actividades:** prueba de usabilidad con 10 estudiantes; tareas: encontrar una materia obligatoria, inscribirse en una optativa con cupo, activar notificación. **Resultados:** los estudiantes comprendieron el flujo en menos de 2 minutos; sugirieron mostrar el prerrequisito de cada materia; varios pidieron poder inscribirse directamente desde la notificación.
**Iteración:** se agregó la visualización de prerrequisitos y un botón de "Inscribir" en la notificación.

### 7.4 Relación con SDLC/Ágil

Design Thinking y los marcos ágiles de gestión son **complementarios, no competidores**:

- **DT reduce el riesgo de construir lo incorrecto.** Mientras Scrum y Kanban optimizan la eficiencia del desarrollo, DT asegura que el equipo esté construyendo algo que el usuario realmente necesita. Un Product Backlog lleno de funcionalidades que nadie usará es un desperdicio, sin importar cuán eficientemente se desarrolle.

- **DT alimenta el Product Backlog.** Los hallazgos de la fase de "Probar" se convierten en historias de usuario priorizadas para Scrum, o en ítems de trabajo para Kanban.

- **DT y Scrum/Kanban comparten valores.** Ambos priorizan la entrega de valor, la iteración y el feedback. Un equipo puede practicar DT durante la fase de descubrimiento de un producto y luego usar Scrum para su construcción.

- **Articulación práctica:**
  1. **Descubrimiento (DT):** empatizar, definir, idear, prototipar, probar → genera un Product Backlog priorizado y validado.
  2. **Construcción (Scrum):** sprints de 2–4 semanas para desarrollar el backlog → genera Incrementos funcionales.
  3. **Sostenimiento (Kanban):** gestión del flujo continuo de tickets, bugs y mejoras → mantiene el producto vivo.

---

## 8. Conclusiones

### Reflexión sobre aplicaciones en el contexto académico y profesional

La agilidad no es una fórmula mágica, sino un conjunto de principios que requieren disciplina, contexto y adaptación. A lo largo de este documento, queda claro que **no existe un marco superior a otro**: Scrum, Kanban y Design Thinking responden a problemas distintos.

**En el contexto académico,** por ejemplo, un equipo de estudiantes desarrollando un proyecto de semestre puede beneficiarse de Scrum para organizar sprints de 2 semanas, pero también de Design Thinking para comprender al usuario antes de escribir código. En mi experiencia, la mayor tentación es saltar directamente a la solución sin validar el problema. Design Thinking es el antídoto contra esa tendencia.

**En el contexto profesional,** la elección del marco depende del tipo de trabajo:
- Equipos de producto con roadmap definido → Scrum.
- Equipos de soporte o plataforma con tickets continuos → Kanban.
- Equipos de innovación o nuevos productos → Design Thinking + Scrum.

**Lecciones clave:**
1. **La agilidad es una mentalidad, no un conjunto de ceremonias.** Adoptar Scrum sin interiorizar sus valores produce "Scrum zombie": reuniones sin propósito y métricas sin significado.
2. **Las métricas deben usarse para mejorar, no para juzgar.** Velocity, lead time y burndown son herramientas de diagnóstico, no armas de evaluación de desempeño.
3. **El mayor riesgo es construir lo incorrecto.** Design Thinking, combinado con la entrega incremental de Scrum o Kanban, es la mejor defensa contra ese riesgo.
4. **La mejora es evolutiva, no revolucionaria.** Kanban enseña que los cambios pequeños y sostenidos son más efectivos que las transformaciones radicales.

---

## 9. Referencias

1. **Atlassian.** *Manifiesto Ágil.* https://www.atlassian.com/es/agile/manifesto
2. **Schwaber, K. & Sutherland, J.** (2020). *The Scrum Guide.* https://scrumguides.org
3. **Deckary.** (2026). *Scrum Framework: Complete Guide to Roles, Ceremonies, and Artifacts.* https://deckary.com/blog/scrum-framework-guide
4. **Atlassian.** *¿Qué es Kanban en la gestión de proyectos?* https://www.atlassian.com/es/agile/kanban
5. **Aha!** (2025). *The Complete Guide to Agile Metrics for PMs and Engineers.* https://www.aha.io/roadmapping/guide/agile/agile-metrics
6. **Sonowal, G.** (2025). *Phases of Design Thinking.* Taylor & Francis. https://www.taylorfrancis.com
7. **Kanban University.** *La Guía Oficial del Método Kanban.* https://kanban.university
8. **Project Management Institute (PMI).** *Agile Practice Guide.*
9. **Vacanti, D.** (2015). *Actionable Agile Metrics for Predictability.*
10. **Rohde, C. et al.** (2019). *Everything flows: Kanban and Scrum as an innovation tool in Design Thinking.* RWTH Aachen. https://publications.rwth-aachen.de