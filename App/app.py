<<<<<<< Updated upstream
=======
import gradio as gr

def greet(name):
    return "Hello World" + name + "!!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
>>>>>>> Stashed changes
