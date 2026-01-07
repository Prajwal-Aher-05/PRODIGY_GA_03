"""
PRODIGY GA_03: Markov Chain Text Generator (Complete)
"""
import random
from collections import defaultdict
import gradio as gr

# Training data
text = "to be or not to be that is the question nobler mind suffer fortune take arms sea troubles"

# Build Markov chain
chain = defaultdict(list)
words = text.split()
for i in range(len(words)-1):
    chain[words[i]].append(words[i+1])

# Generate function
def generate(start="to", length=15):
    result = [start]
    current = start
    for _ in range(length):
        if current in chain:
            next_word = random.choice(chain[current])
            result.append(next_word)
            current = next_word
        else:
            break
    return ' '.join(result)

# Demo prints
print("=== DEMO OUTPUTS ===")
print("1:", generate("to"))
print("2:", generate("be"))
print("3:", generate("question"))

# Gradio App
def markov_app(seed, length=15):
    return generate(seed, int(length))

demo = gr.Interface(
    fn=markov_app,
    inputs=[gr.Textbox("to", label="Seed"), gr.Slider(5,30,15,label="Length")],
    outputs=gr.Textbox(label="Generated"),
    title="Markov Chain Live Demo"
)
demo.launch(share=True)
