<!DOCTYPE html>
<html lang="tr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS INTELLIGENCE | V10 MASTER</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link
        href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;700&display=swap"
        rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">

    <style>
        :root {
            /* Core Palette */
            --bg-deep: #050511;
            --bg-glass: rgba(20, 30, 50, 0.4);
            --bg-glass-hover: rgba(30, 45, 70, 0.6);
            --border: rgba(100, 116, 139, 0.15);

            /* Accents */
            --primary: #3b82f6;
            --primary-glow: rgba(59, 130, 246, 0.5);
            --accent: #6366f1;
            --cyan: #06b6d4;
            --danger: #ef4444;
            --success: #10b981;
            --gold: #f59e0b;
            --purple: #d946ef;

            /* Text */
            --text-main: #f8fafc;
            --text-dim: #94a3b8;
        }

        /* --- GLOBAL & ANIMATIONS --- */
        * {
            box-sizing: border-box;
        }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
            margin: 0;
            overflow-x: hidden;
            background-image:
                radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.08) 0%, transparent 40%),
                linear-gradient(to bottom, #020617 0%, #0b0f19 100%);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes pulseGlow {
            0% {
                box-shadow: 0 0 5px var(--primary-glow);
            }

            50% {
                box-shadow: 0 0 20px var(--primary-glow);
            }

            100% {
                box-shadow: 0 0 5px var(--primary-glow);
            }
        }

        .fade-in {
            animation: fadeIn 0.8s ease-out forwards;
            opacity: 0;
        }

        .delay-100 {
            animation-delay: 0.1s;
        }

        .delay-200 {
            animation-delay: 0.2s;
        }

        .delay-300 {
            animation-delay: 0.3s;
        }

        /* --- UTILS --- */
        .glass-panel {
            background: var(--bg-glass);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }

        .glass-panel:hover {
            border-color: rgba(255, 255, 255, 0.2);
            background: var(--bg-glass-hover);
            transform: translateY(-4px);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        }

        h1,
        h2,
        h3,
        h4 {
            margin: 0;
        }

        .font-tech {
            font-family: 'Rajdhani', sans-serif;
        }

        .font-mono {
            font-family: 'JetBrains Mono', monospace;
        }

        /* --- HEADER --- */
        header {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(5, 5, 17, 0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            padding: 1rem 0;
        }

        .header-inner {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .brand-logo {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            background: linear-gradient(90deg, #fff, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .status-pill {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--success);
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.2);
            padding: 6px 12px;
            border-radius: 99px;
            font-family: 'JetBrains Mono', monospace;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            background: var(--success);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--success);
            animation: pulseGlow 2s infinite;
        }

        /* --- LAYOUT --- */
        .main-container {
            max-width: 1400px;
            margin: 3rem auto;
            padding: 0 2rem;
            display: flex;
            flex-direction: column;
            gap: 4rem;
        }

        .section-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 1rem;
        }

        .section-title {
            font-size: 2rem;
            font-weight: 700;
            color: #fff;
            letter-spacing: 1px;
        }

        .section-icon {
            font-size: 1.5rem;
            color: var(--accent);
        }

        /* --- 1. DATA FUNNEL --- */
        .funnel-grid {
            display: grid;
            grid-template-columns: 1fr auto 1fr auto 1fr;
            align-items: center;
            gap: 1rem;
        }

        .funnel-card {
            padding: 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .funnel-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, currentColor, transparent);
        }

        .count-val {
            font-size: 3.5rem;
            font-weight: 700;
            line-height: 1;
            margin-bottom: 0.5rem;
            font-family: 'Rajdhani', sans-serif;
        }

        .count-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--text-dim);
            font-weight: 600;
        }

        .funnel-arrow i {
            font-size: 1.5rem;
            color: var(--border);
            transition: 0.3s;
        }

        .funnel-grid:hover .funnel-arrow i {
            color: var(--primary);
            transform: translateX(5px);
        }

        .stat-detail {
            margin-top: 1rem;
            text-align: left;
            background: rgba(0, 0, 0, 0.2);
            padding: 10px;
            border-radius: 8px;
            font-size: 0.85rem;
        }

        .stat-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 4px;
            color: var(--text-dim);
        }

        .stat-row b {
            color: #fff;
        }

        /* --- 2. TECH STACK --- */
        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .tech-item h4 {
            color: #fff;
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .tech-item p {
            font-size: 0.95rem;
            color: var(--text-dim);
            line-height: 1.5;
            margin: 0;
        }

        .tech-tags {
            display: flex;
            gap: 10px;
            margin-top: 1rem;
            flex-wrap: wrap;
        }

        .tag {
            background: rgba(255, 255, 255, 0.05);
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            color: var(--text-dim);
            border: 1px solid transparent;
            transition: 0.2s;
        }

        .tech-item:hover .tag {
            border-color: var(--primary);
            color: var(--primary);
        }

        /* --- 3. NEXUS AI TERMINAL --- */
        .ai-grid {
            display: grid;
            grid-template-columns: 350px 1fr;
            gap: 2rem;
            min-height: 450px;
        }

        .terminal-window {
            background: #0d0f1a;
            border: 1px solid var(--border);
            border-radius: 12px;
            font-family: 'JetBrains Mono', monospace;
            padding: 1.5rem;
            position: relative;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .terminal-header {
            display: flex;
            gap: 6px;
            margin-bottom: 1.5rem;
        }

        .dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            opacity: 0.7;
        }

        .dot-r {
            background: #ff5f56;
        }

        .dot-y {
            background: #ffbd2e;
        }

        .dot-g {
            background: #27c93f;
        }

        .terminal-content {
            flex: 1;
            color: var(--success);
            font-size: 0.9rem;
            line-height: 1.6;
        }

        .cursor {
            display: inline-block;
            width: 8px;
            height: 16px;
            background: var(--success);
            animation: blink 1s infinite;
            vertical-align: middle;
        }

        @keyframes blink {
            50% {
                opacity: 0;
            }
        }

        .ai-visual {
            position: relative;
            padding: 1rem;
            display: flex;
            flex-direction: column;
        }

        .ai-verdict {
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 10;
            background: rgba(217, 70, 239, 0.1);
            border: 1px solid var(--purple);
            color: var(--purple);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            letter-spacing: 1px;
            box-shadow: 0 0 15px rgba(217, 70, 239, 0.2);
        }

        /* --- 4. CHARTS GRID (FULL RESTORE) --- */
        .charts-wrapper {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .charts-secondary {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }

        .chart-box {
            padding: 1rem;
            height: 350px;
            position: relative;
        }

        /* --- 5. STRATEGY (FULL RESTORE) --- */
        .strategy-intro {
            color: var(--text-dim);
            margin-bottom: 2rem;
            font-size: 1.1rem;
            line-height: 1.6;
            max-width: 900px;
        }

        .strat-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
        }

        .strat-card {
            padding: 2rem;
            border-top: 4px solid transparent;
        }

        .strat-card.risk {
            border-top-color: var(--danger);
        }

        .strat-card.growth {
            border-top-color: var(--success);
        }

        .strat-card.prod {
            border-top-color: var(--primary);
        }

        .strat-card.cont {
            border-top-color: var(--accent);
        }

        .strat-card.crm {
            border-top-color: var(--gold);
        }

        .strat-card.tech {
            border-top-color: var(--cyan);
        }

        .strat-head {
            display: flex;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            align-items: flex-start;
        }

        .strat-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #fff;
            font-family: 'Rajdhani', sans-serif;
        }

        .strat-insight {
            background: rgba(255, 255, 255, 0.03);
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            border-left: 2px solid rgba(255, 255, 255, 0.1);
            font-size: 0.9rem;
            color: var(--text-dim);
        }

        .strat-insight strong {
            color: #fff;
            display: block;
            margin-bottom: 5px;
        }

        .action-list {
            list-style: none;
            padding: 0;
        }

        .action-item {
            display: flex;
            gap: 15px;
            margin-bottom: 1rem;
            align-items: flex-start;
        }

        .check-circle {
            min-width: 24px;
            height: 24px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--success);
            font-size: 0.8rem;
        }

        .kpi-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px dashed var(--border);
        }

        .kpi-val {
            font-size: 1.5rem;
            font-weight: 700;
            font-family: 'Rajdhani', sans-serif;
        }

        /* --- FOOTER --- */
        footer {
            border-top: 1px solid var(--border);
            padding: 3rem;
            text-align: center;
            color: var(--text-dim);
            margin-top: 3rem;
            background: #020617;
        }

        /* RESPONSIVE */
        @media (max-width: 1024px) {
            .funnel-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .funnel-arrow {
                transform: rotate(90deg);
                margin: 0 auto;
                width: 30px;
            }

            .ai-grid,
            .strat-grid,
            .charts-wrapper,
            .charts-secondary {
                grid-template-columns: 1fr;
            }

            .ai-grid {
                min-height: auto;
            }
        }
    </style>
</head>

<body>

    <header>
        <div class="header-inner">
            <div class="brand-logo"><i class="fa-solid fa-layer-group"></i> NEXUS AI</div>
            <div class="status-pill">
                <div class="status-dot"></div>
                SYSTEM ONLINE | V10 Master
            </div>
        </div>
    </header>

    <div class="main-container">

        <!-- SECTION 1: DATA PIPELINE -->
        <section class="fade-in">
            <div class="section-header">
                <i class="fa-solid fa-network-wired section-icon"></i>
                <h2 class="section-title font-tech">VERİ MADENCİLİĞİ OPERASYONU</h2>
            </div>

            <div class="funnel-grid">
                <!-- Step 1 -->
                <div class="glass-panel funnel-card" style="color: #fff;">
                    <div class="count-val" id="count1">0</div>
                    <div class="count-label">TOPLANAN HAM VERİ</div>
                    <div class="stat-detail">
                        <div class="stat-row">YouTube: <b>100K</b></div>
                        <div class="stat-row">Twitter (X): <b>30K</b></div>
                        <div class="stat-row">Haberler: <b>300+</b></div>
                    </div>
                </div>

                <div class="funnel-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                <!-- Step 2 -->
                <div class="glass-panel funnel-card" style="color: var(--danger);">
                    <div class="count-val" id="count2">0</div>
                    <div class="count-label">FİLTRELENEN ÇÖP</div>
                    <div class="stat-detail" style="border-left: 2px solid var(--danger);">
                        <div class="stat-row">Mükerrer: <b>~15K</b></div>
                        <div class="stat-row">Bot/Spam: <b>~8.5K</b></div>
                        <div class="stat-row">Çöp Veri: <b>~5K</b></div>
                    </div>
                </div>

                <div class="funnel-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                <!-- Step 3 -->
                <div class="glass-panel funnel-card" style="color: var(--success); border-color: rgba(16,185,129,0.3);">
                    <div class="count-val" id="count3">0</div>
                    <div class="count-label">ANALİZE GİREN VERİ</div>
                    <div class="stat-detail" style="border-left: 2px solid var(--success);">
                        <div style="color: var(--text-dim); font-size: 0.9rem;">NLP ve Yapay Zeka motoruna beslenen %100
                            temiz veri seti.</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 2: TECH STACK -->
        <section class="fade-in delay-100">
            <div class="section-header">
                <i class="fa-solid fa-microchip section-icon"></i>
                <h2 class="section-title font-tech">İSTİHBARAT TEKNOLOJİLERİ (TECH STACK)</h2>
            </div>
            <div class="tech-grid">
                <div class="glass-panel tech-item" style="padding: 1.5rem;">
                    <h4><i class="fa-solid fa-mask" style="color:var(--primary);"></i> Stealth Scraper</h4>
                    <p>Twitter API limitlerini aşmak için özel kütüphane (Twikit Modifikasyonu). Human-like Requests ve
                        Cookie Rotasyonu ile IP engeli aşıldı.</p>
                </div>
                <div class="glass-panel tech-item" style="padding: 1.5rem;">
                    <h4><i class="fa-solid fa-brain" style="color:var(--purple);"></i> Hibrit NLP Motoru</h4>
                    <p>Lexicon-Based jargon sözlüğü ve LDA Topic Modeling (100k veri -> 6 konu). Bağlam farkındalığı ile
                        'Düşüş' kelimesini fırsat/risk olarak ayırır.</p>
                </div>
                <div class="glass-panel tech-item" style="padding: 1.5rem;">
                    <h4><i class="fa-solid fa-shield-halved" style="color:var(--danger);"></i> Veri Sanitizasyonu</h4>
                    <p>Asya kökenli bot ağları Regex ile temizlendi. Zaman eşitleme (UTC/Local) ve HTML/Emoji/Link
                        format temizliği.</p>
                </div>
            </div>
        </section>

        <!-- SECTION 3: AI TERMINAL -->
        <section class="fade-in delay-200">
            <div class="section-header">
                <i class="fa-solid fa-robot section-icon"></i>
                <h2 class="section-title font-tech">NEXUS AI: 30 GÜNLÜK ÖNGÖRÜ</h2>
            </div>
            <div class="glass-panel" style="padding: 0; overflow: hidden;">
                <div class="ai-grid">
                    <!-- TERMINAL -->
                    <div class="terminal-window">
                        <div class="terminal-header">
                            <div class="dot dot-r"></div>
                            <div class="dot dot-y"></div>
                            <div class="dot dot-g"></div>
                        </div>
                        <div class="terminal-content" id="terminalText"></div>
                        <span class="cursor"></span>
                    </div>

                    <!-- CHART -->
                    <div class="ai-visual">
                        <div class="ai-verdict"><i class="fa-solid fa-brain"></i> LIVE AI MODEL</div>
                        <p style="color:#e2e8f0; line-height:1.6; font-size:1.05rem; margin-top:0;">
                            NEXUS AI motorumuz, son 30 günün verilerini tarayarak geçmişteki <strong>"2017 Mega Boğa
                                Rallisi"</strong> döngüsüyle %88 benzerlik tespit etti.
                            Piyasa "Sessiz Akümülasyon" evresinden "Parabolik Yükseliş" evresine geçiyor.
                        </p>
                        <div style="flex:1; min-height: 250px;">
                            <canvas id="aiPredictionChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 4: MARKET CHARTS (FULL RESTORE) -->
        <section class="fade-in delay-300">
            <div class="section-header">
                <i class="fa-solid fa-chart-pie section-icon"></i>
                <h2 class="section-title font-tech">PAZAR VERİ ANALİZİ</h2>
            </div>
            <div class="charts-wrapper">
                <div class="glass-panel chart-box"><canvas id="lineChart"></canvas></div>
                <div class="glass-panel chart-box"><canvas id="doughnutChart"></canvas></div>
            </div>
            <div class="charts-secondary">
                <div class="glass-panel chart-box"><canvas id="barWordChart"></canvas></div>
                <div class="glass-panel chart-box"><canvas id="barTopicChart"></canvas></div>
            </div>
        </section>

        <!-- SECTION 5: STRATEGY MAP (FULL RESTORE) -->
        <section class="fade-in delay-300">
            <div class="section-header">
                <i class="fa-regular fa-chess-knight section-icon"></i>
                <h2 class="section-title font-tech">KURUMSAL STRATEJİK YOL HARİTASI</h2>
            </div>
            <p class="strategy-intro">
                101.681 veri noktasından elde edilen içgörüler doğrultusunda; müşteri sadakati, pazar payı artışı ve
                marka otoritesi oluşturmak için tasarlanmış özel aksiyon planı.
            </p>

            <div class="strat-grid">

                <!-- 1. RISK -->
                <div class="glass-panel strat-card risk">
                    <div class="strat-head">
                        <span class="strat-title">🔴 Kriz Yönetimi & PR</span>
                        <span class="status-pill"
                            style="border-color:var(--danger); background:rgba(239, 68, 68, 0.1); color:var(--danger);">KRİTİK</span>
                    </div>
                    <div class="strat-insight">
                        <strong>Veri Tespiti:</strong> Mağduriyetlerin %60'ı "Teknik Hata", "SMS Gelmiyor" ve "Delist
                        Korkusu" kaynaklı.
                    </div>
                    <ul class="action-list">
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">"Şeffaflık Raporu" Yayınlanması</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Delist edilecek coinlerin 1 hafta
                                    önceden bildirilmesi ve gerekçeli karar metni.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Alternatif Doğrulama (2FA)</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">SMS sorunlarına karşı Google
                                    Authenticator ve Biometrik giriş zorunluluğu.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Sigorta Fonu İletişimi</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Kullanıcı varlıklarının %100'ünün
                                    soğuk cüzdanda olduğu kanıtlanmalı.</div>
                            </div>
                        </li>
                    </ul>
                    <div class="kpi-row">
                        <span class="font-tech" style="color:var(--text-dim);">KPI HEDEF</span>
                        <span class="kpi-val" style="color:var(--danger);">-%40 Şikayet</span>
                    </div>
                </div>

                <!-- 2. GROWTH -->
                <div class="glass-panel strat-card growth">
                    <div class="strat-head">
                        <span class="strat-title">🟢 Büyüme (Growth)</span>
                        <span class="status-pill">YÜKSEK ÖNCELİK</span>
                    </div>
                    <div class="strat-insight">
                        <strong>Veri Tespiti:</strong> Pazarın %55'i "Gem", "Sepet" ve "Yapay Zeka" aramalarıyla yüksek
                        iştah gösteriyor.
                    </div>
                    <ul class="action-list">
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">"Gem Avcısı" AI Bot</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Hype artışı olan coinleri
                                    otomatik listeleyen araç lansmanı.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Referans Yarışması</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">"Boğa Sezonu Takımını Kur"
                                    konseptli hacim yarışması.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Mikro-Influencer Ordusu</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Etkileşimi yüksek 50+ alt hesapla
                                    partnerlik.</div>
                            </div>
                        </li>
                    </ul>
                    <div class="kpi-row">
                        <span class="font-tech" style="color:var(--text-dim);">KPI HEDEF</span>
                        <span class="kpi-val" style="color:var(--success);">+%25 Yeni Üye</span>
                    </div>
                </div>

                <!-- 3. PRODUCT -->
                <div class="glass-panel strat-card prod">
                    <div class="strat-head">
                        <span class="strat-title">🔵 Ürün Geliştirme</span>
                        <span class="status-pill"
                            style="border-color:var(--primary); color:var(--primary); background:rgba(59, 130, 246, 0.1);">ORTA
                            VADE</span>
                    </div>
                    <div class="strat-insight">
                        <strong>Veri Tespiti:</strong> Kullanıcılar teknik analizden ziyade "Psikolojik Destek" ve
                        "Hazır Sinyal" arıyor.
                    </div>
                    <ul class="action-list">
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Canlı Duygu İbresi</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Her coin detay sayfasına Fear &
                                    Greed endeksi eklenmesi.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Copy-Trade 2.0</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">İnsanları değil, "Veri
                                    Madenciliği Botu"nun portföyünü kopyalama.</div>
                            </div>
                        </li>
                    </ul>
                    <div class="kpi-row">
                        <span class="font-tech" style="color:var(--text-dim);">KPI HEDEF</span>
                        <span class="kpi-val" style="color:var(--primary);">%15 Hacim Artışı</span>
                    </div>
                </div>

                <!-- 4. CONTENT -->
                <div class="glass-panel strat-card cont">
                    <div class="strat-head">
                        <span class="strat-title">🟣 İçerik & Topluluk</span>
                        <span class="status-pill"
                            style="border-color:var(--accent); color:var(--accent); background:rgba(99, 102, 241, 0.1);">SÜREKLİ</span>
                    </div>
                    <div class="strat-insight">
                        <strong>Veri Tespiti:</strong> "Hocam ne alalım?" sorusu zirvede. Otorite boşluğu var,
                        fenomenlere güven azalıyor.
                    </div>
                    <ul class="action-list">
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">"Veri Ne Diyor?" Serisi</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Subjektif yorum yerine, on-chain
                                    verileriyle haftalık analiz.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Twitter Spaces (AMA)</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">"Mağduriyet" yaşayan
                                    kullanıcılarla doğrudan iletişim.</div>
                            </div>
                        </li>
                    </ul>
                    <div class="kpi-row">
                        <span class="font-tech" style="color:var(--text-dim);">KPI HEDEF</span>
                        <span class="kpi-val" style="color:var(--accent);">Top 3 Otorite</span>
                    </div>
                </div>

                <!-- 5. CRM -->
                <div class="glass-panel strat-card crm">
                    <div class="strat-head">
                        <span class="strat-title">🟡 CRM & Sadakat</span>
                        <span class="status-pill"
                            style="border-color:var(--gold); color:var(--gold); background:rgba(245, 158, 11, 0.1);">UZUN
                            VADE</span>
                    </div>
                    <div class="strat-insight">
                        <strong>Veri Tespiti:</strong> Kullanıcılar zarar edince küsüp gidiyor (Churn). Geri kazanmak
                        yeni kullanıcıdan ucuz.
                    </div>
                    <ul class="action-list">
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">"Recovery" Kampanyası</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Zarar edenlere %0 komisyon veya
                                    işlem iade teklifi.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">VIP Destek Hattı</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">5000$ üzeri portföye WhatsApp
                                    özel temsilcisi.</div>
                            </div>
                        </li>
                    </ul>
                    <div class="kpi-row">
                        <span class="font-tech" style="color:var(--text-dim);">KPI HEDEF</span>
                        <span class="kpi-val" style="color:var(--gold);">%20 Geri Kazanım</span>
                    </div>
                </div>

                <!-- 6. TECH -->
                <div class="glass-panel strat-card tech">
                    <div class="strat-head">
                        <span class="strat-title">⚪ Teknoloji & Altyapı</span>
                        <span class="status-pill"
                            style="border-color:var(--cyan); color:var(--cyan); background:rgba(6, 182, 212, 0.1);">ACİL</span>
                    </div>
                    <div class="strat-insight">
                        <strong>Veri Tespiti:</strong> Yoğun zamanlarda (Pump/Dump) uygulama çökmesi en büyük nefret
                        sebebi.
                    </div>
                    <ul class="action-list">
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Yük Testi ve Ölçekleme</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">Anlık %500 trafik artışına (Boğa
                                    senaryosu) hazırlık.</div>
                            </div>
                        </li>
                        <li class="action-item">
                            <div class="check-circle"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong style="color:#fff;">Mobil Uygulama UX/UI</strong>
                                <div style="font-size:0.85rem; color:var(--text-dim);">"Karmaşık arayüz" şikayetleri
                                    için 'Lite Mod'.</div>
                            </div>
                        </li>
                    </ul>
                    <div class="kpi-row">
                        <span class="font-tech" style="color:var(--text-dim);">KPI HEDEF</span>
                        <span class="kpi-val" style="color:var(--cyan);">%99.99 Uptime</span>
                    </div>
                </div>

            </div>
        </section>

    </div>

    <footer>
        <div class="font-tech" style="font-size: 1.2rem; color: #fff; margin-bottom: 1rem;">NEXUS INTELLIGENCE LABS
        </div>
        <p>Gizli Ticari İstihbarat Raporu | © 2026</p>
    </footer>

    <script>
        // --- 1. COUNT UP ANIMATION ---
        function animateValue(obj, start, end, duration) {
            let startTimestamp = null;
            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                obj.innerHTML = Math.floor(progress * (end - start) + start).toLocaleString();
                if (progress < 1) { window.requestAnimationFrame(step); }
            };
            window.requestAnimationFrame(step);
        }

        document.addEventListener("DOMContentLoaded", () => {
            animateValue(document.getElementById("count1"), 0, 130300, 2000);
            animateValue(document.getElementById("count2"), 0, 28619, 2000);
            animateValue(document.getElementById("count3"), 0, 101681, 2000);
        });

        // --- 2. TERMINAL TYPING ---
        const terminalText = `> INITIALIZING SYSTEM v10.0... [OK]
> CONNECTING TO DATA LAKE... [CONNECTED]
> LOADING SENTIMENT MODELS... [DONE]
> ANALYZING LAST 30 DAYS DATA STREAM...
> > TWITTER VOLUME: HIGH
> > NEWS SENTIMENT: NEUTRAL/POSITIVE
> MATCHING HISTORICAL PATTERNS... 
> DETECTED PATTERN: "MEGA_BULL_RUN_2017"
> SIMILARITY SCORE: 88%
> CALCULATING PROBABILITY... [HIGH]
> PREDICTION: UPTREND CONTINUATION
> SUGGESTION: HOLD POSITIONS (HODL)`;

        const terminalEl = document.getElementById('terminalText');
        let i = 0;
        function typeWriter() {
            if (i < terminalText.length) {
                let char = terminalText.charAt(i);
                if (char === '\n') char = '<br/>>';
                terminalEl.innerHTML += char;
                i++;
                setTimeout(typeWriter, 20);
            }
        }
        setTimeout(typeWriter, 1000);

        // --- 3. CHARTS SETUP ---
        Chart.defaults.font.family = "'Inter', sans-serif";
        Chart.defaults.color = '#94a3b8';
        Chart.defaults.borderColor = 'rgba(255,255,255,0.05)';

        const colorOpp = '#10b981'; const colorRisk = '#ef4444'; const colorVictim = '#06b6d4'; const colorAI = '#d946ef';

        // Chart 1: AI Prediction
        new Chart(document.getElementById('aiPredictionChart'), {
            type: 'line',
            data: {
                labels: ['-30 Gün', '-25', '-20', '-15', '-10', '-5', 'BUGÜN', '+5 (Tahmin)', '+10 (Tahmin)', '+15 (Tahmin)'],
                datasets: [
                    { label: 'Gerçekleşen', data: [42000, 43500, 43000, 44000, 43800, 45000, 46500, null, null, null], borderColor: colorOpp, borderWidth: 3, tension: 0.4, pointRadius: 4 },
                    { label: 'AI Tahmini', data: [null, null, null, null, null, null, 46500, 48000, 49500, 52000], borderColor: colorAI, borderWidth: 3, borderDash: [10, 5], tension: 0.4, pointRadius: 0 }
                ]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { labels: { color: '#fff' } } }, scales: { y: { display: false }, x: { grid: { display: false } } } }
        });

        // Chart 2: Line (Crisis vs Hype)
        new Chart(document.getElementById('lineChart'), {
            type: 'line',
            data: { labels: ['2020 Q4', '2021 Q1', '2021 Q2', '2022 Q1', '2022 Q4', '2023 Q2', '2024 Q1', '2025 Q1', '2026 Q1'], datasets: [{ label: 'Fırsat İştahı', data: [150, 500, 350, 100, 50, 250, 600, 650, 800], borderColor: colorOpp, backgroundColor: 'rgba(16,185,129,0.1)', fill: true, tension: 0.4 }, { label: 'Kriz Endeksi', data: [80, 120, 450, 400, 600, 200, 150, 100, 130], borderColor: colorRisk, backgroundColor: 'rgba(239,68,68,0.1)', fill: true, tension: 0.4 }] },
            options: { responsive: true, maintainAspectRatio: false, plugins: { title: { display: true, text: 'ZAMAN İÇİNDE KRİZ VE FIRSAT DALGALARI' } }, scales: { x: { grid: { display: false } } } }
        });

        // Chart 3: Doughnut
        new Chart(document.getElementById('doughnutChart'), {
            type: 'doughnut',
            data: { labels: ['Fırsat / Hype', 'Risk / Korku', 'Mağduriyet'], datasets: [{ data: [55, 30, 15], backgroundColor: [colorOpp, colorRisk, colorVictim], borderWidth: 0 }] },
            options: { responsive: true, maintainAspectRatio: false, plugins: { title: { display: true, text: 'GENEL DUYGU DAĞILIMI' }, legend: { position: 'bottom' } }, cutout: '70%' }
        });

        // Chart 4: Word Bar
        new Chart(document.getElementById('barWordChart'), {
            type: 'bar', indexAxis: 'y',
            data: { labels: ['GEM / Sepet', 'Boğa', 'Yapay Zeka', 'Scam', 'Delist', 'Binance TR', 'SMS'], datasets: [{ label: 'Frekans', data: [8500, 7200, 6800, 4500, 3200, 2800, 1500], backgroundColor: [colorOpp, colorOpp, colorOpp, colorRisk, colorRisk, colorVictim, colorVictim], borderRadius: 4 }] },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false }, title: { display: true, text: 'TESPİT EDİLEN KRİTİK KELİMELER' } }, scales: { x: { display: false }, y: { grid: { display: false } } } }
        });

        // Chart 5: Topic Bar
        new Chart(document.getElementById('barTopicChart'), {
            type: 'bar',
            data: { labels: ['Altcoinler', 'Borsalar', 'Bitcoin'], datasets: [{ label: 'Fırsat', data: [80, 20, 60], backgroundColor: colorOpp }, { label: 'Risk', data: [20, 80, 40], backgroundColor: colorRisk }] },
            options: { responsive: true, maintainAspectRatio: false, plugins: { title: { display: true, text: 'KONU BAZLI DUYGU ANALİZİ' } }, scales: { x: { stacked: false, grid: { display: false } }, y: { beginAtZero: true, display: false } } }
        });
    </script>
</body>

</html>
NEXUS[kopya.html](https://github.com/user-attachments/files/24738084/kopya.html)
 INTELLIGENCE | V10 MASTER - README
📋 Genel Bakış
Bu proje, NEXUS INTELLIGENCE V10 Master sistemini görselleştiren bir dashboard arayüzüdür. Sistem, veri madenciliği operasyonlarından elde edilen 101.681 veri noktasını analiz ederek stratejik kararlar için içgörüler sunar.

🎯 Özellikler
1. Veri Madenciliği Operasyonu
Toplanan Ham Veri: 130.300 veri noktası

YouTube: 100K

Twitter (X): 30K

Haberler: 300+

Filtrelenen Çöp Veri: 28.619

Mükerrer: ~15K

Bot/Spam: ~8.5K

Çöp Veri: ~5K

Analize Giren Temiz Veri: 101.681

2. İstihbarat Teknolojileri (Tech Stack)
Stealth Scraper: Twitter API limitlerini aşan özel kütüphane

Hibrit NLP Motoru: Lexicon-Based sözlük ve LDA Topic Modeling

Veri Sanitizasyonu: Bot temizleme ve format standardizasyonu

3. NEXUS AI: 30 Günlük Öngörü
Geçmiş verilerle %88 benzerlik tespiti

"2017 Mega Boğa Rallisi" döngüsü benzerliği

Sessiz Akümülasyon → Parabolik Yükseliş evresi tahmini

4. Pazar Veri Analizi - Grafikler
Zaman İçinde Kriz ve Fırsat Dalgaları (Çizgi Grafiği)

Genel Duygu Dağılımı (Halka Grafiği)

Fırsat / Hype: %55

Risk / Korku: %30

Mağduriyet: %15

Tespit Edilen Kritik Kelimeler (Yatay Çubuk Grafiği)

"GEM / Sepet", "Boğa", "Yapay Zeka" öne çıkan pozitif kelimeler

"Scam", "Delist", "SMS" öne çıkan negatif kelimeler

Konu Bazlı Duygu Analizi (Dikey Çubuk Grafiği)

5. Kurumsal Stratejik Yol Haritası
6 ana stratejik alan:

🔴 Kriz Yönetimi & PR (KRİTİK)
KPI Hedef: %40 Şikayet Azalması

Aksiyonlar:

"Şeffaflık Raporu" yayınlanması

Alternatif Doğrulama (2FA) sistemleri

Sigorta Fonu iletişimi

🟢 Büyüme (Growth) (YÜKSEK ÖNCELİK)
KPI Hedef: %25 Yeni Üye Artışı

Aksiyonlar:

"Gem Avcısı" AI Bot lansmanı

Referans Yarışması düzenlenmesi

Mikro-Influencer ordusu oluşturma

🔵 Ürün Geliştirme (ORTA VADE)
KPI Hedef: %15 Hacim Artışı

Aksiyonlar:

Canlı Duygu İbresi entegrasyonu

Copy-Trade 2.0 (Veri Madenciliği Botu)

🟣 İçerik & Topluluk (SÜREKLİ)
KPI Hedef: Top 3 Otorite

Aksiyonlar:

"Veri Ne Diyor?" serisi başlatma

Twitter Spaces (AMA) oturumları

🟡 CRM & Sadakat (UZUN VADE)
KPI Hedef: %20 Geri Kazanım

Aksiyonlar:

"Recovery" Kampanyası

VIP Destek Hattı oluşturma

⚪ Teknoloji & Altyapı (ACİL)
KPI Hedef: %99.99 Uptime

Aksiyonlar:

Yük Testi ve Ölçekleme iyileştirmeleri

Mobil Uygulama UX/UI optimizasyonu

🛠️ Teknik Detaylar
Kullanılan Teknolojiler
HTML5, CSS3, JavaScript

Chart.js - Veri görselleştirme

Font Awesome - İkonlar

Google Fonts - Typography

Tasarım Özellikleri
Modern glassmorphism tasarımı

Responsive layout (mobil uyumlu)

Animasyonlu sayı artışları

Tipografi odaklı terminal simülasyonu

Renk kodlu strateji kartları

Renk Paleti
Ana Arkaplan: #050511

Primary: #3b82f6 (Mavi)

Success: #10b981 (Yeşil)

Danger: #ef4444 (Kırmızı)

Accent: #6366f1 (Mor)

Cyan: #06b6d4 (Turkuaz)

Gold: #f59e0b (Altın)

Purple: #d946ef (Pembe)

🚀 Kurulum ve Kullanım
Dosyayı kopya.html olarak kaydedin

Modern bir tarayıcıda açın (Chrome, Firefox, Edge)

Tüm animasyonlar ve grafikler otomatik yüklenecektir

📊 Veri Kaynakları
YouTube: 100.000+ video içeriği analizi

Twitter (X): 30.000+ tweet ve trend analizi

Haber Kaynakları: 300+ haber makalesi sentimant analizi

⚠️ Notlar
Bu dashboard demo amaçlı statik bir görselleştirmedir

Gerçek zamanlı veri bağlantısı bulunmamaktadır

Tüm grafikler örnek verilerle oluşturulmuştur

Sistem "ONLINE" durumu simülasyon amaçlıdır

📄 Lisans
Bu proje gizli ticari istihbarat raporu olarak hazırlanmıştır. © 2026 NEXUS INTELLIGENCE LABS.
