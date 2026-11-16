#!/usr/bin/env python3
"""Adiciona o intent-filter de compartilhamento (ACTION_SEND text/*) na
MainActivity do AndroidManifest gerado pelo `npx cap add android`.

O projeto Android é recriado do zero a cada build do GitHub Actions, então
editar o AndroidManifest.xml na mão não dura — este script roda no workflow
logo depois do `cap add android` e antes do `cap sync`/gradle.

Também garante android:launchMode="singleTop" na MainActivity, para que um
link compartilhado com o app já aberto chegue via onNewIntent em vez de
criar outra instância do app.
"""
import re
import sys
from pathlib import Path

MANIFEST = Path("android/app/src/main/AndroidManifest.xml")

INTENT_FILTER = """        <intent-filter>
            <action android:name="android.intent.action.SEND" />
            <category android:name="android.intent.category.DEFAULT" />
            <data android:mimeType="text/*" />
        </intent-filter>
"""

def main():
    if not MANIFEST.exists():
        print(f"ERRO: {MANIFEST} não existe — rode depois do `npx cap add android`")
        return 1
    text = MANIFEST.read_text(encoding="utf-8")

    if "android.intent.action.SEND" in text:
        print("intent-filter de compartilhamento já presente — nada a fazer")
    else:
        # Insere o filtro dentro da <activity ... MainActivity ...> ... </activity>
        m = re.search(
            r'(<activity[^>]*android:name="\.MainActivity"[^>]*>)(.*?)(</activity>)',
            text, re.S)
        if not m:
            print("ERRO: MainActivity não encontrada no AndroidManifest.xml")
            return 1
        text = text[:m.start(2)] + "\n" + INTENT_FILTER + m.group(2) + text[m.end(2):]
        print("intent-filter de compartilhamento adicionado na MainActivity")

    if 'android:name=".MainActivity"' in text:
        # launchMode singleTop na MainActivity
        m = re.search(r'<activity[^>]*android:name="\.MainActivity"[^>]*>', text)
        tag = m.group(0)
        if "launchMode" not in tag:
            new_tag = tag[:-1] + ' android:launchMode="singleTop">'
            text = text[:m.start()] + new_tag + text[m.end():]
            print("launchMode=singleTop aplicado na MainActivity")
        else:
            print("launchMode já definido na MainActivity")

    MANIFEST.write_text(text, encoding="utf-8")
    return 0

if __name__ == "__main__":
    sys.exit(main())
