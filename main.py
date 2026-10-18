from http.server import HTTPServer, BaseHTTPRequestHandler


class ContactsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Читаем файл contacts.html с помощью with open()
        # Убедитесь, что файл лежит в той же папке, откуда запускается скрипт
        try:
            with open('templates/contacts.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            # 2. Отправляем статус 200 (Успех)
            self.send_response(200)

            # 3. Заменяем Content-type на text/html
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # 4. Отправляем тело ответа (переводим строку в байты)
            self.wfile.write(html_content.encode('utf-8'))

        except FileNotFoundError:
            self.send_error(404, "File contacts.html not found")


if __name__ == '__main__':
    # Запускаем сервер на порту 8000
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, ContactsServer)

    print(f'Сервер запущен: http://localhost:{port}')
    print('Любой GET-запрос вернет страницу "Контакты".')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
