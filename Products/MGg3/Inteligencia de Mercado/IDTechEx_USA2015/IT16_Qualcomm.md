---
tipo: registro-documento
produto: MGg3
fonte_arquivo: "IDTechEx_USA2015PresentationQualcomm.pdf"
organizacao: "Qualcomm"
tipo_documento: "Apresentação estratégica — conferência"
data_documento: "2015-11"
confidencialidade: publico
status_extracao: "completo"
confianca_extracao: "alta"
temas:
  - eletrônica de superfície
  - sensores impressos
  - plataforma de sensor híbrido
  - eletrônica flexível descartável
  - Moore's Law
produtos:
  - "Sensor Platform: giroscópio + acelerômetro 3 eixos integrado (band-aid form factor)"
aplicacoes:
  - "Saúde (sensores wearable descartáveis)"
  - "Esportes (golfe — alto impacto)"
  - "Internet das Coisas"
  - "Monitoramento de saúde contínuo"
metricas_chave:
  - "Sensor Platform: lifetime 1 hora a 7 dias"
  - "Form factor: similar a band-aid"
  - "Especificações golf: velocidade de swing 120 mph, 250G aceleração centrípeta, 3.000°/s rotação, 1.500G impacto"
  - "Fab cost surface electronics: muito menor que silicon fabs convencionais"
riscos_uso:
  - "Apresentação não específica de grafeno — foco em eletrônica de superfície em geral"
  - "Qualcomm como usuário/integrador, não produtor de grafeno"
links_relacionados:
  - "[[IDTechEx_USA2015]]"
atualizado: "2026-05-14"
---
# IT16: Qualcomm — Eletrônica de Superfície e Plataformas de Sensor

**Código:** IT16  
**Organização:** Qualcomm  
**Data:** 18 Novembro/2015 (IDTechEx, Santa Clara, CA)  
**Apresentador:** Stein Lundby  
**Classificação:** Público

---

## Resumo Executivo

Qualcomm apresenta visão sobre "surface electronics" — categoria diferente da eletrônica tradicional em silício: fabs simples, substratos flexíveis, tempos de chaveamento longos, mas área grande e custo baixo. A empresa demonstra uma plataforma de sensor integrado (giroscópio + acelerômetro em band-aid descartável) para aplicações esportivas e de saúde. A apresentação não foca especificamente em grafeno, mas contextualiza a eletrônica impressa/flexível como mercado crescente onde materiais como grafeno encontram aplicações.

---

## Produtos e Aplicações

| Categoria | Itens |
|-----------|-------|
| Produto | Sensor Platform: giroscópio 3 eixos + acelerômetro integrados em eletrônica híbrida |
| Form factor | Band-aid (fino, flexível, descartável) |
| Lifetime | 1 hora a 7 dias |
| Aplicação demonstrada | Golfe (análise de swing) |
| Mercado-alvo | Saúde, esportes, IoT |

---

## Comparativo Eletrônica Convencional vs. Superfície

| Parâmetro | Eletrônica Convencional | Surface Electronics |
|-----------|------------------------|---------------------|
| Setup fab cost | Muito alto (bilhões) | Muito baixo |
| Velocidade de chaveamento | Alta | Baixa |
| Substrato | Rígido | Flexível |
| Densidade de transistores | Alta | Baixa |
| Área | Pequena | Grande |
| Custo por área | Alto | Baixo |

---

## Implicações para MGg3

- **Eletrônica de superfície como mercado potencial para grafeno**: Tintas condutoras, eletrodos impressos, sensores — todos usam materiais condutores em substrato flexível; grafeno é candidato natural para algumas dessas aplicações
- **Qualcomm como integrador**: Grandes empresas de tecnologia (Qualcomm, Samsung, etc.) são compradores finais de materiais condutores inovadores — potencial cliente de longo prazo para produtor de grafeno com produto de eletrônica
- **Sensores descartáveis**: Aplicação de grafeno em biosensores e sensores ambientais de baixo custo tem mercado emergente de saúde pessoal (IoT médico)

---

## Links Internos

- **Índice da pasta:** [[IDTechEx_USA2015]]
---

## Fonte original

- **PDF:** [[_attachments/IDTechEx_USA2015PresentationQualcomm.pdf|IDTechEx_USA2015PresentationQualcomm.pdf]]
- **Método de extração:** reprocessamento com `pypdf` em 2026-05-14.
- **Cobertura textual:** 17 de 19 páginas com texto extraído; 6649 caracteres após limpeza.

## Transcrição organizada do PDF

> Texto reextraído da camada textual do PDF e normalizado para consulta em Markdown. Foram removidos cabeçalhos, rodapés, numeração repetitiva e linhas de separação sem conteúdo. Gráficos, imagens e layout visual continuam dependentes do PDF original.

### Slide 1

Creating Value-Added
**Products Using Surface**
Electronics
**Stein Lundby**
November 18, 2015

### Slide 2

A Model for Innovation
**INDUSTRY**
ECOSYSTEM
**Complex**
Systems R&D
**Leadership**
Design for
**Manufacturability**
Supply Chain
**Management**
Customer Support
**Engineering**
USERS

### Slide 3

Transforming our Relationship with Data
**Access Share Store Consume Create**
Device-to-device
connectivity
**Smart edge-caching**
Advanced data
digest & compression
**Behavior- &**
biometric-based security
**Context awareness**
Broadcast / multicast
**Air link / spectrum**
aggregation

### Slide 4

Chasing Moore’s Law
**Source: Wikipedia user Wgsimon Date of Introduction**
Transistor Count
- Transistor density
- Switching speed ( )
- Cost per transistor ( )
- Fixed costs
2,300
10,000
100,000
1,000,000
10,000,000
100,000,000
1,000,000,000
1971 1980 1990 2000 2010
**RCA 1802**
Z80
**MOS 6502**
8086 80186
**Pentium**
AMD K5
**Pentium II**
Pentium III AMD K6
**AMD K7**
Pentium 4
**Barton**
Atom
**Itanium 2 Core 2 Duo**
POWER6
**Six-Core Opteron 2400**
8-Core Xeon Nehalem-EX
**Quad-Core Itanium Tukwila**
16-Core SPARC T3
**Six-Core Core i7**
Dual-Core Itanium 2
**AMD K10**
A self-fulfilling prophecy

### Slide 5

Surface Electronics (Printed, Deposited, Flexible, etc.)
**A different approach to electronics**
Setup fab cost*
**Area**
Surface Electronics
**Long switching times**
Flexible substrates
**Simple fabs**
Large Small
**Low High**
Conventional Electronics
**Short switching times**
High transistor count
**Sophisticated fabs**
Cost vs Area

### Slide 6

Perspective on Surface Electronics
**Opportunity**
− Surface electronics offer a paradigm shift in electronics
− Significant potential in dimensions not addressed by
traditional electronics
**Challenges**
− Little industry structure
− Vast scatter of disparate technologies and technology
providers
− Challenging for potential customers

### Slide 7

Sensor Platform
**Integrated hybrid electronics product**
Electronics and battery form a single monolithic device
**Design objectives**
- Robust 3-axis gyroscope
- Robust 3-axis accelerator
- Disposable (1 hr to 7 days lifetime)
- Band-Aid like form factor and
application

### Slide 8

Sensor Platform
**Golfing application**
120 mph club head velocity
250 G centripetal acceleration
3000⁰/s rotation
1500 G shock load
160 mph ball launch velocity

### Slide 9

Sensor Platform
**Golfing application**
Ax
Ay
Az
Gx
Gy
Gz
**Club speed**
Ball speed
**Tempo**
Face angles
**Club path**

### Slide 10

Golf Sensor Patch
**Measuring acceleration (A) and angular velocity (G) during swing**
Black: Club Face Red: Club Path

### Slide 13

Initial Results: Velocity
**Measurements show excellent precision and accuracy**
Strike Calculated Velocity
[mph]
**Reference Value**
[mph]
**Error**
[%]
1 114.3 115.9 -1.4
2 111.4 112.4 -0.9
3 120.2 119.6 0.5
4 118.5 119.2 -0.6
5 119.0 119.0 0.0
6 125.0 122.2 2.3
7 120.8 120.4 0.4
8 122.1 122.9 -0.7
9 121.7 122.6 -0.7
10 119.2 120.4 -1.0
11 120.6 120.1 0.4
12 119.2 120.0 -0.7
13 121.5 120.1 1.2

### Slide 14

- Circuit pattern printing
- Electrical characteristics
- Materials performance vs. processability vs. price
- Rigid board vs. prototype product vs. actual product
- Mechanical stress
- Design for mass manufacturability
- Cost targets
**Challenges**
Screen print
**Inkjet print**
Mechanical stress
**Electrical and electromagnetic characteristics**

### Slide 15

Source: Machina Research, Feb ‘14

### Slide 16

For more information on Qualcomm, visit us at:
www.qualcomm.com & www.qualcomm.com/blog
Qualcomm, Snapdragon, MSM, Gobi, VIVE, Vuforia and 2Net are trademarks of Qualcomm Incorporated, registered in the United States and other
countries. Born Mobile, Wireless Reach, Toq, IZat, and Zeroth are trademarks of Qualcomm Incorporated. All Qualcomm Incorporated trademarks are
used with permission. Pixtronix is a trademark of Pixtronix, Inc., used with permission. Mirasol is a trademark of Qualcomm MEMS Technologies, Inc.,
registered in the United States and other countries, used with permission. All Joyn is a trademark of Qualcomm Innovation Center, Inc., registered in the
United States and other countries, used with permission. Other products and brand names may be trademarks or registered trademarks of their respective
owners
References in this presentation to “Qualcomm” may mean Qualcomm Incorporated, Qualcomm Technologies, Inc., and/or other subsidiaries or business
units within the Qualcomm corporate structure, as applicable. Qualcomm Incorporated includes Qualcomm’s licensing business, QTL, and the vast majority
of its patent portfolio. Qualcomm Technologies, Inc., a wholly-owned subsidiary of Qualcomm Incorporated, operates, along with its subsidiaries,
substantially all of Qualcomm’s engineering, research and development functions, and substantially all of its product and services businesses, including its
semiconductor business, QCT.
**Thank you**
Follow us on:

### Slide 17

Born Mobile™
29+
years of driving the evolution of wireless
communications
**Making wireless more personal, affordable and**
accessible
World’s largest fabless semiconductor
company
**S&P 100/ S&P 500/ Fortune**
Currently, Qualcomm® semiconductors are products of Qualcomm Technologies, Inc. or its subsidiaries.

### Slide 18

Qualcomm fuels major technology shifts in the industry
**Anticipating the big challenges and investing early on to solve them**
Source: Qualcomm Technologies, Inc. Data. Brew is a product of Qualcomm Technologies, Inc. Currently, Qualcomm® semiconductors are products of Qualcomm Technologies, Inc. or its subsidiaries.
**Digitized mobile**
communications
- 1989: Qualcomm proves CDMA
- 1993: Demonstration of TCP/IP
over CDMA
- 1998: First High Data Rate (HDR) demo
- 1999: CDMA selected as 3G standard
- 2003: First WCDMA multimode
chipset supporting HSDPA
**Redefined computing Transforming the edge**
of the Internet
**From analog to digital**
From desktop to smartphones
- 1998: First commercial CDMA smartphone
- 2001: Introduced Brew™ platform
- 2005: Scorpion CPU development initiated
- 2007: First 1 GHz mobile chip sampled
- 2008: First Android smartphone
- 2009: First 3G/LTE integrated chips
- LTE/Wi-Fi convergence
- Machine learning
- Computer vision
- Security and privacy
- 5G
- LTE-U
- 2013: First LTE Advanced carrier
aggregation smartphone
- 2014: First 64-bit 3G/LTE integrated chip
>$34B Cumulative R&D

### Slide 19

Drivers for Change
Cost is a high value driver for surface electronics (i.e., printed, deposited, flexible, etc.)
Setup fab cost*
**Area**
Surface Electronics
**Long Switching Times**
Flexible Substrates
**Simple Fabs**
Large Small Low High Conventional Electronics
**Short Switching Times**
High transistor count
**Sophisticated Fabs**
Cost vs Area Drivers
**Manufacturing Materials**
Consumer Demand Processes
- Customer does not care
how product is made
- Form Factor
- Scale
- Economic value
- Disposability
- Higher yield
- Higher resolution
- Controlled atmosphere
for materials
- Low cost of fab
- Greater flexibility
- Mobility
- Stability
- Consistency
- Process ability
