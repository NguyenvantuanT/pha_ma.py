import tkinter as tk
from tkinter import messagebox

def generate_playfair_matrix(key):
    alphabet = 'abcdefghiklmnopqrstuvwxyz' # Bỏ 'j' vì thường được thay thế bằng 'i'
    key = key.lower().replace('j', 'i')
    key += alphabet
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_char(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)
    return None

def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_char(matrix, char1)
        row2, col2 = find_char(matrix, char2)
        if row1 == row2: # Cùng hàng
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2: # Cùng cột
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else: # Khác hàng và cột
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

def decrypt():
    ciphertext = entry_ciphertext.get()
    key = entry_key.get()
    if len(key) == 0 or len(ciphertext) == 0:
        messagebox.showerror("Error", "Please enter ciphertext and key")
        return
    plaintext = decrypt_playfair(ciphertext, key)
    entry_plaintext.delete(0, tk.END)
    entry_plaintext.insert(0, plaintext)

# Tạo giao diện
root = tk.Tk()
root.title("Playfair Decryptor")

# Khung nhập liệu
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_ciphertext = tk.Label(frame_input, text="Ciphertext:")
label_ciphertext.grid(row=0, column=0, padx=5)
entry_ciphertext = tk.Entry(frame_input)
entry_ciphertext.grid(row=0, column=1, padx=5)

label_key = tk.Label(frame_input, text="Key:")
label_key.grid(row=1, column=0, padx=5)
entry_key = tk.Entry(frame_input)
entry_key.grid(row=1, column=1, padx=5)

# Nút giải mã
btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt)
btn_decrypt.pack(pady=5)

# Khung hiển thị kết quả
frame_output = tk.Frame(root)
frame_output.pack(pady=10)

label_plaintext = tk.Label(frame_output, text="Plaintext:")
label_plaintext.grid(row=0, column=0, padx=5)
entry_plaintext = tk.Entry(frame_output)
entry_plaintext.grid(row=0, column=1, padx=5)

root.mainloop()
