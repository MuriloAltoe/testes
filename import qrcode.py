import qrcode

github = qrcode.make('https://github.com/MuriloAltoe')
github.save('github.png')

linkdin = qrcode.make('https://www.linkedin.com/in/murilo-augusto-alto%C3%A9-leme-62565a232/')
linkdin.save('linkedin.png')