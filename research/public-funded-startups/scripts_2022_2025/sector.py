import re
RULES=[
(r'videojuego|video ?game|gaming|esports|e-sports','Videogames/esports'),
(r'ciberseguridad|cybersecurity|cyber','Cybersecurity'),
(r'biotecnolog|biotech|farmac|pharma|medicament|f[aá]rmaco|terap[eé]ut|anticuerp|microbio','Biotech/pharma'),
(r'sanitari|m[eé]dic|salud|health|cl[ií]nic|hospital|fisioterap|paciente|diagn[oó]stic','Health/medtech'),
(r'cosm[eé]tic|belleza|beauty','Cosmetics/beauty'),
(r'hidr[oó]geno|hydrogen','Hydrogen/energy'),
(r'fotovolt|solar|renovable|energ[eé]tic|energ[ií]a|electrificaci|bater[ií]a|battery|eólic|eolic','Energy/cleantech'),
(r'reciclaj|residuo|recycl|circular|valorizaci','Recycling/circular economy'),
(r'agr[ií]col|agri|agro|cultivo|ganad|acuicultur|alga|forest','Agri/food-tech/forestry'),
(r'aliment|bebida|food|cerveza|vino|bodega|caf[eé]|gastronom|restaura|cocina','Food & beverage'),
(r'drone|dron|aeroespacial|aerospace|aeron[aá]ut|sat[eé]lite|space','Aerospace/drones'),
(r'robot','Robotics/automation'),
(r'inteligencia artificial|\bia\b|\bai\b|machine learning|aprendizaje autom','AI/software'),
(r'software|aplicaci[oó]n(es)? inform|plataforma digital|saas|programaci[oó]n|desarrollo inform|app\b|apps|tecnolog[ií]as de la informaci|inform[aá]tic|digital','Software/digital'),
(r'electr[oó]nic|semiconduct|microelectr|sensor|iot|telecomunic','Electronics/IoT'),
(r'construcci|edificaci|arquitect|inmobiliar|vivienda','Construction/real estate'),
(r'textil|moda|ropa|prendas|calzado|fashion','Textile/fashion'),
(r'deport|sport|fitness|gimnas','Sport'),
(r'audiovisual|cine|m[uú]sica|music|producci[oó]n de contenido|editorial|comunicaci[oó]n|publicidad|marketing','Media/marketing'),
(r'educaci|formaci[oó]n|ense[nñ]anza|training','Education/training'),
(r'movilidad|veh[ií]culo|bicicleta|bike|transporte|log[ií]stic|automoci','Mobility/logistics'),
(r'fabricaci|mecaniz|maquinaria|industrial|metal|fundici|calderer|moldes|matric|soldadura|pl[aá]stic|material|composite|recubrimiento|coating','Industrial manufacturing/materials'),
(r'ingenier[ií]a|engineering|consultor[ií]a t[eé]cnica','Engineering services'),
(r'consultor[ií]a|asesor[ií]a|gesti[oó]n empresarial','Consulting'),
(r'comercio|venta|distribuci|e-commerce|ecommerce|tienda','Commerce/e-commerce'),
(r'turismo|viaje|travel|hotel','Tourism/travel'),
(r'investigaci[oó]n|i\+d|desarrollo tecnol','R&D'),
]
def sector(obj,name=''):
    s=(obj or '')+' '+(name or '')
    for p,l in RULES:
        if re.search(p,s,re.I): return l
    return 'unknown'
