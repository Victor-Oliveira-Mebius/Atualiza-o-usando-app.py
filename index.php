<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sistemas ERP para Mercados | Soluções em Gestão e Automação</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Fontes -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100..900&display=swap" rel="stylesheet">

  <!-- Font Awesome -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">

  <!-- SEO -->
  <meta name="description" content="Descubra os melhores sistemas ERP para mercados. Soluções completas para supermercados, minimercados e mercearias. Aumente sua produtividade com sistemas modernos, fáceis e integrados.">
  <meta name="keywords" content="sistema para mercados, sistemas ERP para mercado, melhores sistemas para mercados, melhores sistemas ERP para mercado, sistema para supermercado, sistema para minimercado, ERP para mercearia, software para gestão de mercado">
  <meta name="author" content="Universo Sistemas">

  <!-- Open Graph -->
  <meta property="og:title" content="Sistemas ERP para Mercados | Universo Sistemas">
  <meta property="og:description" content="Soluções completas e inteligentes em sistemas ERP para o seu mercado. Veja por que somos referência em tecnologia para o varejo.">
  <meta property="og:image" content="https://siteuniversosistemas.com/static/img-sistema/banner-sistema-erp.jpg">
  <meta property="og:url" content="https://siteuniversosistemas.com/">
  <meta property="og:type" content="website">

  <link rel="canonical" href="https://siteuniversosistemas.com/">
  <link rel="icon" href="/favicon.ico" type="image/x-icon">

  <!-- Estilos personalizados -->
  <style>
    html { font-size: 16px; font-family: "Roboto", sans-serif; }

    .product-image-left{
      /* Caminho estático da imagem de fundo */
      background: url("/static/img-sistema/boneco+logo.png") center/cover no-repeat;
      min-height: 480px;
      transition: transform .3s ease;
    }
    .product-image-left:hover { transform: scale(1.02); }

    .feature-icon { transition: all .3s ease; }
    .feature-card:hover .feature-icon { transform: rotate(10deg) scale(1.1); color:#3b82f6; }

    .hero-image{ width:100%; min-height:60vh; height:auto; background-size:cover; background-position:center; background-repeat:no-repeat; }
    @media (min-width:768px){ .hero-image{ min-height:80vh; } }

    .stat-card{ transition:all .3s ease; padding:1.5rem; }
    .stat-card:hover{ transform:translateY(-5px); box-shadow:0 12px 18px -6px rgba(0,0,0,.1); }

    .counter{ font-family:Arial, sans-serif; font-weight:bold; font-size:2rem; }

    .fade-in-up{ opacity:0; transform:translateY(30px); transition:all .6s ease-in-out; }
    .fade-in-up.visible{ opacity:1; transform:translateY(0); }

    #hero.opacity-0{ opacity:0; }
    #hero{ opacity:1; transition:opacity .7s; }

    .segment-card{ box-shadow:rgba(0,0,0,.16) 0 1px 4px, rgb(51,51,51) 0 0 0 3px; }
    .feature-card{ background:#fff; padding:1rem; border-radius:.5rem; box-shadow:0 2px 4px rgba(0,0,0,.1); transition:all .3s ease; }
    .feature-card:hover{ box-shadow:0 5px 15px rgba(0,0,0,.2); transform:translateY(-3px); }

    .card-hover{ transition:all .3s ease; }
    .card-hover:hover{ transform:translateY(-5px); box-shadow:0 15px 25px -10px rgba(0,0,0,.15); }

    .slider-track{ display:flex; white-space:nowrap; animation:scroll 20s linear infinite; }
    @keyframes scroll{ 0%{ transform:translateX(0);} 100%{ transform:translateX(-50%);} }
  </style>
</head>
<body class="bg-white text-gray-800">

  <!-- Header Desktop -->
  <header class="bg-white sticky top-0 z-50 h-20 hidden md:flex shadow-md transition-shadow duration-300">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center h-full">
      <div class="flex items-center">
        <a href="/index.html" class="transition transform hover:scale-105 duration-300">
          <img src="/static/img-sistema/imagem-chat2.png" alt="Logo Universo Sistemas" class="h-auto max-h-48 w-auto max-w-[160px] sm:max-w-[200px] lg:max-w-[250px]" />
        </a>
      </div>
      <nav>
        <div class="flex items-center space-x-6">
          <a href="/quem-somos.html" class="text-gray-700 hover:text-blue-500 transition duration-300">Quem somos</a>
          <a href="/solucoes.html"   class="text-gray-700 hover:text-blue-500 transition duration-300">Soluções</a>
        </div>
      </nav>
    </div>
  </header>

  <!-- Header Mobile -->
  <header class="bg-white sticky top-0 z-50 h-20 flex items-center justify-between px-4 md:hidden">
    <a href="/index.html">
      <img src="/static/img-sistema/imagem-chat2.png" alt="Logo Universo Sistemas" class="h-auto max-h-48 w-auto max-w-[160px] sm:max-w-[200px] lg:max-w-[250px]"/>
    </a>
    <button id="mobileMenuBtn" class="text-3xl focus:outline-none">☰</button>
  </header>

  <!-- Hero -->
  <section id="hero" class="hero-image text-white flex items-center justify-start px-4 md:px-8 min-h-[60vh] md:min-h-[80vh] lg:min-h-[700px] relative">
    <img id="hero-bg"
         src="/static/img-sistema/parte-interna.png"
         alt="Imagem de Apresentação do Mercado"
         class="absolute inset-0 w-full h-full object-cover object-top md:object-[center_20%] z-0" />
    <div id="hero-overlay" class="absolute inset-0 pointer-events-none z-10" style="background:none;"></div>

    <!-- Botão flutuante: WhatsApp -->
    <div id="whatsapp-flutuante" class="fixed right-6 bottom-24 z-50 transition-opacity duration-500 opacity-100">
      <a href="https://wa.me/5566999624725?text=Ol%C3%A1!%20Quero%20ajuda%20para%20escolher%20o%20sistema." target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
        <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-green-500 hover:bg-green-600 shadow-lg hover:shadow-xl flex items-center justify-center transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-green-300">
          <i class="fa-brands fa-whatsapp text-white text-xl"></i>
        </div>
      </a>
    </div>

    <!-- Botão flutuante (direto para WhatsApp) -->
    <div id="botao-flutuante" class="fixed right-6 bottom-6 z-50 transition-opacity duration-500 opacity-100">
      <a href="https://wa.me/5566999624725?text=Ol%C3%A1!%20Quero%20ajuda%20para%20escolher%20o%20sistema." target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
        <button class="bg-cyan-600 hover:bg-cyan-800 text-white font-semibold py-2 px-4 text-sm sm:py-3 sm:px-6 sm:text-base rounded-full shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-cyan-300 flex items-center gap-2">
          <i class="fa-brands fa-whatsapp text-white text-lg"></i> Fale conosco
        </button>
      </a>
    </div>
  </section>

  <!-- Menu Mobile -->
  <div id="mobileMenu" class="bg-white fixed top-20 left-0 w-full hidden flex-col shadow-md z-50 md:hidden">
    <a href="/solucoes.html"   class="block px-4 py-3 border-b border-gray-200">Soluções</a>
    <a href="/quem-somos.html" class="block px-4 py-3 border-b border-gray-200">Quem somos</a>
  </div>

  <main class="container mx-auto px-4 py-12">
    <section id="solutions" class="mb-20">
      <div class="flex flex-col lg:flex-row items-center gap-12">
        <div class="product-image-left w-full lg:w-1/2 rounded-xl shadow-xl"></div>
        <div class="w-full lg:w-2/2">
          <h2 class="text-2xl font-bold text-gray-800 mb-2">Sistema Completo para sua Empresa</h2>
          <p class="text-gray-600 mb-6 font-playfair text-xl">Você já imaginou controlar vendas, estoque e clientes em tempo real sem perder horas com planilhas?</p>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition">
              <i class="fas fa-shield-alt text-3xl text-blue-500 mb-4"></i>
              <h3 class="text-lg font-playfair font-bold mb-2">Anos no mercado</h3>
              <p class="text-gray-600">A Universo Sistemas está no mercado há mais de 20 anos, oferecendo soluções de alta qualidade.</p>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition">
              <i class="fas fa-user-friends text-3xl text-blue-500 mb-4"></i>
              <h3 class="text-lg font-playfair font-bold mb-2">Apoio Personalizado</h3>
              <p class="text-gray-600">Atendimento próximo e ajustado às necessidades de cada cliente.</p>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition">
              <i class="fas fa-laptop-code text-3xl text-blue-500 mb-4"></i>
              <h3 class="text-lg font-playfair font-bold mb-2">Atualizações Constantes</h3>
              <p class="text-gray-600">Sistema sempre atualizado com novas funções e melhorias.</p>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition">
              <i class="fas fa-rocket text-3xl text-blue-500 mb-4"></i>
              <h3 class="text-lg font-playfair font-bold mb-2">Performance e Velocidade</h3>
              <p class="text-gray-600">Navegação rápida com foco em eficiência e produtividade.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Segmentos -->
  <section class="py-6 bg-gray-50">
    <div class="container mx-auto flex flex-col lg:flex-row items-center gap-6 px-4 sm:px-6 lg:px-8">
      <div class="w-full lg:w-1/2 flex justify-center lg:justify-start px-4">
        <img src="/static/img-sistema/imagem-super.jpg" alt="Imagem PDV compras" class="w-full max-w-md h-auto object-contain rounded-xl shadow-md" />
      </div>

      <div class="w-full lg:w-1/2">
        <h2 class="text-3xl font-bold text-gray-900 mb-6 text-center">Segmentos que atendemos</h2>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 w-full">
          <div class="bg-white p-4 rounded-xl text-center shadow segment-card">
            <img src="/static/img-sistema/market_16684068.png" alt="Supermercado" class="mx-auto h-20 mb-3">
            <h3 class="text-base font-semibold text-gray-800 mb-2">SUPERMERCADOS</h3>
            <a href="/solucoes.html">
              <button class="bg-blue-200 text-black px-4 py-1 rounded-md hover:bg-blue-300 transition text-sm">SAIBA MAIS</button>
            </a>
          </div>

          <div class="bg-white p-4 rounded-xl text-center shadow segment-card">
            <img src="/static/img-sistema/grocery_15170859.png" alt="Mercado" class="mx-auto h-20 mb-3">
            <h3 class="text-base font-semibold text-gray-800 mb-2">MERCADO</h3>
            <a href="/solucoes.html">
              <button class="bg-blue-200 text-black px-4 py-1 rounded-md hover:bg-blue-300 transition text-sm">SAIBA MAIS</button>
            </a>
          </div>

          <div class="bg-white p-4 rounded-xl text-center shadow segment-card">
            <img src="/static/img-sistema/mannequin_15265532.png" alt="Lojas" class="mx-auto h-20 mb-3">
            <h3 class="text-base font-semibold text-gray-800 mb-2">LOJAS</h3>
            <a href="/solucoes.html">
              <button class="bg-blue-200 text-black px-4 py-1 rounded-md hover:bg-blue-300 transition text-sm">SAIBA MAIS</button>
            </a>
          </div>

          <div class="bg-white p-4 rounded-xl text-center shadow segment-card">
            <img src="/static/img-sistema/restaurant_497823.png" alt="Restaurante" class="mx-auto h-20 mb-3">
            <h3 class="text-base font-semibold text-gray-800 mb-2">RESTAURANTES</h3>
            <a href="/solucoes.html">
              <button class="bg-blue-200 text-black px-4 py-1 rounded-md hover:bg-blue-300 transition text-sm">SAIBA MAIS</button>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Seção de vendas -->
  <section class="bg-gradient-to-r from-blue-50 to-gray-50 py-12 md:py-16 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
      <div>
        <div class="inline-block bg-red-100 border-l-4 border-red-600 mb-8 p-4 text-left w-full">
          <div class="flex items-center">
            <svg class="h-6 w-6 text-red-600 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
            <span class="font-bold text-red-800">ATENÇÃO DONOS DE MERCADO EM MATO GROSSO</span>
          </div>
        </div>

        <div class="mb-6">
          <h2 class="text-2xl md:text-3xl font-extrabold text-gray-600 mb-4">❌ Sistema lento e confuso?</h2>
        </div>

        <div class="text-gray-800 mb-6 p-4 rounded-lg shadow-md bg-gray-50">
          <p class="text-lg md:text-xl font-medium">✅ Tenha controle total das vendas e estoque, com relatórios automáticos e suporte ágil.</p>
          <p class="text-gray-600 mt-2">Não fique para trás. <span class="font-semibold text-yellow-600">A concorrência já está usando automação para vender mais!!</span></p>
        </div>

        <ul class="grid grid-cols-1 gap-4 mb-10 text-left">
          <li class="flex items-start bg-white p-4 rounded-lg shadow-sm border border-gray-100"><i class="h-6 w-6 text-green-500 fa-solid fa-check mt-1 mr-3"></i><span class="text-gray-800 font-medium">Controle de estoque em tempo real - nunca mais perca vendas por falta de produtos</span></li>
          <li class="flex items-start bg-white p-4 rounded-lg shadow-sm border border-gray-100"><i class="h-6 w-6 text-green-500 fa-solid fa-check mt-1 mr-3"></i><span class="text-gray-800 font-medium">Relatórios automáticos que mostram EXATAMENTE onde está seu lucro</span></li>
          <li class="flex items-start bg-white p-4 rounded-lg shadow-sm border border-gray-100"><i class="h-6 w-6 text-green-500 fa-solid fa-check mt-1 mr-3"></i><span class="text-gray-800 font-medium">Suporte que resolve seus problemas na hora</span></li>
          <li class="flex items-start bg-white p-4 rounded-lg shadow-sm border border-gray-100"><i class="h-6 w-6 text-green-500 fa-solid fa-check mt-1 mr-3"></i><span class="text-gray-800 font-medium">Sistema rápido que não trava mesmo no horário de pico</span></li>
        </ul>

        <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-6 shadow-md">
          <div class="flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="text-left">
              <h3 class="text-lg font-bold text-yellow-800">SOLICITE AGORA</h3>
              <p class="text-yellow-700"><span class="font-bold">uma demonstração gratuita</span></p>
            </div>
            <a href="/solucoes.html" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 md:py-4 md:px-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300 transform hover:scale-105 whitespace-nowrap">Escolha seu sistema!</a>
          </div>
        </div>
      </div>

      <div class="flex justify-center lg:justify-end">
        <img src="/static/img-sistema/grafico-universo-sistemas.png" alt="Imagem pdv caixa compras" class="w-full max-w-md h-auto object-contain rounded-xl shadow-md">
      </div>
    </div>
  </section>

  <!-- Sobre -->
  <section id="about" class="mb-20">
    <div class="text-center mb-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-2">Sobre a Nossa Empresa</h2>
      <div class="w-20 h-1 bg-blue-600 mx-auto"></div>
    </div>

    <div class="flex flex-col lg:flex-row gap-12">
      <div class="w-full lg:w-1/2 px-4 sm:px-6">
        <h3 class="text-2xl font-bold text-gray-800 mb-2">Expertise em Sistemas Comerciais</h3>
        <p class="text-gray-600 mb-6 leading-relaxed">Há mais de 20 anos, somos referência em soluções tecnológicas para o comércio de mercadorias, ajudando empresas a automatizar processos, reduzir custos e aumentar resultados.</p>
        <p class="text-gray-600 mb-6 leading-relaxed">Nossa equipe multidisciplinar alia conhecimento técnico aprofundado e experiência prática no varejo e atacado, oferecendo muito mais do que softwares: entregamos parcerias estratégicas que impulsionam o crescimento do seu negócio.</p>
        <div class="bg-blue-50 p-6 rounded-lg border-l-4 border-blue-600">
          <p class="text-gray-700 italic">Com atendimento ágil, suporte especializado e foco em inovação, estamos prontos para levar sua empresa ao próximo nível. Conte conosco para transformar desafios em oportunidades reais.</p>
        </div>
      </div>

      <div class="w-full lg:w-1/2">
        <img src="/static/img-sistema/telas-de-graficos.png" class="rounded-xl shadow-lg w-full max-w-full h-auto object-contain" alt="Telas de gráficos">
      </div>
    </div>
  </section>

  <!-- CTA final -->
  <section class="bg-blue-800 text-white py-12 px-4">
    <div class="max-w-4xl mx-auto text-center">
      <div class="text-5xl mb-4 text-white"><i class="fa-solid fa-clipboard-check"></i></div>
      <h2 class="text-2xl md:text-3xl font-bold">Qual sistema é o melhor para você?</h2>
      <p class="mt-3 text-blue-100">Fale com nosso time e receba uma recomendação gratuita.</p>
      <a href="https://wa.me/5566999624725?text=Ol%C3%A1!%20Quero%20ajuda%20para%20escolher%20o%20sistema." target="_blank" rel="noopener" aria-label="Falar no WhatsApp" class="inline-flex items-center gap-2 mt-6 bg-white text-blue-700 hover:bg-blue-50 px-6 py-3 rounded-lg shadow">
        <i class="fa-brands fa-whatsapp"></i> Fale Conosco
      </a>
    </div>
  </section>

  <!-- Logos (slider) -->
  <div class="bg-white shadow-lg rounded-xl py-8 px-4 mx-auto max-w-7xl mb-16">
    <div class="text-center mb-6">
      <h2 class="text-xl md:text-2xl font-bold text-gray-800">Empresas que confiam em nosso trabalho</h2>
    </div>

    <div class="overflow-hidden relative">
      <div class="slider-track">
        <!-- Dobre os itens para rolagem contínua -->
        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 1" class="h-20 object-contain" /></div>
        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 2" class="h-20 object-contain" /></div>
        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 3" class="h-20 object-contain" /></div>
        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 4" class="h-20 object-contain" /></div>

        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 1" class="h-20 object-contain" /></div>
        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 2" class="h-20 object-contain" /></div>
        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 3" class="h-20 object-contain" /></div>
        <div class="inline-flex items-center justify-center min-w-[250px] px-4"><img src="/static/img-sistema/imagem-chat2.png" alt="Logo 4" class="h-20 object-contain" /></div>
      </div>
    </div>
  </div>

  <!-- Cards finais -->
  <section class="mb-20">
    <div class="flex flex-col lg:flex-row items-stretch gap-6 px-4 sm:px-6">
      <div class="card-hover bg-gray-800 text-white rounded-xl p-5 lg:w-1/3 w-full" style="box-shadow:rgba(58,58,68,.25) 0 20px 40px -12px inset, rgba(95,85,85,.3) 0 12px 24px -18px inset;">
        <h3 class="text-2xl font-bold mb-2">ERP Empresarial</h3>
        <p class="text-gray-300 mb-4 text-sm">Solução integrada para controlar e automatizar os setores financeiro, fiscal, RH e operações da sua empresa, com dados centralizados e em tempo real.</p>
        <ul class="space-y-2 mb-6 text-sm">
          <li class="flex items-start"><i class="fas fa-check-circle text-blue-400 mt-1 mr-2"></i><span><strong>Controle financeiro e contábil</strong> — fluxo de caixa, contas a pagar/receber e conciliações bancárias.</span></li>
          <li class="flex items-start"><i class="fas fa-check-circle text-blue-400 mt-1 mr-2"></i><span><strong>Emissão de documentos fiscais</strong> — NFe, NFCe, CT-e, integração com SEFAZ e contabilidade.</span></li>
          <li class="flex items-start"><i class="fas fa-check-circle text-blue-400 mt-1 mr-2"></i><span><strong>Contas a Pagar e Receber</strong> — automatize lançamentos e gere relatórios em tempo real.</span></li>
        </ul>
        <a href="/solucoes.html" class="text-blue-400 hover:text-blue-300 font-medium text-sm flex items-center">Saiba mais <i class="fas fa-arrow-right ml-2"></i></a>
      </div>

      <div class="card-hover bg-blue-600 text-white rounded-xl p-5 lg:w-1/3" style="box-shadow:rgba(17,3,105,.25) 0 20px 40px -12px inset, rgba(248,248,248,.3) 0 12px 24px -18px inset;">
        <h3 class="text-2xl font-bold mb-2">e-Commerce</h3>
        <p class="text-blue-100 mb-4 text-sm">Plataforma completa de vendas online com automações inteligentes, integração a marketplaces e controle centralizado de pedidos, pagamentos e logística.</p>
        <ul class="space-y-2 mb-6 text-sm">
          <li class="flex items-start"><i class="fas fa-check-circle text-white mt-1 mr-2"></i><span><strong>Loja virtual personalizada</strong> — vitrines modernas com checkout rápido e seguro.</span></li>
          <li class="flex items-start"><i class="fas fa-check-circle text-white mt-1 mr-2"></i><span><strong>Integração com TEF/SITEF</strong> — cartões, PIX e boleto.</span></li>
          <li class="flex items-start"><i class="fas fa-check-circle text-white mt-1 mr-2"></i><span><strong>Relatórios de conversão</strong> — acompanhe métricas para aumentar vendas.</span></li>
        </ul>
        <a href="/solucoes.html" class="text-white hover:text-blue-100 font-medium text-sm flex items-center">Saiba mais <i class="fas fa-arrow-right ml-2"></i></a>
      </div>

      <div class="card-hover bg-white rounded-xl p-5 lg:w-1/3 w-full" style="box-shadow:rgba(158,158,209,.25) 0 20px 40px -12px inset, rgba(150,147,147,.3) 0 12px 24px -18px inset;">
        <h3 class="text-2xl font-bold text-gray-800 mb-2">Parceria</h3>
        <p class="text-gray-600 mb-4 text-sm">Parceria com a <strong>Orgamec</strong> para oferecer mais segurança fiscal aos nossos clientes.</p>
        <ul class="space-y-2 mb-6 text-sm">
          <li class="flex items-start"><i class="fas fa-check-circle text-blue-600 mt-1 mr-2"></i><span><strong>Análise de rentabilidade por setor</strong> — descubra as áreas com mais retorno.</span></li>
          <li class="flex items-start"><i class="fas fa-check-circle text-blue-600 mt-1 mr-2"></i><span><strong>Atendimento consultivo</strong> — apoio contábil próximo e humano.</span></li>
          <li class="flex items-start"><i class="fas fa-check-circle text-blue-600 mt-1 mr-2"></i><span><strong>Integração direta</strong> — sincronização para evitar erros e retrabalho.</span></li>
        </ul>
        <a href="https://br.linkedin.com/company/orgamecassessoriacontabil" target="_blank" class="text-blue-600 hover:text-blue-700 font-medium text-sm flex items-center">Saiba mais <i class="fas fa-arrow-right ml-2"></i></a>
      </div>
    </div>
  </section>

  <!-- Rodapé -->
  <footer class="bg-gray-900 text-white py-12">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
        <div>
          <h3 class="text-xl font-bold mb-4 flex items-center justify-center md:justify-start">
            <img src="/static/img-sistema/imagem-chat2.png" class="h-14 md:h-48 w-auto object-contain transition hover:scale-110 duration-300 mx-auto md:mx-0" alt="Universo Sistemas">
          </h3>
        </div>

        <div>
          <h4 class="font-bold mb-4 text-lg">Produtos</h4>
          <ul class="space-y-2">
            <li><span class="text-gray-400">SysGestão</span></li>
            <li><span class="text-gray-400">SysErp</span></li>
            <li><span class="text-gray-400">SysVendas</span></li>
            <li><span class="text-gray-400">SysNop</span></li>
          </ul>
        </div>

        <div>
          <h4 class="font-bold mb-4 text-lg">Links Úteis</h4>
          <ul class="space-y-2">
            <li><a href="https://www.facebook.com/people/Universo-Sistemas-Sinop-e-Regi%C3%A3o/100083637337710/?mibextid" class="text-gray-400 hover:text-white">Facebook</a></li>
            <li><a href="https://www.instagram.com/universo_sistemas/" class="text-gray-400 hover:text-white">Instagram</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-bold mb-4 text-lg">Contato</h4>
          <address class="not-italic text-gray-400">
            <p class="mb-2">
              <a href="https://www.google.com/maps/place/11%C2%B052'17.6%22S+55%C2%B031'13.8%22W/" class="hover:text-white">
                <i class="fas fa-map-marker-alt text-blue-400 mr-2"></i>Localização
              </a>
            </p>
            <p class="mb-2"><i class="fas fa-phone-alt text-blue-400 mr-2"></i>+55 66 99631-0123</p>
            <p class="mb-2"><i class="fas fa-envelope text-blue-400 mr-2"></i>atendimento@universosistemas.inf.br</p>
          </address>
          <div class="flex space-x-4 mt-4">
            <a href="https://www.facebook.com/people/Universo-Sistemas-Sinop-e-Regi%C3%A3o/100083637337710/?mibextid" class="text-gray-400 hover:text-white"><i class="fab fa-facebook-f"></i></a>
            <a href="https://wa.me/5566999624725" class="text-gray-400 hover:text-white"><i class="fab fa-whatsapp"></i></a>
            <a href="https://www.instagram.com/universo_sistemas/" class="text-gray-400 hover:text-white"><i class="fab fa-instagram"></i></a>
          </div>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-center text-gray-500">
        <p>&copy; <span id="ano"></span> Universo Sistemas</p>
      </div>
    </div>
  </footer>

  <script>
    // Overlay do hero
    (function(){
      const overlay = document.getElementById('hero-overlay');
      if (overlay) overlay.style.background = 'rgba(0,0,0,0.3)'; // 30% escuro
    })();

    // Inatividade: apaga botões flutuantes
    (function(){
      const flutuantes = [document.getElementById('botao-flutuante'), document.getElementById('whatsapp-flutuante')].filter(Boolean);
      const INACTIVE_MS = 3000, ACTIVE_OP = 1, DIM_OP = 0.06;
      let timer = null;
      function setOpacityAll(v){ flutuantes.forEach(el => el.style.opacity = String(v)); }
      function userActivity(){ setOpacityAll(ACTIVE_OP); if (timer) clearTimeout(timer); timer = setTimeout(()=>setOpacityAll(DIM_OP), INACTIVE_MS); }
      ['scroll','mousemove','touchstart','keydown'].forEach(evt => window.addEventListener(evt, userActivity, {passive:true}));
      userActivity();
    })();

    // Menu mobile
    (function(){
      const menuBtn = document.getElementById('mobileMenuBtn');
      const menuEl  = document.getElementById('mobileMenu');
      function setMenuOpen(isOpen){ if(!menuEl) return; menuEl.classList.toggle('hidden', !isOpen); document.body.style.overflow = isOpen ? 'hidden' : ''; }
      if (menuBtn && menuEl){
        menuBtn.addEventListener('click', (e)=>{ e.stopPropagation(); setMenuOpen(menuEl.classList.contains('hidden')); });
        menuEl.querySelectorAll('a').forEach(a => a.addEventListener('click', ()=>setMenuOpen(false)));
        document.addEventListener('click', (e)=>{ if(menuEl.classList.contains('hidden')) return; const inside=menuEl.contains(e.target); const btn=menuBtn.contains(e.target); if(!inside && !btn) setMenuOpen(false); }, {passive:true});
        document.addEventListener('keydown', (e)=>{ if(e.key==='Escape') setMenuOpen(false); });
        window.addEventListener('resize', ()=>{ if (window.innerWidth >= 768) setMenuOpen(false); });
      }
    })();

    // Ano dinâmico
    (function(){
      const ano = document.getElementById('ano');
      if (ano) ano.textContent = new Date().getFullYear();
    })();
  </script>
</body>
</html>
