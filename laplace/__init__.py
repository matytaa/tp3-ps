from sympy.abc import s,l
from sympy import *
import parser

t = symbols('t', real=true, positive=true)
s = symbols('s', real=true, positive=true)

class ecuaciones_diferenciales:
    co_derivada = 0
    coeficiente = 0
    funcion_t = 0
    condicion_inicial = 0

    def __init__(self, coeficiente_derivada, coeficiente_funcion, termino_libre, cond_inicial):
        self.co_derivada = eval(coeficiente_derivada)
        self.coeficiente = eval(coeficiente_funcion)
        self.funcion_t = eval(termino_libre)
        self.condicion_inicial = eval(cond_inicial)


    def transformar(self, funcion, variable, variable_transformada):
        transformada, algo, algo2 = laplace_transform(funcion, variable, variable_transformada)
        return transformada

    def transformar_funcion(self, coeficiente, variable_transformada):
        return coeficiente*variable_transformada

    def laplace_con_derivada_de_primer_orden(self, coeficiente_de_la_derivada, condicion_inicial):
        return (s*l - condicion_inicial) * coeficiente_de_la_derivada


    def resolver(self):
        transformada_derivada = self.laplace_con_derivada_de_primer_orden(self.co_derivada, self.condicion_inicial)
        print("\nderivada x")
        pprint(transformada_derivada)

        transformada_x = self.transformar_funcion(self.coeficiente, l)
        print("\nx")
        pprint(transformada_x)


        transformada_t = self.transformar(self.funcion_t, t, s)
        print("\nt")
        pprint(transformada_t)

        pprint("fraccion")
        suma = Add(transformada_derivada, transformada_x, (-1) * transformada_t)
        pprint(suma)
        print("\n")
        print("\nbusco valor de l")
        valor_l = solve(suma, l)
        valor_l = simplify(valor_l)
        pprint(valor_l)

        inversas = []
        for raiz in valor_l:
            inversa = inverse_laplace_transform(raiz, s, t).evalf().simplify()
            inversas.append(inversa)

        resultado = 0
        for inversa2 in inversas:
            resultado = resultado + inversa2

        pprint("\nresultado")
        pprint(simplify(resultado))
        return simplify(resultado)