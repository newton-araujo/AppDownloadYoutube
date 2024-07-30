
# YouTube Video Downloader

Este projeto é uma aplicação gráfica simples para download de vídeos do YouTube, utilizando as bibliotecas `ttkbootstrap` e `tkinter` para a interface, e uma classe `Download` personalizada para o processo de download.

## Requisitos

- Python 3.x
- ttkbootstrap
- tkinter
- youtube (um módulo personalizado para download de vídeos)

## Instalação

1. Clone este repositório.
2. Instale as dependências necessárias utilizando `pip`:

```bash
pip install ttkbootstrap
```

## Estrutura do Código

### Importações

O código importa os seguintes módulos:

```python
import ttkbootstrap as ttk
from tkinter import filedialog, messagebox
from ttkbootstrap.constants import *
from youtube import Download  # Corrigido o nome do módulo
import threading
import time
```

### Classe `App`

A classe `App` é responsável pela interface gráfica da aplicação. 

#### Inicialização

O método `__init__` define a estrutura e layout da janela principal:

```python
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("DOWNLOAD YOUTUBE")
        
        # Configurações do grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        
        # Título da página
        self.lb_title = ttk.Label(self.frame, text="DOWNLOAD YOUTUBE", font=("MS Serif", 20))
        self.lb_title.grid(column=1, row=0, padx=10, pady=50)
        
        # Seletor de pasta
        self.lb_paste = ttk.Label(self.frame, text="File", font=("MS Serif", 16))
        self.lb_paste.grid(column=0, row=1, padx=10, pady=10)
        self.entre_paste = ttk.Entry(self.frame, width=60)
        self.entre_paste.grid(column=1, row=1, padx=10, pady=10)
        self.btn_paste = ttk.Button(self.frame, text="Open File", padding=5, command=self.browse_folder)
        self.btn_paste.grid(column=2, row=1)
        
        # URL do YouTube
        self.lb_url = ttk.Label(self.frame, text="URL", font=("MS Serif", 16))
        self.lb_url.grid(column=0, row=2, padx=10, pady=10)
        self.entry_url = ttk.Entry(self.frame, width=60)
        self.entry_url.grid(column=1, row=2, padx=10, pady=10)
        
        self.btn_download = ttk.Button(self.frame, text="DOWNLOAD", padding=5, width=60, bootstyle=SUCCESS, command=self.start_download)
        self.btn_download.grid(column=1, row=3, padx=10, pady=10)
        
        # Barra de progresso
        self.progress = ttk.Progressbar(self.frame, orient=HORIZONTAL, mode='determinate', length=280)
        self.progress.grid(column=1, row=4, padx=10, pady=20)
```

#### Método `browse_folder`

Este método abre um diálogo para selecionar uma pasta:

```python
def browse_folder(self):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        self.entre_paste.delete(0, 'end')
        self.entre_paste.insert(0, folder_selected)
```

#### Método `start_download`

Este método inicia a thread para o download:

```python
def start_download(self):
    self.paste = self.entre_paste.get()
    self.url = self.entry_url.get()
    threading.Thread(target=self.download).start()
```

#### Método `download`

Este método executa o download e atualiza a barra de progresso:

```python
def download(self):
    self.progress['value'] = 0
    self.root.update_idletasks()
    downloader = Download(url=self.url, paste=self.paste)
    yt_down = downloader.download_video(url=self.url, paste=self.paste)
    for i in range(10):  
        time.sleep(1)  
        self.progress['value'] += 10
        self.root.update_idletasks()
        print(f"Downloading {self.progress['value']}%")
    self.progress['value'] = 100
    self.root.update_idletasks()
    messagebox.showinfo("Download Complete", "The download has been completed successfully.")
    print("Download complete")
```

### Execução

O código principal para execução da aplicação é:

```python
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = App(root)
    root.mainloop()
```

## Como Usar

1. Execute o script.
2. Selecione a pasta onde deseja salvar o vídeo.
3. Insira a URL do vídeo do YouTube.
4. Clique em "DOWNLOAD" para iniciar o download.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
