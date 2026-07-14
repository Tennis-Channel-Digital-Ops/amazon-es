# Amazon ES / TC Spain Live Monitor

TC Spain live schedule browser for Amazon Spain metadata.

## What it does

Single-page web UI (`index.html`) that shows the TC Spain live feed schedule in three tabs:

- **Now Playing** — what's live right now
- **Upcoming** — scheduled future events
- **Finished** — historical airings with a date picker

It fetches data from the CloudFront XMLTV feed and supports timezone selection.

## Data source

`https://d3bd0tgyk368z1.cloudfront.net/feeds/epg/tcies_tennisono/TCSPAIN.xml`

## Runtime

```bash
cd /opt/epg/amazon-es
/usr/bin/python3 -m http.server 8111 --bind 0.0.0.0
```

Systemd unit: `amazon-es.service`

- Static HTML + Tailwind CSS + vanilla JavaScript
- No build step; serve the folder with any HTTP server

## DOPS publication

| Item | Value |
|------|-------|
| Slug | `/amazon-es/` |
| Port | `8111` |
| DOPS URL | `https://dops.tct2pbtv.com/amazon-es/` |

Publish via DOPS Publisher Admin (`/publisher-admin`) and assign users in Auth Admin (`/auth-admin`).

## Files

- `index.html` — the entire app
