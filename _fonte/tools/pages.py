# Conteúdo das páginas (executado dentro de build.py)

def HOME():
    cats = [
        ("Louças", "loucas-vitrine", "Cubas"),
        ("Metais", "torneiras-fila", "Torneiras e misturadores"),
        ("Banheiras, Spas e Ofurôs", "banheira-pedra", "Banheiras"),
        ("Cubas e Bancadas", "cuba-marmore", "Cubas"),
        ("Revestimentos e Porcelanatos", "box-marmore", "Porcelanatos"),
        ("Eletrodomésticos", "eletros-embutir", "Fornos"),
        ("Acessórios e Decoração", "acessorios-perola", "Acessórios de banheiro"),
        ("Soluções para Cozinhas", "cozinha-cuba", "Acessórios de cozinha"),
    ]
    cards = "".join(
        f'''<a class="card rv{' rv-d'+str(i%4) if i%4 else ''}" href="catalogo.html?cat={c[2].replace(' ','%20')}">{img(c[1], c[0])}
<h3 class="h3" style="margin-top:22px">{c[0]}</h3><span class="link">Explorar</span></a>'''
        for i, c in enumerate(cats))
    brands = "".join(f'<a href="marcas.html#{m.lower().replace(" ","-")}">{m}</a>' for m in MARCAS)
    slides = [("banheiro-cubas", "Banheiro com cubas de apoio e metais escovados"),
              ("banho-cuba-verde", "Cuba de apoio verde com espelho iluminado"),
              ("metais-paprica", "Misturador de cozinha na cor páprica"),
              ("piso-marmore", "Piso em mármores combinados"),
              ("cozinha-cuba", "Cuba de cozinha com misturador de bica móvel")]
    slides_html = "".join(f'<div class="slide" role="group" aria-roledescription="slide" aria-label="{i+1} de {len(slides)}">{vid(n, l)}<p class="caption">{l}</p></div>' for i, (n, l) in enumerate(slides))
    return f'''
<div class="intro" aria-hidden="true"><div><div class="intro__logo"><img src="assets/img/logo-marrom.png" alt="" width="1667" height="456"><span class="intro__beam"></span></div><div class="intro__line"></div></div></div>

<section class="hero" id="inicio" aria-label="Apresentação">
  <div class="hero__bg"><img src="assets/img/hero-lavabo.jpg" alt="Lavabo com bancada esculpida em mármore marrom, metais em cobre e painéis de madeira iluminados" width="1500" height="1875" fetchpriority="high"></div>
  <div class="wrap hero__c on-image">
    <span class="eyebrow rv-h">Boutique de banho · Paraíba</span>
    <h1 class="rv-h">A arte de transformar ambientes começa nos <em>detalhes.</em></h1>
    <p class="lead rv-h">Uma curadoria exclusiva de louças, metais, revestimentos e acabamentos para projetos que valorizam cada escolha.</p>
    <div class="btns rv-h"><a class="btn btn--light" href="#boutique">Explore a Le Bagno</a><a class="btn btn--light btn--ghost" href="{WA}" data-wa="geral">Fale com um especialista</a></div>
  </div>
  <div class="hero__foot"><span>Role</span><i></i></div>
</section>

<section class="sec" id="boutique">
  <div class="wrap tri tri--offset">
    <figure class="tri__media rv" style="margin:0">{img("showroom-fernanda", "Fernanda Lima, CEO da Le Bagno, no showroom de metais em João Pessoa", w=1005, h=1256)}<figcaption class="caption">Showroom João Pessoa</figcaption></figure>
    <div class="tri__text rv rv-d1">
      <span class="eyebrow">A Boutique</span>
      <h2 class="h2">Mais que produtos. <em>Uma experiência.</em></h2>
      <p class="lead">Há escolhas que definem a personalidade de um ambiente. Na Le Bagno, reunimos design, qualidade e sofisticação em uma curadoria de produtos que transforma projetos em experiências únicas.</p>
      <p class="lead" style="margin-top:14px">Nossa essência está em oferecer soluções que unem beleza, funcionalidade e excelência, com um atendimento consultivo pensado para cada detalhe.</p>
      <a class="btn btn--ghost" href="#historia">Conheça nossa história</a>
    </div>
    <figure class="tri__media rv rv-d2" style="margin:0">{img("showroom-metais", "Parede de metais em diferentes acabamentos no showroom", w=748, h=935)}<figcaption class="caption">Metais em múltiplos acabamentos</figcaption></figure>
  </div>
</section>

<section class="sec sec--alt" id="produtos">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Categorias</span><h2 class="h2">Cada ambiente merece uma escolha <em>extraordinária.</em></h2><p class="lead">Descubra soluções que unem estética, tecnologia e funcionalidade.</p></div>
    <div class="cats">{cards}</div>
  </div>
</section>

<section class="band" id="banho">
  <div class="band__bg" data-parallax><img src="assets/img/espelhos-duplos.jpg" alt="" width="1100" height="1375" loading="lazy"></div>
  <div class="wrap"><div class="head rv on-image">
    <span class="eyebrow">A arte do banho</span>
    <h2 class="h2">Seu banho merece uma experiência <em>extraordinária.</em></h2>
    <p class="lead">Mais do que funcionalidade, o banheiro é um espaço de pausa, conforto e personalidade. Descubra uma seleção de louças, metais, banheiras e acabamentos que elevam cada detalhe.</p>
    <div class="btns btns--one"><a class="btn btn--light" href="inspiracoes.html">Explore o universo do banho</a></div>
  </div></div>
</section>

<section class="sec" id="cozinhas">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Cozinhas</span><h2 class="h2">Design e funcionalidade em perfeita <em>harmonia.</em></h2><p class="lead">Da escolha dos metais aos eletrodomésticos, cada elemento participa da construção de uma cozinha que combina personalidade, praticidade e sofisticação.</p></div>
    <div class="trio">
      <div class="rv">{img("eletros-embutir", "Forno e micro-ondas de embutir em marcenaria de madeira")}</div>
      <div class="frame--feature-wrap rv rv-d1"><div class="frame frame--feature"><video src="assets/video/cozinha-ambiente.mp4" poster="assets/img/poster-cozinha-ambiente.jpg" muted loop playsinline preload="metadata" aria-label="Cozinha planejada com cooktop, acessórios de cuba e eletrodomésticos"></video></div></div>
      <div class="rv rv-d2">{img("cozinha-cuba", "Cuba de inox com misturador de bica móvel")}</div>
    </div>
    <ul class="chips rv"><li>Cubas</li><li>Torneiras</li><li>Misturadores</li><li>Coifas</li><li>Fornos</li><li>Eletrodomésticos</li><li>Acessórios</li></ul>
    <div class="btns btns--one rv"><a class="btn" href="{WA}" data-wa="cozinha">Descubra as soluções</a></div>
  </div>
</section>

<section class="sec sec--dark" id="marcas">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Marcas</span><h2 class="h2">Grandes marcas. <em>Escolhas extraordinárias.</em></h2><p class="lead">Uma seleção de marcas reconhecidas pela excelência em design, tecnologia e qualidade.</p></div>
    <div class="brands rv">{brands}</div>
  </div>
</section>

<section class="sec" id="pronta-entrega">
  <div class="wrap split">
    <div class="split__text sec--alt rv">
      <span class="eyebrow">Pronta entrega</span>
      <h2 class="h2">Seu projeto não precisa <em>esperar.</em></h2>
      <p class="lead">Na Le Bagno, você encontra uma seleção de produtos a pronta entrega, unindo praticidade, agilidade e sofisticação para acompanhar o ritmo do seu projeto.</p>
      <a class="btn" href="{WA}" data-wa="estoque">Consulte nosso estoque</a>
      <p class="caption" style="margin-top:22px">Disponibilidade confirmada pela equipe no atendimento</p>
    </div>
    <div class="rv rv-d1">{img("cubas-vitrine", "Cubas de apoio em diferentes formatos expostas na boutique")}</div>
  </div>
</section>

<section class="sec sec--alt" id="movimento" aria-label="Vídeos">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Em movimento</span><h2 class="h2">Projetos que ganham <em>vida.</em></h2><p class="lead">Ambientes reais com produtos da boutique, do lavabo à cozinha.</p></div>
    <div class="carousel rv" aria-roledescription="carrossel" aria-label="Vídeos de projetos">
      <div class="track" tabindex="0">{slides_html}</div>
      <div class="ctrl"><button class="prev" type="button" aria-label="Vídeo anterior">{ARROW_L}</button><div class="dots"></div><button class="next" type="button" aria-label="Próximo vídeo">{ARROW_R}</button></div>
    </div>
  </div>
</section>

<section class="sec sec--dark" id="arquitetos">
  <div class="wrap arch">
    <div class="arch__text rv">
      <span class="eyebrow">Espaço do arquiteto</span>
      <h2 class="h2">Seu projeto merece escolhas <em>à altura.</em></h2>
      <p class="lead">A Le Bagno acredita na força dos detalhes e na importância de cada especificação. Por isso, oferecemos uma experiência consultiva para profissionais que buscam soluções diferenciadas em louças, metais, revestimentos e acabamentos.</p>
      <ul class="feats"><li>Atendimento especializado</li><li>Consultoria para especificação</li><li>Curadoria de marcas</li><li>Suporte na escolha de produtos</li><li>Parcerias profissionais</li><li>Consulta a informações técnicas</li></ul>
    </div>
    <form class="form rv rv-d1" id="form-arquitetos" novalidate>
      <h3 class="h3">Fale com nossa equipe</h3>
      <p class="form__note">Envie seus dados e continuamos a conversa pelo WhatsApp.</p>
      <div class="field"><label for="arq-nome">Nome</label><input id="arq-nome" name="nome" autocomplete="name" required></div>
      <div class="row2"><div class="field"><label for="arq-escritorio">Escritório</label><input id="arq-escritorio" name="escritorio" autocomplete="organization"></div>
      <div class="field"><label for="arq-area">Atuação</label><select id="arq-area" name="area"><option>Arquitetura</option><option>Design de interiores</option><option>Engenharia / construção</option><option>Outro</option></select></div></div>
      <div class="row2"><div class="field"><label for="arq-contato">Telefone ou e-mail</label><input id="arq-contato" name="contato" autocomplete="tel" required></div>
      <div class="field"><label for="arq-cidade">Cidade</label><input id="arq-cidade" name="cidade" autocomplete="address-level2"></div></div>
      <div class="field"><label for="arq-msg">Sobre o projeto</label><textarea id="arq-msg" name="mensagem" rows="3"></textarea></div>
      <button class="btn" type="submit">Fale com nossa equipe</button>
      <p class="form__msg" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>

<section class="sec" id="historia">
  <div class="wrap tri">
    <div class="tri__media rv">{img("lavabo-emperador", "Lavabo com bancada em mármore marrom e metais em cobre")}</div>
    <div class="tri__text rv rv-d1">
      <span class="eyebrow">Desde 2018</span>
      <h2 class="h2">Uma história construída com <em>elegância.</em></h2>
      <p class="lead">Desde 2018, a Le Bagno constrói sua trajetória em João Pessoa com um propósito: oferecer muito mais do que produtos, proporcionando uma experiência de escolha marcada pela sofisticação, qualidade e atendimento personalizado.</p>
      <p class="lead" style="margin-top:14px">Nossa boutique reúne grandes marcas e soluções para transformar ambientes, acompanhando arquitetos, profissionais e clientes em cada etapa de seus projetos.</p>
      <p class="signature">Fernanda Lima<small>CEO · Le Bagno</small></p>
    </div>
    <div class="tri__media rv rv-d2">{img("fernanda-lima", "Fernanda Lima, CEO da Le Bagno, em seu escritório", w=888, h=1110)}</div>
  </div>
</section>

<section class="sec sec--alt" id="lojas">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Nossas lojas</span><h2 class="h2">Uma experiência Le&nbsp;Bagno, <em>mais perto de você.</em></h2></div>
    <article class="store store--main rv">
      {img("fachada-jp", "Fachada da Le Bagno em Manaíra, João Pessoa, com vitrines iluminadas")}
      <div class="store__info">
        <span class="store__tag">Showroom principal</span>
        <h3>Le Bagno João Pessoa</h3>
        <dl class="dl">
          <div><dt>Endereço</dt><dd>Avenida Monteiro da Franca, 1592 – Manaíra, João Pessoa – PB</dd></div>
          <div><dt>Telefone</dt><dd><a href="tel:+558335080048">(83) 3508-0048</a></dd></div>
          <div><dt>Horário</dt><dd>Segunda a sexta: 09h às 18h<br>Sábado: 09h às 13h</dd></div>
          <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/lebagno/" target="_blank" rel="noopener">@lebagno</a></dd></div>
        </dl>
        <div class="btns"><a class="btn" href="https://www.instagram.com/lebagno/" target="_blank" rel="noopener">Conheça nosso showroom</a><a class="btn btn--ghost" href="{MAPS_JP}" data-maps="jp">Como chegar</a></div>
      </div>
    </article>
    <div class="stores-label"><span class="eyebrow">Segunda unidade</span></div>
    <article class="store store--second rv">
      <div class="store__info">
        <h3>Le Bagno Campina Grande</h3>
        <dl class="dl">
          <div><dt>Endereço</dt><dd>Rua Raimundo Alves da Silva, 333 – Centro, Campina Grande – PB</dd></div>
          <div><dt>Telefone</dt><dd><a href="tel:+558332010671">(83) 3201-0671</a></dd></div>
          <div><dt>Horário</dt><dd>Segunda a sexta: 09h às 18h<br>Sábado: 09h às 13h</dd></div>
          <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/lebagnocg/" target="_blank" rel="noopener">@lebagnocg</a></dd></div>
        </dl>
        <div class="btns"><a class="btn" href="https://wa.me/5583993818544" data-wa="cg" data-wa-cg>Fale com a unidade</a><a class="btn btn--ghost" href="https://www.google.com/maps/search/?api=1&amp;query=Rua%20Raimundo%20Alves%20da%20Silva%2C%20333%20%E2%80%93%20Centro%2C%20Campina%20Grande%20%E2%80%93%20PB" data-maps="cg">Como chegar</a></div>
      </div>
      {img("cuba-pedra-bruta", "Cuba esculpida em pedra sobre bancada de madeira maciça")}
    </article>
  </div>
</section>

<section class="band band--cta" id="contato">
  <div class="band__bg" data-parallax><img src="assets/img/cubas-escuras.jpg" alt="" width="1100" height="1375" loading="lazy"></div>
  <div class="wrap"><div class="head rv on-image">
    <span class="eyebrow">Atendimento consultivo</span>
    <h2 class="h2">Seu próximo projeto começa com uma <em>boa escolha.</em></h2>
    <p class="lead">Descubra possibilidades, explore acabamentos e encontre soluções que traduzem a essência do seu ambiente.</p>
    <div class="btns btns--one"><a class="btn btn--light" href="{WA}" data-wa="geral">Fale com a Le Bagno</a></div>
  </div></div>
</section>
'''

def CATALOGO():
    sel = "".join(f'<div class="field"><label for="f-{k}">{l}</label><select id="f-{k}"><option value="">Todos</option></select></div>'
                  for k, l in [("ambiente","Ambiente"),("categoria","Categoria"),("marca","Marca"),("acabamento","Acabamento"),("estilo","Estilo")])
    return f'''
<section class="phead"><div class="wrap"><span class="eyebrow">Catálogo</span><h1 class="h2">Uma curadoria para <em>cada detalhe.</em></h1>
<p class="lead">Explore por ambiente, categoria, marca, acabamento ou estilo. Cada peça é apresentada para orçamento consultivo com nossa equipe.</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap">
<div class="filters">{sel}<button class="btn btn--ghost" type="button" id="f-limpar">Limpar</button></div>
<p class="count" id="catalogo-count" aria-live="polite"></p>
<div class="grid3" id="catalogo-grid"></div>
</div></section>
<section class="sec sec--dark center"><div class="wrap"><div class="head" style="margin-bottom:0"><span class="eyebrow">Não encontrou?</span><h2 class="h2">A boutique reúne muito <em>mais.</em></h2><p class="lead">O catálogo online mostra uma seleção. Conte o que seu projeto pede e indicamos as opções disponíveis.</p><div class="btns btns--one"><a class="btn btn--light" href="{WA}" data-wa="geral">Fale com um especialista</a></div></div></div></section>
'''

def MARCAS_PAGE():
    cards = "".join(f'''<article class="bcard rv" id="{m.lower().replace(' ','-')}"><h2 class="h3">{m}</h2><p>Linhas e disponibilidade apresentadas pela nossa equipe na boutique.</p>
<div class="bcard__a"><a class="link" href="catalogo.html?marca={m.replace(' ','%20')}">Ver produtos</a><a class="link" href="{WA}" data-wa="Olá, Le Bagno! Gostaria de conhecer os produtos {m}.">Consultar</a></div></article>''' for m in MARCAS)
    return f'''
<section class="phead"><div class="wrap"><span class="eyebrow">Marcas</span><h1 class="h2">Grandes marcas. <em>Escolhas extraordinárias.</em></h1>
<p class="lead">Uma seleção de marcas reconhecidas pela excelência em design, tecnologia e qualidade. Conheça o universo de cada fabricante com a nossa equipe.</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="grid3">{cards}</div></div></section>
'''

def INSPIRACOES():
    items = [
        ("hero-lavabo", "Lavabo em mármore marrom", "lavabos alto-padrao", 1500, 1875),
        ("banheira-pedra", "Banheira de imersão", "banheiros contemporaneos", 928, 1160),
        ("espelhos-duplos", "Bancada dupla iluminada", "banheiros contemporaneos", 1100, 1375),
        ("cubas-escuras", "Cubas escuras e pedra bruta", "lavabos alto-padrao", 1100, 1375),
        ("banheiro-lustre", "Banheiro de casal", "banheiros alto-padrao", 720, 900),
        ("cuba-pedra-bruta", "Cuba esculpida", "lavabos contemporaneos", 1100, 1375),
        ("torneira-ouro", "Metais dourados entre pedras", "lavabos alto-padrao", 856, 1070),
        ("eletros-embutir", "Eletros de embutir", "cozinhas", 1100, 1375),
        ("poster-metais-paprica", "Bar com misturador páprica", "gourmet cozinhas", 712, 890),
        ("cozinha-cuba", "Cuba de cozinha em inox", "cozinhas contemporaneos", 1100, 1375),
        ("chuveiros-cobre", "Duchas em cobre", "banheiros", 1100, 1375),
        ("espelho-organico", "Espelho orgânico iluminado", "banheiros contemporaneos", 960, 1200),
        ("box-marmore", "Box em porcelanato marmorizado", "banheiros", 1100, 1375),
        ("cuba-escavada", "Cuba escavada no mármore", "lavabos alto-padrao", 776, 970),
        ("lavabo-madeira", "Lavabo em madeira e mármore", "lavabos alto-padrao", 1100, 1375),
        ("banheira-ladrilho", "Banheira e ladrilhos", "banheiros", 750, 938),
        ("espelho-oval", "Espelho oval e metais pretos", "banheiros contemporaneos", 960, 1200),
        ("cuba-dourada", "Cuba dourada", "lavabos", 828, 1035),
    ]
    tabs = [("todos","Todos"),("banheiros","Banheiros"),("lavabos","Lavabos"),("cozinhas","Cozinhas"),("gourmet","Áreas gourmet"),("contemporaneos","Contemporâneos"),("alto-padrao","Alto padrão")]
    tb = "".join(f'<button type="button" data-f="{k}" aria-pressed="{"true" if k=="todos" else "false"}">{l}</button>' for k, l in tabs)
    g = "".join(f'''<figure class="gal rv" data-cat="{c}" data-title="{t}" style="margin:0"><button type="button" aria-label="Ampliar: {t}"><div class="frame"><img src="assets/img/{s}.jpg" alt="{t}" width="{w}" height="{h}" loading="lazy"></div></button><figcaption class="caption"><span>{t}</span><span>{i+1:02d}</span></figcaption></figure>''' for i, (s, t, c, w, h) in enumerate(items))
    return f'''
<section class="phead"><div class="wrap"><span class="eyebrow">Inspirações</span><h1 class="h2">Ambientes que inspiram. <em>Detalhes que transformam.</em></h1>
<p class="lead">Projetos e ambientes com produtos da curadoria Le Bagno. Toque em uma imagem para ampliar.</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="tabs" role="group" aria-label="Filtrar ambientes">{tb}</div><div class="grid3" id="galeria">{g}</div></div></section>
<div class="lb" hidden role="dialog" aria-modal="true" aria-label="Imagem ampliada"><button class="lb__p" type="button" aria-label="Anterior">{ARROW_L}</button><figure><img src="" alt=""><figcaption></figcaption></figure><button class="lb__n" type="button" aria-label="Próxima">{ARROW_R}</button><button class="lb__x" type="button" aria-label="Fechar"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg></button></div>
'''

def PAGES():
    D = "Le Bagno, a maior boutique de banho da Paraíba: louças, metais, revestimentos, acabamentos e eletrodomésticos de alto padrão em João Pessoa e Campina Grande."
    return {
        "index.html": doc("Le Bagno", D, HOME(), "", True),
        "catalogo.html": doc("Catálogo Le Bagno", "Catálogo premium Le Bagno: metais, cubas, banheiras, acessórios, eletrodomésticos e revestimentos para orçamento consultivo.", CATALOGO(), "page-light", False, "produtos"),
        "marcas.html": doc("Marcas Le Bagno", "Marcas comercializadas pela Le Bagno: Doka, Rubinettos, Tramontina, Debacco, Invita, Portobello, Portinari, Villagres, Ceusa, Deca, Franke e Zen Design.", MARCAS_PAGE(), "page-light", False, "marcas"),
        "inspiracoes.html": doc("Inspirações Le Bagno", "Galeria editorial de banheiros, lavabos, cozinhas e ambientes de alto padrão com produtos Le Bagno.", INSPIRACOES(), "page-light", False, "inspiracoes"),
    }
