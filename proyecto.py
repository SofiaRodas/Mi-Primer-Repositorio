nombre_proyecto = 'LocalUp'
descripcion = 'LocalUp resuelve la dificultad de encontrar eventos, lugares y planes confiables en la ciudad al centralizar recomendaciones, reseñas y actividades en una sola plataforma. Además, ayuda a negocios y organizadores a ganar visibilidad e interactuar directamente con su comunidad.'
tecnologias = ['HTML', 'Python', 'MySQL']
integrantes =  ['Sofia Rodas', 'Estefania Restrepo', 'Miguel Angel Castro']
funcionalidades = ['Login', 'Interactuar', 'Comentar', 'Reseñas']

def mostrar_info():
    print(f'Proyecto: {nombre_proyecto}')
    print(f'Descripción: {descripcion}')

    print(f'Equipo: {", ".join(integrantes)}')
    print(f'Tecnologías: {", ".join(tecnologias)}')
    print('Funcionalidades:')
    
    for f in funcionalidades:
        print(f' - {f}')
mostrar_info()