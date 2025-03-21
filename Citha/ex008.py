import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard Simples")
        self.root.geometry("800x600")

        # Botão para carregar CSV
        self.load_button = tk.Button(root, text="Carregar CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

        # Label para mostrar o resumo dos dados
        self.summary_label = tk.Label(root, text="Resumo dos dados aparecerá aqui.", justify="left")
        self.summary_label.pack(pady=10)

        # Frame para o gráfico
        self.graph_frame = tk.Frame(root)
        self.graph_frame.pack(pady=20)

    def load_csv(self):
        # Abrir a caixa de diálogo para escolher o arquivo
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        
        if file_path:
            # Carregar os dados
            self.data = pd.read_csv(file_path, delimiter=";")
            self.show_summary()
            self.plot_graph()

    def show_summary(self):
        # Exibir um resumo simples dos dados
        num_rows, num_columns = self.data.shape
        summary_text = f"Total de Linhas: {num_rows}\nTotal de Colunas: {num_columns}\n\n"

        # Filtra colunas numéricas para mostrar as estatísticas descritivas
        numeric_data = self.data.select_dtypes(include=['float64', 'int64'])
        if not numeric_data.empty:
            summary_text += "Estatísticas Descritivas (Colunas Numéricas):\n"
            
            # Ajustando as estatísticas para formatar números
            formatted_stats = numeric_data.describe().round(2)  # Arredonda para 2 casas decimais
            summary_text += formatted_stats.to_string()  # Converte para string para exibir corretamente
        else:
            summary_text += "Não há colunas numéricas para estatísticas descritivas.\n"
        
        self.summary_label.config(text=summary_text)

    def plot_graph(self):
        # Exibir um gráfico de barras (exemplo de produto vs quantidade)
        if 'Produto' in self.data.columns and 'Quantidade' in self.data.columns:
            # Criar o gráfico de barras
            fig, ax = plt.subplots(figsize=(6, 4))
            self.data.plot(kind='bar', x='Produto', y='Quantidade', ax=ax, color='skyblue')

            ax.set_title("Quantidade Vendida por Produto")
            ax.set_xlabel("Produto")
            ax.set_ylabel("Quantidade Vendida")
            
            # Colocar o gráfico dentro da interface Tkinter
            for widget in self.graph_frame.winfo_children():
                widget.destroy()  # Limpar o frame do gráfico antes de desenhar o novo gráfico

            canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

# Criar a janela principal do Tkinter
root = tk.Tk()
app = DashboardApp(root)
root.mainloop()