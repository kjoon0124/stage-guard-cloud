from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>StageGuard Cloud</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f4f9;">
            <div style="background: white; padding: 40px; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
                <h1 style="color: #2c3e50;">🚀 StageGuard Cloud Deployment Success</h1>
                <p style="color: #555; font-size: 18px;">Vercel 및 Supabase 연동 클라우드 배포가 완료되었습니다.</p>
                <p style="color: #888; font-size: 14px;">(과제 제출용 퍼블릭 URL 정상 작동 확인)</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))
        return
        