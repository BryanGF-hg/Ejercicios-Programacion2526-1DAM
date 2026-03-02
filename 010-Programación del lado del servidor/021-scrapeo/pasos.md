Conseguimos una lista de web (posible hacerlo en CSV)
Luego usamos Python con la libreria LXML para conseguir cualquier etiqueta que queramos (<title>)
Usamos la IA para que haga una descripcion
**prompt:**
with local ollama deepseek-r1.1:1.5b get a description, in spanish, one paragraph, of the web contents (what is that web about)

Ahora escogemos como guardar la informacion
i would like to save data (url,title,summary and find emails on web code) to newly created sqlite database
