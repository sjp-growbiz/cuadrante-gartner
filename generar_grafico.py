import matplotlib.pyplot as plt

# Definir las estrategias con sus respectivos niveles de ahorro y dificultad (ahora de 1 a 100, replanteados)
# X = Nivel de Ahorro
# Y = Complejidad de Implementacion
'''
estrategias = [
    ("Apagar Recursos Inactivos", 20, 20),
    ("Utilizar Instancias Reservadas", 90, 5),
    ("Uso de Instancias Spot", 90, 75),
    ("Right-Sizing", 80, 60),
    ("Eliminar Volúmenes No Utilizados", 40, 12),
    ("Utilizar Servicios Gestionados", 90, 25),
    ("Optimización de Almacenamiento", 70, 30),
    ("Monitoreo y Alerta de Costos", 80, 10),
    ("Consolidación de Cuentas", 20, 40),
    ("Implementación de Políticas de Auto-Scaling", 80, 70),
    ("Optimización de Arquitectura", 85, 75),
    ("Reserva de Capacidad de Planificación", 73, 40),
    ("Reducción de Tráfico de Datos", 77, 40),
    ("Optimización de Bases de Datos", 83, 40),
    ("Utilización de Análisis de Costos y Mejora Continua", 60, 40),
    ("Automatización de Optimización de Costos", 75, 65),
    ("Uso de AI/ML para Predicción de Costos", 40, 78),
    ("Negociación de Descuentos Personalizados", 30, 44)
]
'''
'''estrategias = [
    ("1.Uso de Spot Instances", 90, 60),
    ("2.Reserved Instances y Savings Plans", 85, 55),
    ("3.Optimización de Almacenamiento en S3", 80, 35),
    ("4.Dimensionamiento de Recursos", 75, 40),
    ("5.Autoscaling y Elasticidad", 70, 45),
    ("6.Uso de AWS Cost Explorer y AWS Budgets", 65, 10),
    ("7.Aprovechamiento de Créditos y Programas Promocionales", 60, 15),
    ("8.Uso de Arquitecturas Sin Servidor (Serverless)", 55, 50),
    ("9.Monitorización y Optimización Continua con CloudWatch", 50, 25),
    ("10.Optimización de Redes y Transferencia de Datos", 45, 30),
    ("11.Optimización de Bases de Datos", 40, 65),
    ("12.Uso de Amazon CloudFront para Distribución de Contenidos", 35, 50),
    ("13.Uso de servicios de almacenamiento eficientes como S3 One Zone-IA", 30, 35),
    ("14.Consolidación de Cuentas con AWS Organizations", 25, 40),
    ("15.Uso de instancias EC2 con menor costo", 20, 45),
    ("16.Uso de Auto Scaling Groups", 15, 40),
    ("17.Gestión de Snapshots y Backups", 10, 20),
    ("18.Uso de Servicios Gestionados", 8, 70),
    ("19.Uso de Arquitecturas Basadas en Microservicios", 5, 65),
]'''

estrategias = [
    ("1.Uso de Spot Instances", 90, 60),
    ("2.Reserved Instances y Savings Plans", 85, 55),
    ("3.Optimización de Almacenamiento en S3", 80, 35),
    ("4.Derecho a Dimensionar Recursos", 75, 40),
    ("5.Autoscaling y Elasticidad", 70, 45),
    ("6.Uso de AWS Cost Explorer y AWS Budgets", 65, 10),
    ("7.Aprovechamiento de Créditos y Programas Promocionales", 60, 15),
    ("8.Uso de Arquitecturas Sin Servidor (Serverless)", 55, 50),
   # ("Monitorización y Optimización Continua con CloudWatch", 50, 25),
   # ("Optimización de Redes y Transferencia de Datos", 45, 30),
   # ("Optimización de Bases de Datos", 40, 65),
   # ("Uso de Amazon CloudFront para Distribución de Contenidos", 35, 50),
   # ("Uso de servicios de almacenamiento eficientes como S3 One Zone-IA", 30, 35),
   # ("Consolidación de Cuentas con AWS Organizations", 25, 40),
    ("9.Uso de instancias EC2 con menor costo", 20, 45),
    ("10.Uso de Auto Scaling Groups", 15, 40),
    ("11.Gestión de Snapshots y Backups", 10, 20),
    ("12Uso de Servicios Gestionados",8, 70),
    ("13.Uso de Arquitecturas Basadas en Microservicios", 5, 65),
    #("Uso de AWS Free Tier", 3, 5),
]



# Convertir dificultad en facilidad (100 - dificultad)
estrategias_facilidad = [(nombre, ahorro, 100 - dificultad) for nombre, ahorro, dificultad in estrategias]

# Definir los ejes
x = [estrategia[2] for estrategia in estrategias_facilidad]  # Facilidad de Implementación
y = [estrategia[1] for estrategia in estrategias_facilidad]  # Nivel de Ahorro
labels = [estrategia[0] for estrategia in estrategias_facilidad]

# Crear el gráfico
plt.figure(figsize=(14, 10))
plt.scatter(x, y, color='blue')

# Añadir etiquetas a los puntos con ajustes para evitar superposición y evitar que salgan del marco
for i, label in enumerate(labels):
    if x[i] > 95:
        plt.text(x[i], y[i] + 1, label, fontsize=12, ha='left', va='bottom')
    elif y[i] > 95:
        plt.text(x[i], y[i], label, fontsize=12, ha='right', va='bottom')
    else:
        plt.text(x[i] + 15, y[i] + 1, label, fontsize=12, ha='right', va='bottom')

# Añadir títulos y etiquetas de los ejes
plt.title("Estrategias para Reducir Costos en AWS: Facilidad de Implementación vs Ahorro")
plt.xlabel("Facilidad de Implementación")
plt.ylabel("Nivel de Ahorro")

# Añadir líneas de cuadrantes
plt.axhline(y=50, color='gray', linestyle='--')
plt.axvline(x=50, color='gray', linestyle='--')

# Añadir etiquetas en cada eje
plt.text(-8, 105, 'Alto Ahorro', ha='center', va='center', fontsize=12, color='green')
plt.text(-8, 5, 'Bajo Ahorro', ha='center', va='center', fontsize=12, color='red')
plt.text(95, -5, 'Facil Impl', ha='center', va='center', fontsize=12, color='green')
plt.text(5, -5, 'Dificil Impl', ha='center', va='center', fontsize=12, color='red')

# Ajustar límites de los ejes
plt.xlim(1, 100)
plt.ylim(1, 100)

# Mostrar el gráfico sin cuadriculas y solo con líneas de cuadrantes
plt.grid(False)

# Guardar la imagen como PNG
plt.savefig("./estrategias_aws_ahorro_facilidad.png", format='png')

# Mostrar el gráfico
#plt.show()
