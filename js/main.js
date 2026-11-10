(function () {
  "use strict";
  var doc = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Links centralizados (config.js) ---------- */
  function bindLinks() {
    if (!window.LB) return;
    $$("[data-wa]").forEach(function (a) {
      var k = a.getAttribute("data-wa");
      var num = a.hasAttribute("data-wa-cg") ? LB.unidades.cg.whatsapp : null;
      a.href = LB.wa(LB.mensagens[k] || k, num);
      a.target = "_blank"; a.rel = "noopener";
    });
    $$("[data-maps]").forEach(function (a) {
      a.href = LB.maps(LB.unidades[a.getAttribute("data-maps")].endereco);
      a.target = "_blank"; a.rel = "noopener";
    });
    $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  /* ---------- Intro do logo ---------- */
  function intro() {
    var el = $(".intro");
    if (!el) return;
    var seen = false;
    try { seen = sessionStorage.getItem("lb-intro") === "1"; } catch (e) {}
    if (seen) { el.classList.add("gone"); doc.classList.remove("intro-on"); return; }
    doc.classList.add("intro-on");
    document.body.style.overflow = "hidden";
    var finish = function () {
      if (el.classList.contains("done")) return;
      el.classList.add("done");
      document.body.style.overflow = "";
      doc.classList.remove("intro-on");
      try { sessionStorage.setItem("lb-intro", "1"); } catch (e) {}
      setTimeout(function () { el.classList.add("gone"); }, 1200);
    };
    setTimeout(finish, reduce ? 500 : 2500);
    el.addEventListener("click", finish);
  }

  /* ---------- Header inteligente ---------- */
  function header() {
    var h = $(".header");
    if (!h) return;
    var last = 0, solidAt = 60;
    var onScroll = function () {
      var y = window.scrollY;
      h.classList.toggle("solid", y > solidAt);
      last = y;
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    var b = $(".burger");
    if (b) b.addEventListener("click", function () {
      var open = doc.classList.toggle("menu-open");
      b.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    $$(".mnav a").forEach(function (a) {
      a.addEventListener("click", function () {
        doc.classList.remove("menu-open");
        if (b) b.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Revelação suave ---------- */
  function reveal() {
    var els = $$(".rv");
    if (!("IntersectionObserver" in window) || reduce) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: .08 });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- Parallax sutil ---------- */
  function parallax() {
    if (reduce) return;
    var items = $$("[data-parallax]");
    if (!items.length) return;
    var ticking = false;
    var run = function () {
      var vh = window.innerHeight;
      items.forEach(function (el) {
        var r = el.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var p = (r.top + r.height / 2 - vh / 2) / vh;
        el.style.transform = "translate3d(0," + (p * -60).toFixed(1) + "px,0)";
      });
      ticking = false;
    };
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(run); } }, { passive: true });
    run();
  }

  /* ---------- Vídeos: sempre mudos, tocam só quando visíveis ---------- */
  function videos() {
    var vids = $$("video");
    vids.forEach(function (v) { v.muted = true; v.defaultMuted = true; v.setAttribute("muted", ""); v.playsInline = true; });
    if (!("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting && !reduce) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else v.pause();
      });
    }, { threshold: .35 });
    vids.forEach(function (v) { io.observe(v); });
  }

  /* ---------- Carrossel ---------- */
  function carousel() {
    $$(".carousel").forEach(function (c) {
      var track = $(".track", c), slides = $$(".slide", c), dots = $(".dots", c);
      if (!track || !slides.length) return;
      slides.forEach(function (s, i) {
        var d = document.createElement("button");
        d.type = "button"; d.setAttribute("aria-label", "Ir para o vídeo " + (i + 1));
        d.addEventListener("click", function () { go(i); });
        dots.appendChild(d);
      });
      var cur = 0;
      function go(i) {
        i = (i + slides.length) % slides.length;
        var s = slides[i];
        track.scrollTo({ left: s.offsetLeft - (track.clientWidth - s.clientWidth) / 2, behavior: reduce ? "auto" : "smooth" });
      }
      function update() {
        var mid = track.scrollLeft + track.clientWidth / 2, best = 0, bd = 1e9;
        slides.forEach(function (s, i) { var d = Math.abs(s.offsetLeft + s.clientWidth / 2 - mid); if (d < bd) { bd = d; best = i; } });
        cur = best;
        slides.forEach(function (s, i) { s.classList.toggle("active", i === best); });
        $$("button", dots).forEach(function (d, i) { d.setAttribute("aria-current", i === best ? "true" : "false"); });
      }
      var t; track.addEventListener("scroll", function () { clearTimeout(t); t = setTimeout(update, 60); }, { passive: true });
      $(".prev", c).addEventListener("click", function () { go(cur - 1); });
      $(".next", c).addEventListener("click", function () { go(cur + 1); });
      window.addEventListener("resize", update);
      // começa com o vídeo central em destaque
      var start = Math.floor(slides.length / 2);
      requestAnimationFrame(function () { track.scrollLeft = slides[start].offsetLeft - (track.clientWidth - slides[start].clientWidth) / 2; update(); });
    });
  }

  /* ---------- Formulário de arquitetos → WhatsApp ---------- */
  function archForm() {
    var f = $("#form-arquitetos");
    if (!f) return;
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var g = function (id) { return ($("#" + id).value || "").trim(); };
      var msg = $(".form__msg", f);
      if (!g("arq-nome") || !g("arq-contato")) { msg.textContent = "Preencha seu nome e um telefone ou e-mail para continuarmos."; return; }
      var txt = "Olá, Le Bagno! Sou profissional e tenho interesse em ser parceiro.\n\n" +
        "Nome: " + g("arq-nome") + "\n" +
        (g("arq-escritorio") ? "Escritório: " + g("arq-escritorio") + "\n" : "") +
        "Atuação: " + g("arq-area") + "\n" +
        (g("arq-cidade") ? "Cidade: " + g("arq-cidade") + "\n" : "") +
        "Contato: " + g("arq-contato") + "\n" +
        (g("arq-msg") ? "\nProjeto: " + g("arq-msg") : "");
      var url = LB.wa(txt);
      msg.innerHTML = 'Abrimos o WhatsApp com sua mensagem pronta. Se não abriu, <a href="' + url + '" target="_blank" rel="noopener" style="border-bottom:1px solid">toque aqui</a>.';
      window.open(url, "_blank", "noopener");
    });
  }

  /* ---------- Catálogo ---------- */
  function catalogo() {
    var grid = $("#catalogo-grid");
    if (!grid || !window.LB_PRODUTOS) return;
    var P = LB_PRODUTOS;
    var keys = ["ambiente", "categoria", "marca", "acabamento", "estilo"];
    var params = new URLSearchParams(location.search);
    keys.forEach(function (k) {
      var sel = $("#f-" + k);
      var vals = k === "marca" ? LB.marcas.slice() : [];
      P.forEach(function (p) { if (p[k] && vals.indexOf(p[k]) < 0) vals.push(p[k]); });
      if (k === "categoria") vals = CATS.slice();
      vals.sort(function (a, b) { return a.localeCompare(b, "pt"); });
      vals.forEach(function (v) { var o = document.createElement("option"); o.value = o.textContent = v; sel.appendChild(o); });
      var q = params.get(k === "categoria" ? "cat" : k);
      if (q) sel.value = q;
      sel.addEventListener("change", render);
    });
    $("#f-limpar").addEventListener("click", function () { keys.forEach(function (k) { $("#f-" + k).value = ""; }); render(); });
    function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
    function render() {
      var f = {}; keys.forEach(function (k) { f[k] = $("#f-" + k).value; });
      var list = P.filter(function (p) { return keys.every(function (k) { return !f[k] || p[k] === f[k]; }); });
      $("#catalogo-count").textContent = list.length + (list.length === 1 ? " produto" : " produtos");
      if (!list.length) {
        grid.innerHTML = '<div class="empty" style="grid-column:1/-1"><p>Ainda não há itens cadastrados com esses filtros.</p><p>Nossa equipe pode indicar opções da boutique.</p><p style="margin-top:28px"><a class="btn" target="_blank" rel="noopener" href="' + LB.wa("Olá, Le Bagno! Procuro: " + keys.map(function (k) { return f[k]; }).filter(Boolean).join(", ")) + '">Consultar a equipe</a></p></div>';
        return;
      }
      grid.innerHTML = list.map(function (p) {
        var msg = "Olá, Le Bagno! Gostaria de um orçamento para: " + p.nome + (p.marca ? " (" + p.marca + ")" : "") + " — código no site: " + p.id + ".";
        var tech = p.tecnico && p.tecnico.length ? '<p class="prod__tech">' + p.tecnico.map(esc).join(" · ") + "</p>" : '<p class="prod__tech">Informações técnicas sob consulta.</p>';
        return '<article class="prod rv in"><div class="frame"><img loading="lazy" src="' + p.img + '" alt="' + esc(p.nome) + '" width="880" height="1100"></div>' +
          '<div class="prod__body"><span class="prod__brand">' + esc(p.marca || "Curadoria Le Bagno") + '</span><h3 class="h3">' + esc(p.nome) + "</h3><p>" + esc(p.descricao) + "</p>" + tech +
          '<div class="prod__tags"><span>' + esc(p.categoria) + "</span><span>" + esc(p.acabamento) + "</span><span>" + esc(p.estilo) + "</span></div>" +
          '<div class="prod__actions"><a class="btn" target="_blank" rel="noopener" href="' + LB.wa(msg) + '">Solicitar orçamento</a></div></div></article>';
      }).join("");
    }
    render();
  }
  var CATS = ["Torneiras e misturadores", "Cubas", "Bacias sanitárias", "Chuveiros", "Ralos", "Banheiras", "Spas e ofurôs",
    "Acessórios de banheiro", "Acessórios de cozinha", "Coifas", "Fornos", "Eletrodomésticos", "Revestimentos", "Porcelanatos", "Puxadores", "Acabamentos especiais"];

  /* ---------- Inspirações: filtro + ampliação ---------- */
  function galeria() {
    var gal = $("#galeria");
    if (!gal) return;
    var items = $$(".gal", gal);
    $$(".tabs button").forEach(function (b) {
      b.addEventListener("click", function () {
        var f = b.getAttribute("data-f");
        $$(".tabs button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        items.forEach(function (it) { it.hidden = !(f === "todos" || it.getAttribute("data-cat").split(" ").indexOf(f) >= 0); });
      });
    });
    var lb = $(".lb"), img = $("img", lb), cap = $("figcaption", lb), cur = 0, lastFocus;
    function vis() { return items.filter(function (i) { return !i.hidden; }); }
    function show(i) {
      var v = vis(); cur = (i + v.length) % v.length;
      var src = $("img", v[cur]);
      img.src = src.src; img.alt = src.alt; cap.textContent = v[cur].getAttribute("data-title");
    }
    items.forEach(function (it) {
      $("button", it).addEventListener("click", function () {
        lastFocus = document.activeElement; lb.hidden = false; document.body.style.overflow = "hidden";
        show(vis().indexOf(it)); $(".lb__x", lb).focus();
      });
    });
    function close() { lb.hidden = true; document.body.style.overflow = ""; if (lastFocus) lastFocus.focus(); }
    $(".lb__x", lb).addEventListener("click", close);
    $(".lb__p", lb).addEventListener("click", function () { show(cur - 1); });
    $(".lb__n", lb).addEventListener("click", function () { show(cur + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (lb.hidden) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(cur - 1);
      if (e.key === "ArrowRight") show(cur + 1);
    });
  }

  doc.classList.add("js");
  document.addEventListener("DOMContentLoaded", function () {
    bindLinks(); intro(); header(); catalogo(); reveal(); parallax(); videos(); carousel(); archForm(); galeria();
  });
})();
