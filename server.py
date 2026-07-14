#!/usr/bin/env python3
import http.server
import re
import socketserver
import urllib.request

FEED_URL = "https://d3bd0tgyk368z1.cloudfront.net/feeds/epg/tcies_tennisono/TCSPAIN.xml"
PORT = 8111
DOCTYPE_RE = re.compile(rb"<!DOCTYPE[^>]*>", re.IGNORECASE)


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path.endswith("/feed.xml") or path == "/feed.xml":
            try:
                with urllib.request.urlopen(FEED_URL, timeout=30) as resp:
                    data = resp.read()
            except Exception as exc:
                self.send_response(502)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(f"Failed to fetch EPG feed: {exc}".encode("utf-8"))
                return

            # Browsers' DOMParser fails on external SYSTEM DTDs like xmltv.dtd
            data = DOCTYPE_RE.sub(b"", data)

            self.send_response(200)
            self.send_header("Content-Type", "text/xml; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(data)
            return

        return super().do_GET()


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        httpd.serve_forever()
