"""Jerarquía de sesión, revisada hoja por hoja. No cambia los motores clínicos.

Los índices se refieren a los bloques originales de primer nivel. Se verifica
su número al construir para evitar que una sección nueva cambie de lugar sola.
Las imágenes se incrustan: cada HTML conserva su funcionamiento sin conexión.
"""
from pathlib import Path
import base64
import re
from bs4 import BeautifulSoup

AQUI = Path(__file__).resolve().parent

# archivo: (número de bloques, bloques centrales en orden, entrada en una frase)
REVISION = {
 'act-brujula-de-valores': (4, [0,1], 'Lo que importa y el lugar que está teniendo en la vida cotidiana.'),
 'act-costo-de-la-lucha': (5, [0,1], 'Lo que has intentado: qué alivia en el momento y qué sucede con el tiempo.'),
 'act-por-donde-entrar': (3, [0,1,2], 'Un mapa de los seis procesos para orientar la formulación y elegir por dónde trabajar.'),
 'act-soltar-el-anzuelo': (4, [0,1], 'Un pensamiento y distintas formas de relacionarte con él. Elige una para explorar.'),
 'act-matriz': (3, [0], 'Quién y qué importa, lo que aparece por dentro y los movimientos de la vida cotidiana.'),
 'act-los-ganchos': (5, [0,1,2,3], 'Lo que engancha, lo que haces después y la dirección hacia la que quieres nadar.'),
 'act-el-cielo-y-el-clima': (4, [0,1], 'Darle espacio a lo que aparece, como el cielo al clima que lo atraviesa.'),
 'act-empujar-el-papel': (5, [0,1], 'Explora qué ocurre al empujar los pensamientos y al dejarlos junto a lo que estás haciendo.'),
 'act-quien-lleva-los-globos': (4, [0,1,2,3], 'Llevar lo que aparece mientras eliges hacia dónde dar el siguiente paso.'),
 'cft-ritmo-tranquilizador': (5, [2], 'Acompaña el movimiento con una respiración cómoda. Ajusta el ritmo si lo necesitas.'),
 'cft-espacio-de-respiracion': (4, [0], 'Reconocer lo que hay, atender a la respiración y ampliar la atención al cuerpo.'),
 'cft-pausa-de-autocompasion': (5, [0,1,2], 'Encuentra unas palabras y un gesto para acompañarte en un momento difícil.'),
 'cft-el-yo-compasivo': (5, [0,1], 'Ensaya una manera cálida, sabia y valiente de acompañar a quien está pasándolo mal.'),
 'crisis-plan-de-seguridad': (8, list(range(8)), 'Un plan concreto y accesible para atravesar una crisis, elaborado junto con quien acompaña.'),
 'crisis-surfear-el-impulso': (3, [0,1], 'Reconoce el impulso y observa cómo cambia mientras eliges qué hacer.'),
 'crisis-importancia-y-confianza': (4, [0,1,2], 'Un cambio, dos reglas y las razones propias que aparecen al conversar sobre ellas.'),
 'dbt-analisis-en-cadena': (5, [0,1,2], 'Reconstruye una situación: qué venía pasando, qué ocurrió después y qué consecuencias tuvo.'),
 'dbt-tarjeta-de-crisis': (7, [0,1,2,3,4], 'Ubica lo que está ocurriendo y explora las habilidades para atravesar el momento.'),
 'dbt-verificar-los-hechos': (6, [0,1,2,3,4,5], 'Una emoción, una situación y la diferencia entre lo que ocurrió y su interpretación.'),
 'dbt-pedir-y-decir-no': (7, [0,1], 'En esta conversación, ¿qué quieres conseguir, cuidar o sostener?'),
 'dbt-mente-sabia': (4, [0,1,2], 'Dale un lugar a lo que dice la razón, a lo que dice la emoción y a lo que surge al escucharlas.'),
 'dbt-tarjeta-diaria': (3, [1], 'La semana a la vista: emociones, impulsos y habilidades. Elige un día para registrar o revisar.'),
 'flor-permah': (2, [0], 'Seis áreas del bienestar para mirar cómo está la vida hoy y por dónde empezar.'),
 'fortalezas-del-caracter': (2, [0], 'Elige las fortalezas que reconoces en tu vida y conversa sobre lo que representa cada una.'),
 'met-el-tablero': (4, [0,1,2], 'Las piezas que quieres que ganen, las que quieres sacar y el tablero que puede contenerlas.'),
 'met-jardin-de-valores': (4, [0,1,2,3], 'Siembra lo que importa, encuentra sus raíces y mira cómo lo has cuidado esta semana.'),
 'met-la-cuerda': (3, [0,1,2], 'Una cuerda, lo que aparece al otro lado y lo que podrías hacer con las manos libres.'),
 'met-hojas-en-el-arroyo': (4, [0,2,3], 'Pon en las hojas los pensamientos que reconoces y observa su paso por el arroyo.'),
 'met-el-bus': (5, [0,1,2], 'Una dirección importante y los pasajeros que aparecen durante el camino.'),
 'met-los-ochenta-anos': (4, [0,1,2,3], 'Personas importantes y la huella que quisieras dejar en sus vidas.'),
 'met-el-poligrafo': (3, [0,1,2], 'Explora qué ocurre cuando intentas controlar lo que estás sintiendo.'),
 'met-la-palabra-repetida': (5, [0,2,4], 'Di la palabra en voz alta al ritmo del punto. Prueba primero con «limón» y observa qué ocurre.'),
 'met-la-radio': (4, [0,1,2,3], 'Una tarea por hacer mientras la radio de la mente sigue transmitiendo.'),
 'met-el-hoyo': (3, [0,1,2], 'Lo que has estado haciendo para salir del hoyo y lo que ocurre al seguir cavando.'),
 'pp-tres-cosas-buenas': (4, [0], 'Recupera algo bueno de hoy o de ayer y explora qué hizo posible que ocurriera.'),
 'registro-de-pensamientos': (7, [0,1,2], 'Una situación concreta, lo que sentiste y lo que pasó por tu mente.'),
 'tcc-flecha-descendente': (5, [0,1], 'Parte de un pensamiento y explora qué significaría para ti que fuera cierto.'),
 'tcc-escalera-de-exposicion': (4, [0,1,2], 'Pon las situaciones en una escalera y explora con quien te acompaña cómo abordarlas.'),
 'tcc-activacion-conductual': (5, [0,1,2], 'Mira las actividades de tu semana y lo que aportan en agrado y sensación de logro.'),
 'tcc-solucion-de-problemas': (6, [1,2], 'Define una dificultad concreta y abre espacio para distintas alternativas antes de evaluarlas.'),
 'tcc-autoinstrucciones': (5, [0,1], 'Construye unas palabras propias para acompañarte antes, durante y después de una situación.'),
 'tcc-analisis-funcional': (6, [0,1,2,3], 'Un mapa de lo que sucede antes, lo que hace la persona y lo que ocurre después.'),
 'tcc-aplazar-la-preocupacion': (5, [1,2], 'Un pensamiento que aparece y distintas maneras de responder a partir de ahí.'),
 'tcc-balance-decisional': (4, [0,1], 'Dale lugar a las razones para cambiar y a las razones para seguir igual.'),
 'tcc-ventana-de-sueno': (5, [0,1,2,4], 'Revisa el diario de sueño y los antecedentes con el profesional antes de acordar una ventana.'),
 'tcc-lista-abc': (4, [0,2], 'Reúne lo pendiente y distingue qué necesita tu atención primero.'),
 'tcc-inoculacion-de-estres': (5, [0,1], 'Distingue lo que puedes cambiar y los recursos con los que cuentas para afrontarlo.'),
}

# Las escenas con preparación larga se mantienen a ancho completo.
ESCENAS_LATERALES = {'met-la-cuerda','met-hojas-en-el-arroyo','met-el-hoyo',
 'met-el-poligrafo','met-el-tablero','met-el-bus','met-la-radio',
 'met-la-palabra-repetida','act-los-ganchos','act-quien-lleva-los-globos',
 'act-el-cielo-y-el-clima','crisis-surfear-el-impulso','tcc-aplazar-la-preocupacion'}

def incrustar_imagenes(texto):
    def imagen(m):
        p = AQUI / 'imagenes' / m[1]
        return 'data:image/png;base64,' + base64.b64encode(p.read_bytes()).decode('ascii')
    return re.sub(r'\[\[imagen:([\w.-]+)\]\]', imagen, texto)

def aplicar(documento, archivo):
    nombre = Path(archivo).stem
    total, centrales, entrada = REVISION[nombre]
    # El código JS permanece byte por byte; solo se transforma el marcado.
    soup = BeautifulSoup(documento, 'html.parser')
    envoltura = soup.select_one('.envoltura')
    assert envoltura and not soup.body.has_attr('data-sesion'), archivo
    bloques = [e for e in envoltura.find_all(['section','div'], recursive=False)
               if 'barra' not in e.get('class', [])]
    assert len(bloques) == total, (archivo, len(bloques), total)
    soup.body['data-sesion'] = nombre
    sub = soup.select_one('.tapa .sub')
    if sub:
        sub.clear(); sub.append(entrada)
    fuente = soup.select_one('.tapa .fuente')
    if fuente:
        d = soup.new_tag('details', attrs={'class':'sesion-fuente'})
        s = soup.new_tag('summary'); s.string = 'Fuente'; d.append(s)
        fuente.wrap(d)
    ids = soup.select_one('.tapa .campos-id')
    if ids:
        d = soup.new_tag('details', attrs={'class':'sesion-fuente'})
        s = soup.new_tag('summary'); s.string = 'Datos del registro'; d.append(s)
        ids.wrap(d)
    # La secuencia del jardín conserva el comportamiento conocido.
    if nombre == 'met-jardin-de-valores':
        soup.body['data-secuencia'] = 'jardin'
    else:
        principal = soup.new_tag('div', attrs={'class':'sesion-principal'})
        envoltura.header.insert_after(principal)
        complementos = soup.new_tag('div', attrs={'class':'sesion-complementos'})
        principal.insert_after(complementos)
        for i in centrales:
            principal.append(bloques[i].extract())
        for i,b in enumerate(bloques):
            if i in centrales: continue
            titulo = b.find(['h2','h3'])
            if titulo:
                numero = titulo.select_one('.num')
                if numero: numero.decompose()
                etiqueta = titulo.get_text(' ',strip=True)
            else:
                et = b.select_one('.etq,.campo,.nombre')
                etiqueta = et.get_text(' ',strip=True) if et else {
                    'dial':'Intensidad de la petición', 'escenario':'Explorar la escena',
                    'antes-despues':'Comparar las frases', 'hipotesis':'Hipótesis de trabajo',
                    'nucleo':'Lectura de la creencia', 'panel-mapa':'Mapa del inventario',
                }.get((b.get('class') or [''])[0], 'Explorar con más detalle')
            if nombre == 'pp-tres-cosas-buenas' and i == 2: etiqueta = 'Practicar la visualización'
            d = soup.new_tag('details', attrs={'class':'sesion-apoyo'})
            s = soup.new_tag('summary'); s.string = etiqueta; d.append(s)
            d.append(b.extract()); complementos.append(d)
            if titulo: titulo['class'] = titulo.get('class',[]) + ['sesion-titulo-repetido']
        # Sin numeración global: cada apoyo se abre por su contenido.
        if nombre not in {'crisis-plan-de-seguridad','dbt-verificar-los-hechos'}:
            for n in principal.select('h2 > .num'): n.decompose()
        if nombre in ESCENAS_LATERALES:
            escena = principal.select_one(':scope > .escenario')
            if escena:
                mesa = soup.new_tag('div', attrs={'class':'sesion-mesa'})
                prep = soup.new_tag('div', attrs={'class':'sesion-preparacion'})
                principal.insert(0, mesa); mesa.append(prep)
                for e in list(principal.children):
                    if e is mesa or e is escena: continue
                    if getattr(e,'name',None) == 'section' and 'pregunta-sola' not in e.get('class',[]):
                        prep.append(e.extract())
                mesa.append(escena.extract())
        # Marcadores de juego quedan consultables; los controles y la experiencia arriba.
        for escena in principal.select('.escenario'):
            marcas = escena.select_one(':scope > .marcas')
            if marcas:
                d = soup.new_tag('details', attrs={'class':'sesion-datos'})
                s = soup.new_tag('summary'); s.string = 'Datos de la práctica'; d.append(s)
                d.append(marcas.extract()); escena.append(d)
        if nombre == 'met-hojas-en-el-arroyo':
            duracion = soup.select_one('#duracion')
            opciones = soup.new_tag('details', attrs={'class':'sesion-datos'})
            titulo = soup.new_tag('summary'); titulo.string = 'Duración, corriente y registro de enganches'
            opciones.append(titulo)
            duracion.wrap(opciones)
            escena = soup.select_one('.escenario')
            escena.append(opciones.extract())
        # El termómetro, las precauciones y las ramas clínicas no se ocultan.
        if nombre == 'tcc-ventana-de-sueno':
            seguridad = soup.select_one('#antecedentes')
            bandera = soup.select_one('#bandera')
            if seguridad:
                aviso = soup.new_tag('section', attrs={'class':'bloque sesion-seguridad'})
                h = soup.new_tag('h2'); h.string = 'Antes de acordar la ventana'; aviso.append(h)
                label = seguridad.find_previous_sibling('label')
                if label: aviso.append(label.extract())
                aviso.append(seguridad.extract())
                if bandera: aviso.append(bandera.extract())
                principal.insert(0,aviso)
        if nombre == 'dbt-tarjeta-diaria':
            registro = complementos.select_one('details')
            if registro:
                registro['id'] = 'registro-del-dia'
                registro.summary.string = 'Registrar o revisar un día'
    css = soup.new_tag('style'); css.string = (AQUI/'sesion.css').read_text(encoding='utf-8')
    soup.head.append(css)
    return incrustar_imagenes(str(soup))

def descripcion(archivo):
    return REVISION[Path(archivo).stem][2]

def documentar():
    lineas = ['# Revisión de las 47 herramientas para el uso en sesión', '',
      'Criterio acordado: protagonismo y acceso inicial al componente aprovechable en conversación. '
      'Los complementos se conservan y se abren por su nombre. No se exige completar la herramienta.', '',
      '| Herramienta | Entrada principal | Bloques centrales (índices de fuente) |',
      '|---|---|---|']
    for n,(_,orden,entrada) in REVISION.items():
        lineas.append(f'| {n} | {entrada} | {", ".join(map(str,orden))} |')
    lineas += ['', 'El jardín conserva su secuencia. El plan de seguridad conserva todos sus componentes visibles. '
      'Las ramas de Verificar los hechos siguen dependiendo de las respuestas. Las precauciones de sueño preceden al cálculo.',
      '', 'Los motores y las interpretaciones clínicas existentes requieren una revisión clínica separada si se desean cambiar; '
      'esta revisión reorganiza su acceso y su presentación. No se han añadido puntuaciones ni nuevas reglas clínicas.']
    (AQUI/'REVISION-SESION.md').write_text('\n'.join(lineas)+'\n',encoding='utf-8')
