from flask import Flask, render_template

app = Flask(__name__)

# POSTS MOCK
posts = [
{
"titulo": "Post 1",
"texto": "Meu primeiro post"
},
{
"titulo": "Post 2",
"texto": "olha eu aqui de novo"
}
]

@app.route('/')
def exibir_entradas():
    
    return render_template("layout.html", entradas=posts)


    