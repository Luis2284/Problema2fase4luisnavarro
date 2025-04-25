# =====================================
# Nombre del estudiante: Luis Navarro Masson
# Grupo: 81
# Problema 2 - Cálculo de pago en una clínica según código de procedimiento
# Código fuente: autoría propia
# Este programa utiliza funciones para validar un código de paciente,
# identificar el tipo de paciente, el procedimiento, calcular el costo base,
# aplicar descuentos o recargos y determinar el pago final.
# =====================================

def validar(codigo):
    """Valida que el código tenga 5 dígitos."""
    return 1 if 10000 <= codigo <= 99999 else 0

def tipo(codigo):
    """Retorna tipo de paciente según primer dígito."""
    primer_digito = int(str(codigo)[0])
    if primer_digito == 1:
        return "AFILIADO"
    elif primer_digito == 2:
        return "PARTICULAR"
    else:
        return "DESCONOCIDO"

def servicio(codigo):
    """Retorna el nombre del procedimiento según segundo dígito."""
    procedimientos = {
        1: "RADIOGRAFÍA",
        2: "ECOGRAFÍA",
        3: "LABORATORIO",
        4: "CONSULTA EXTERNA",
        5: "CONSULTA ESPECIALIZADA"
    }
    segundo_digito = int(str(codigo)[1])
    return procedimientos.get(segundo_digito, "SERVICIO DESCONOCIDO")

def costo(nombre_servicio):
    """Retorna el costo base según el servicio."""
    valores = {
        "RADIOGRAFÍA": 30000,
        "ECOGRAFÍA": 35000,
        "LABORATORIO": 25000,
        "CONSULTA EXTERNA": 40000,
        "CONSULTA ESPECIALIZADA": 80000
    }
    return valores.get(nombre_servicio, 0)

def descuReca(codigo, tipo_paciente, costo_base):
    """Calcula el descuento o recargo según reglas."""
    digitos = [int(d) for d in str(codigo)]
    suma = sum(digitos[2:])  # tercer, cuarto y quinto dígito
    if suma % 2 == 0:  # par
        return -0.15 * costo_base if tipo_paciente == "AFILIADO" else 0.15 * costo_base
    else:  # impar
        return -0.25 * costo_base if tipo_paciente == "AFILIADO" else 0.25 * costo_base

def pago(costo_base, ajuste):
    """Calcula el pago final."""
    return costo_base + ajuste

def principal():
    try:
        codigo = int(input("Ingrese el código de 5 dígitos del procedimiento: "))
    except ValueError:
        print("Error: El código debe ser un número entero.")
        return

    if validar(codigo) == 0:
        print("Código inválido. Debe tener exactamente 5 dígitos.")
        return

    tipo_p = tipo(codigo)
    nombre_servicio = servicio(codigo)
    costo_base = costo(nombre_servicio)
    ajuste = descuReca(codigo, tipo_p, costo_base)
    total = pago(costo_base, ajuste)

    print(f"Tipo de paciente: {tipo_p}")
    print(f"Servicio: {nombre_servicio}")
    print(f"Costo base: ${costo_base}")
    print(f"{'Descuento' if ajuste < 0 else 'Recargo'} aplicado: ${abs(ajuste):.2f}")
    print(f"Total a pagar: ${total:.2f}")

# Ejecutar función principal
if __name__ == "__main__":
    principal()
