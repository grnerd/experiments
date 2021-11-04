import pyqrcode as q

lnk = ("https://cf9ada1bada3.ngrok.io")
g = q.create(lnk)
g.svg('hack.svg',scale=7)


