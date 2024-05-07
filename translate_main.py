import socket
from googletrans import Translator


def translate_text(text, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text


def main():
    host = '0.0.0.0'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print("Servidor ouvindo na porta", port)

        while True:
            client_socket, address = server_socket.accept()
            with client_socket:
                print('Conexão de', address)
                data = client_socket.recv(1024).decode('utf-8')
                data = data.split('|')
                if len(data) == 2:
                    text, dest_lang = data
                    translated_text = translate_text(text, dest_lang)
                    client_socket.sendall(translated_text.encode('utf-8'))
                else:
                    client_socket.sendall("Requisição inválida!".encode('utf-8'))


if __name__ == "__main__":
    main()
