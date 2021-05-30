# cambiar este valor para cambiar la "definicion"
CANTIDAD_DE_PASOS_TOTALES = 3

import bpy

def blender_borrar_pantalla():
    for el in bpy.data.objects:
        bpy.data.objects.remove(el)

    
def suma(t1, t2):
    return tuple(p + q for p,q  in zip(t1,t2))
        
def mult(constante, tupla):
    return tuple(constante * t for t in tupla)


def avanzar_un_paso(inicial, anterior, paso):
    extendido = anterior * 4
    siguiente = []
    
    for i in range(len(extendido)):
        siguiente.append(suma( extendido[i], mult(2**paso, inicial[i // ( len(extendido) // 4) ]) ) )
    
    return siguiente


def generar_fractal(pasos_totales):

    inicial = [(1,1,-1),(-1,1,1),(-1,-1,-1),(1,-1,1)]

    siguiente = inicial
    for paso in range(1, pasos_totales+1):
        siguiente = avanzar_un_paso(inicial, siguiente, paso)
    
    return siguiente
            
def blender_dibujar_cubos(coords):
    for coord in coords:
        bpy.ops.mesh.primitive_cube_add(location=coord)
   

def dibujar_fractal():
    blender_borrar_pantalla()
    coords = generar_fractal(CANTIDAD_DE_PASOS_TOTALES)    
    blender_dibujar_cubos(coords)




dibujar_fractal()

##  Algunas notas de como hacer algunas cosas en blender:

#bpy.ops.mesh.primitive_cube_add(location=(0,0,0), name='carlos')

#import inspect
#inspect.getargspec(bpy.ops.mesh.primitive_cube_add)


##bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
##bpy.context.active_object.name = 'carlos';
##for i in range(len(bpy.data.objects)):
##    print(bpy.data.objects[i].name)


# borro todo antes de empezar denuevo