import os
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

# Список папок, которые нужно игнорировать
IGNORE_DIRS = {'__pycache__', '.git', '.idea', '.venv', 'logs'}


def add_files_to_tree(tree, parent, path):
    """ Рекурсивно добавляет файлы и папки в дерево, игнорируя определённые директории """
    for p in sorted(Path(path).iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        if p.name in IGNORE_DIRS:
            continue
        # Устанавливаем open=True для всех узлов, чтобы они были раскрыты
        node_id = tree.insert(parent, 'end', text=p.name, open=True)
        if p.is_dir():
            add_files_to_tree(tree, node_id, p)
        tree.set(node_id, 'fullpath', str(p))


def collect_selected_files(tree, selected_files):
    """ Собирает выбранные файлы из дерева """
    for node in tree.selection():
        node_path = tree.set(node, 'fullpath')
        if os.path.isfile(node_path):
            selected_files.append(node_path)


def save_selected_files(selected_files):
    """ Функция для сохранения выбранных файлов в текстовый файл. """
    output_filename = ".selected_files_code.txt"
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            # Записываем имена файлов
            f.write(", ".join(f'"{os.path.relpath(file, start=os.getcwd())}"' for file in selected_files) + "\n\n")
            # Записываем содержимое файлов
            for file in selected_files:
                f.write(f"{os.path.relpath(file, start=os.getcwd())}:\n```\n")
                with open(file, 'r', encoding='utf-8') as content_file:
                    f.write(content_file.read())
                f.write("\n```\n\n")
        messagebox.showinfo("Success", "The files have been successfully written to the output file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def main():
    root = tk.Tk()
    root.title("File Selector")
    root.geometry("800x600")
    root.configure(bg='#f0f0f0')
    
    container = ttk.Frame(root)
    container.pack(fill='both', expand=True)
    
    tree_scroll_y = ttk.Scrollbar(container, orient="vertical")
    tree_scroll_x = ttk.Scrollbar(container, orient="horizontal")
    tree_scroll_y.pack(side='right', fill='y')
    tree_scroll_x.pack(side='bottom', fill='x')
    
    tree = ttk.Treeview(container, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set,
                        columns=('fullpath',), displaycolumns=())
    tree.heading('#0', text='Project Files', anchor='w')
    
    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.config(command=tree.xview)
    
    style = ttk.Style()
    style.configure("Treeview", font=('Helvetica', 12), background="#ffffff", fieldbackground="#ffffff")
    style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), background="#e0ffff", foreground="#003366")
    
    tree.pack(fill='both', expand=True)
    
    base_path = os.getcwd()
    add_files_to_tree(tree, '', base_path)
    
    def on_select():
        selected_files = []
        collect_selected_files(tree, selected_files)
        if selected_files:
            save_selected_files(selected_files)
        else:
            messagebox.showinfo("No Selection", "No files were selected.")
    
    select_button = tk.Button(root, text="Выбрать файлы", command=on_select, bg="#e0ffff", fg="#003366",
                              font=('Helvetica', 12, 'bold'))
    select_button.pack(fill='x')
    
    def item_clicked(event):
        item = tree.identify('item', event.x, event.y)
        if item:
            if item in tree.selection():
                tree.selection_remove(item)
            else:
                tree.selection_add(item)
    
    tree.bind('<Double-1>', item_clicked)
    
    root.mainloop()


if __name__ == "__main__":
    main()