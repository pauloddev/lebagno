/* =========================================================
   LE BAGNO — DADOS INSTITUCIONAIS CENTRALIZADOS
   Edite aqui telefones, endereços, links e mensagens.
   Todo o site lê estes valores (atributos data-bind).
   ========================================================= */
window.LB = {
  nome: "Le Bagno",
  ceo: "Fernanda Lima",
  cnpj: "30.865.325/0001-06",
  email: "lebagnopb@gmail.com",

  // WhatsApp comercial (único número de WhatsApp informado — unidade Campina Grande).
  // Se João Pessoa tiver um WhatsApp próprio, coloque-o em "whatsappPrincipal".
  whatsappPrincipal: "5583993818544",

  unidades: {
    jp: {
      nome: "Le Bagno João Pessoa",
      endereco: "Avenida Monteiro da Franca, 1592 – Manaíra, João Pessoa – PB",
      telefone: "(83) 3508-0048",
      tel: "+558335080048",
      instagram: "https://www.instagram.com/lebagno/",
      instagramUser: "@lebagno",
      horario: ["Segunda a sexta: 09h às 18h", "Sábado: 09h às 13h", "Domingo: fechado"]
    },
    cg: {
      nome: "Le Bagno Campina Grande",
      endereco: "Rua Raimundo Alves da Silva, 333 – Centro, Campina Grande – PB",
      telefone: "(83) 3201-0671",
      tel: "+558332010671",
      whatsapp: "5583993818544",
      instagram: "https://www.instagram.com/lebagnocg/",
      instagramUser: "@lebagnocg",
      horario: ["Segunda a sexta: 09h às 18h", "Sábado: 09h às 13h", "Domingo: fechado"]
    }
  },

  marcas: ["Doka", "Rubinettos", "Tramontina", "Debacco", "Invita", "Portobello",
           "Portinari", "Villagres", "Ceusa", "Deca", "Franke", "Zen Design"],

  mensagens: {
    geral: "Olá, Le Bagno! Vim pelo site e gostaria de falar com um especialista.",
    estoque: "Olá, Le Bagno! Gostaria de consultar os produtos a pronta entrega.",
    banho: "Olá, Le Bagno! Quero conhecer as soluções para banheiro.",
    cozinha: "Olá, Le Bagno! Quero conhecer as soluções para cozinha.",
    cg: "Olá, Le Bagno Campina Grande! Vim pelo site e gostaria de atendimento."
  }
};

LB.wa = function (msg, numero) {
  return "https://wa.me/" + (numero || LB.whatsappPrincipal) + "?text=" + encodeURIComponent(msg || LB.mensagens.geral);
};
LB.maps = function (endereco) {
  return "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(endereco);
};
