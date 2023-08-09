def print_identity_matrix(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print("1", end="")
            else:
                print("0", end="")
        print()

n = int(input("Masukkan jumlah ordo matriks (n): "))
print("Matriks Identitas:")
print_identity_matrix(n)
