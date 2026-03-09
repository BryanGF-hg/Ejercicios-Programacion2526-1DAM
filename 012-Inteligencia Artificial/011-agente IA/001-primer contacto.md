ollama list

josevicente@josevicenteportatil:~$ ollama list
NAME                     ID              SIZE      MODIFIED    
ministral-3:3b           f04aa1c738f6    3.0 GB    12 days ago    
qwen2.5-coder:7b         dae161e27b0e    4.7 GB    4 weeks ago    
deepseek-r1:1.5b         e0979632db5a    1.1 GB    5 weeks ago    
nomic-embed-text:v1.5    0a109f422b47    274 MB    5 weeks ago    
llama3.1:8b              46e0c10c039e    4.9 GB    5 weeks ago    
qwen2.5:3b-instruct      357c53fb659c    1.9 GB    5 weeks ago    
josevicente@josevicenteportatil:~$ ollama run qwen2.5-coder:7b "crea una web en HTML, sin comentarios, solo el código"

josevicente@josevicenteportatil:~$ ollama run qwen2.5-coder:7b "crea un programa que sume 4+3. solo quiero el codigo, ningun comentario"
