import os
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get("PORT", 10000))


class MK1Handler(SimpleHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/api/status":
            data = {
                "app": "EJ Business Systems PRO",
                "version": "MK1",
                "server": "online",
                "facebook": "not_connected",
                "instagram": "not_connected",
                "whatsapp": "not_connected",
                "x": "not_connected",
                "live_leads": 0
            }

            response = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        super().do_GET()


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), MK1Handler)
    print(f"MK1 server running on port {PORT}", flush=True)
    server.serve_forever()
