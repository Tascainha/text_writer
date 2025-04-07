import pyautogui
import time
import tkinter as tk

def iniciar_spam():
    msg = message.get()
    count = int(qtd.get())
    intervalo = float(tempo.get())

    root.withdraw()
    time.sleep(3)

    for _ in range(count):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        time.sleep(intervalo)

    root.deiconify()

root = tk.Tk()
root.title("text_writer")

tk.Label(root, text="Mensagem:").pack()
message = tk.Entry(root, width=40)
message.pack()

tk.Label(root, text="Quantidade de vezes:").pack()
qtd = tk.Entry(root)
qtd.pack()

tk.Label(root, text="Intervalo (segundos):").pack()
tempo = tk.Entry(root)
tempo.pack()

btn = tk.Button(root, text="Iniciar", command=iniciar_spam)
btn.pack(pady=10)

root.mainloop()
