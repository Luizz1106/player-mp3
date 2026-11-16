# Meu Player MP3

Player de MP3 que roda no celular, instalável pelo link (PWA).

- Adicione os MP3 que já estão no celular (arquivos ou pasta inteira)
- As músicas ficam guardadas no navegador do celular (IndexedDB) — nada é enviado para servidor
- Toca em segundo plano e com a tela bloqueada (Media Session API)
- No APK, o botão **🔍 Buscar músicas do celular** varre o aparelho sozinho (MediaStore, igual ao Lark Player) — pede a permissão de áudio uma vez e lista todas as músicas, com artista, álbum e duração. v3: mostra o status da busca na tela (permissão negada / quantas achou), tenta de novo ao abrir e tem busca reserva caso a primeira não retorne nada
- **YouTube (v4):** cole o link da música no campo "YouTube" e toque em ▶ Tocar — ela fica salva na aba YouTube e toca no player embutido, com título/capa vindos do oEmbed. Atenção: o YouTube pode pausar ao desligar a tela (limite do player dele); precisa de internet e não baixa o MP3
- **YouTube v5 — áudio direto com tela desligada:** ao tocar um link, o app tenta extrair o áudio direto (InnerTube → Piped → Invidious → Cobalt, com cache de 30 min) e toca no player normal, igual MP3 — aí a tela desligada não pausa. Se nenhum extrator responder, volta para o player embutido do YouTube e avisa na tela. Os servidores de extração bloquearam a conexão daqui, então não deu para testar ao vivo — o teste real é no celular dele
- **YouTube v6 — correção de "não toca":** se o áudio direto de uma fonte falhar, o app tenta outra fonte sozinho e, se nenhuma funcionar, cai para o player do YouTube; o player do YouTube agora desmuta e dá play ao abrir, e avisa se não começar sozinho ("toque no vídeo para tocar"). O app mostra a versão no rodapé (v1.0.9) para identificar a versão instalada
- **Modo tela apagada (v7):** botão 🌙 Tela apagada no player em tela cheia — a tela fica toda preta e segura ligada por dentro (Wake Lock, sem plugin), então o YouTube não pausa e o celular parece desligado; toque na tela para voltar. Gasta mais bateria que a tela desligada de verdade, porque a tela continua ligada (só preta). Versão no rodapé: v1.0.10
- **Baixar do YouTube estilo Snaptube (v7):** compartilhe o vídeo do YouTube direto para o app (o app aparece na lista de compartilhar) ou cole o link e toque em ⬇ Baixar — escolha **MP3** (só o áudio, fica guardado na biblioteca e toca offline) ou **MP4** (o vídeo, até 720p, salvo na pasta Documentos do celular; toque nele para abrir no player de vídeo). Usa os mesmos extratores do player (YouTube/Piped/Invidious/Cobalt) — se nenhum responder, o download falha e o app avisa. Plugins novos: `@capgo/capacitor-share-target` (receber o link compartilhado), `@capacitor/filesystem` (baixar o arquivo) e `@capacitor/share` (abrir o MP4). O workflow roda `scripts/patch-manifest.py` depois do `cap add android` para ativar o recebimento de links (o projeto Android é recriado a cada build)
- Playlists, favoritos, aleatório, repetir, busca
- Preto e dourado, igual ao Future Painel

## Instalar

1. Abra o link do GitHub Pages no Chrome do celular
2. Toque em **Instalar app** no topo, ou menu ⋮ → **Instalar app / Adicionar à tela inicial**
3. Toque em **＋ Adicionar músicas** e escolha os MP3

Publicado via GitHub Pages a partir da branch `main`.
