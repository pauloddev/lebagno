#!/usr/bin/env python3
"""Gera as páginas do site Le Bagno a partir de partes compartilhadas.
Saídas:
  dist/      -> site completo para hospedar (Vercel/Netlify)
  preview/   -> mesma coisa, com a página inicial no formato do artefato
"""
import os, re, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA = "https://wa.me/5583993818544?text=Ol%C3%A1%2C%20Le%20Bagno!%20Vim%20pelo%20site%20e%20gostaria%20de%20falar%20com%20um%20especialista."
MAPS_JP = "https://www.google.com/maps/search/?api=1&query=Avenida%20Monteiro%20da%20Franca%2C%201592%20%E2%80%93%20Mana%C3%ADra%2C%20Jo%C3%A3o%20Pessoa%20%E2%80%93%20PB"
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Manrope:wght@400;500;600;700&display=swap">'
HEADJS = "<script>(function(d){d.className+=' js';try{if(sessionStorage.getItem('lb-intro')==='1')d.className+=' no-intro'}catch(e){}})(document.documentElement)</script>"

def wa_icon():
    return '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.15h-.01a8.23 8.23 0 0 1-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23 2.2 0 4.27.86 5.83 2.42a8.18 8.18 0 0 1 2.41 5.83c0 4.54-3.7 8.22-8.23 8.22Zm4.51-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.15.16-.29.18-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.16.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48a.92.92 0 0 0-.66.31c-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.24 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.08.15-1.18-.06-.11-.22-.17-.47-.29Z"/></svg>'

ARROW_L = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
ARROW_R = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'

def header(home, cur=""):
    h = "" if home else "index.html"
    def a(href, label, key=""):
        ac = ' aria-current="page"' if key and key == cur else ""
        return f'<a href="{href}"{ac}>{label}</a>'
    left = a(f"{h}#boutique", "A Boutique") + a("catalogo.html", "Produtos", "produtos") + a("marcas.html", "Marcas", "marcas") + a("inspiracoes.html", "Inspirações", "inspiracoes")
    right = a(f"{h}#arquitetos", "Arquitetos") + a(f"{h}#lojas", "Nossas Lojas") + a(f"{h}#contato", "Contato") + f'<a href="{WA}" data-wa="geral">Orçamento</a>'
    mob = "".join([a(f"{h}#inicio" if h else "#inicio", "Início"), left, a(f"{h}#arquitetos", "Arquitetos"), a(f"{h}#lojas", "Nossas Lojas"), a(f"{h}#contato", "Contato")])
    return f'''<header class="header"><div class="wrap header__in">
<nav class="nav nav--l" aria-label="Principal">{left}</nav>
<a class="brand" href="{h or '#inicio'}" aria-label="Le Bagno — início"><img class="on-dark" src="assets/img/logo-branco.png" alt="Le Bagno — Louças, metais e decoração" width="1667" height="456"><img class="on-light" src="assets/img/logo-marrom.png" alt="" width="1667" height="456"></a>
<nav class="nav nav--r" aria-label="Secundária">{right}</nav>
<button class="burger" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="mnav"><span></span><span></span></button>
</div></header>
<nav class="mnav" id="mnav" aria-label="Menu">{mob}<a class="btn btn--light btn--ghost" href="{WA}" data-wa="geral">Solicitar orçamento</a></nav>'''

def footer(home):
    h = "" if home else "index.html"
    return f'''<footer class="footer" id="rodape"><div class="wrap">
<div class="footer__top"><img src="assets/img/logo-branco.png" alt="Le Bagno — Louças, metais e decoração" width="1667" height="456" loading="lazy">
<p>Boutique de louças, metais, revestimentos, acabamentos e eletrodomésticos de alto padrão. Mais que produtos, uma experiência.</p></div>
<div class="fcols">
<div><h4>Navegação</h4><ul><li><a href="{h}#inicio">Início</a></li><li><a href="{h}#boutique">A Boutique</a></li><li><a href="catalogo.html">Produtos</a></li><li><a href="marcas.html">Marcas</a></li><li><a href="inspiracoes.html">Inspirações</a></li><li><a href="{h}#arquitetos">Arquitetos</a></li><li><a href="{h}#lojas">Nossas Lojas</a></li></ul></div>
<div><h4>Categorias</h4><ul><li><a href="catalogo.html?cat=Torneiras%20e%20misturadores">Metais</a></li><li><a href="catalogo.html?cat=Cubas">Louças e cubas</a></li><li><a href="catalogo.html?cat=Banheiras">Banheiras, spas e ofurôs</a></li><li><a href="catalogo.html?cat=Porcelanatos">Revestimentos e porcelanatos</a></li><li><a href="catalogo.html?cat=Fornos">Eletrodomésticos</a></li><li><a href="catalogo.html?cat=Acess%C3%B3rios%20de%20banheiro">Acessórios e decoração</a></li></ul></div>
<div><h4>Marcas</h4><ul style="grid-template-columns:1fr 1fr;column-gap:16px">{"".join(f'<li><a href="marcas.html#{m.lower().replace(" ","-")}">{m}</a></li>' for m in MARCAS)}</ul></div>
<div><h4>Unidades</h4>
<address><strong>João Pessoa · Showroom principal</strong><br>Av. Monteiro da Franca, 1592 – Manaíra<br>João Pessoa – PB<br><a href="tel:+558335080048">(83) 3508-0048</a><br>Seg a sex 09h–18h · Sáb 09h–13h</address>
<address><strong>Campina Grande</strong><br>Rua Raimundo Alves da Silva, 333 – Centro<br>Campina Grande – PB<br><a href="tel:+558332010671">(83) 3201-0671</a> · <a href="https://wa.me/5583993818544" data-wa="cg" data-wa-cg>WhatsApp</a><br>Seg a sex 09h–18h · Sáb 09h–13h</address></div>
</div>
<div class="footer__bot"><span><a href="mailto:lebagnopb@gmail.com">lebagnopb@gmail.com</a> · <a href="https://www.instagram.com/lebagno/" target="_blank" rel="noopener">@lebagno</a> · <a href="https://www.instagram.com/lebagnocg/" target="_blank" rel="noopener">@lebagnocg</a></span><span>Le Bagno · CNPJ 30.865.325/0001-06 · © <span data-year>2026</span></span></div>
</div></footer>
<a class="wa" href="{WA}" data-wa="geral" aria-label="Falar com a Le Bagno no WhatsApp" target="_blank" rel="noopener">{wa_icon()}</a>'''

MARCAS = ["Doka","Rubinettos","Tramontina","Debacco","Invita","Portobello","Portinari","Villagres","Ceusa","Deca","Franke","Zen Design"]

def doc(title, desc, body, bodyclass="", home=False, cur=""):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#2A180C">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/hero-lavabo.jpg">
<link rel="icon" href="assets/img/favicon.png">
{FONTS}
<link rel="stylesheet" href="css/style.css">
{HEADJS}
</head>
<body class="{bodyclass}">
{header(home, cur)}
<main id="conteudo">
{body}
</main>
{footer(home)}
<script src="js/config.js"></script>
<script src="js/produtos.js"></script>
<script src="js/main.js"></script>
</body>
</html>
'''

def img(src, alt, cls="frame", extra="", w=1100, h=1375, lazy=True):
    return f'<div class="{cls}"{extra}><img src="assets/img/{src}.jpg" alt="{alt}" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else ""}></div>'

def vid(name, label):
    return f'<div class="frame"><video src="assets/video/{name}.mp4" poster="assets/img/poster-{name}.jpg" muted loop playsinline preload="metadata" aria-label="{label}"></video></div>'

for_include = {}
exec(open(os.path.join(ROOT, "tools", "pages.py"), encoding="utf-8").read())

def write(outdir, name, html):
    with open(os.path.join(outdir, name), "w", encoding="utf-8") as f: f.write(html)

def main():
    for out in ("dist", "preview"):
        d = os.path.join(ROOT, out)
        shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
        for sub in ("css", "js", "assets"):
            shutil.copytree(os.path.join(ROOT, sub), os.path.join(d, sub))
        for name, html in PAGES().items():
            write(d, name, html)
    # artefato: página inicial sem doctype/html/head/body (o publicador envolve)
    p = os.path.join(ROOT, "preview", "index.html")
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", s)
    s = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', "", s)
    s = s.replace("</head>\n<body class=\"\">", "").replace("</head>\n<body class=\"home\">", '<div class="home">')
    s = s.replace("</body>\n</html>", "")
    write(os.path.dirname(p), "index.html", s)
    print("ok")

if __name__ == "__main__": main()
