# Cyberportal Subscriptions Mirror

Это автоматическое зеркало конфигураций (подписок) для обхода блокировок.  
Репозиторий обновляется автоматически **каждый час** при помощи GitHub Actions.

## Прямые ссылки на подписки (Raw URLs):

Эти ссылки можно вставлять в клиенты V2rayNG, NekoBox, ПроБел (v2Whitelist) и др.:

- **Black MIX RU:**  
  `https://raw.githubusercontent.com/NullCoreDeveloper/cyberportal-mirror/master/cp-001.txt`
- **VLESS Black All RU:**  
  `https://raw.githubusercontent.com/NullCoreDeveloper/cyberportal-mirror/master/cp-002.txt`
- **VLESS White List:**  
  `https://raw.githubusercontent.com/NullCoreDeveloper/cyberportal-mirror/master/cp-035.txt`
- **CIDR White All RU:**  
  `https://raw.githubusercontent.com/NullCoreDeveloper/cyberportal-mirror/master/cp-006.txt`
- **SNI White All RU:**  
  `https://raw.githubusercontent.com/NullCoreDeveloper/cyberportal-mirror/master/cp-008.txt`
- **White Keys:**  
  `https://raw.githubusercontent.com/NullCoreDeveloper/cyberportal-mirror/master/cp-042.txt`

## Как это работает?

Внутри репозитория настроен воркер `sync.py`, который регулярно проверяет оригинальный сервер киберпортала на наличие обновлений. 
Встроена защита от сбоев: если оригинальный сервер упал и отдает ошибку (или Cloudflare заглушку), скрипт игнорирует её и сохраняет последние 100% рабочие файлы. Благодаря этому зеркало продолжает отдавать рабочие настройки без перебоев.
