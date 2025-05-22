def gerar_nota_peso_preco():
    print("🧾 GERADOR DE NOTA (SOMA DE PESO E PREÇO)")
    data = input("Data (ex: 22/05/2025): ").strip()

    while True:
        peso_boi = input("Peso total do boi (kg, use ponto): ").strip()
        try:
            peso_boi_float = float(peso_boi)
            break
        except ValueError:
            print("⚠️ Valor inválido. Tente de novo.")

    cortes = []
    while True:
        corte = input("Corte (ENTER para finalizar): ").strip()
        if not corte:
            break

        # Pede peso
        while True:
            peso = input(f"Peso de {corte} (kg, use ponto): ").strip()
            try:
                peso_float = float(peso)
                break
            except ValueError:
                print("⚠️ Peso inválido. Tente de novo.")

        # Pede preço por kg
        while True:
            preco_kg = input(f"Preço por kg de {corte} (use ponto): ").strip()
            try:
                preco_kg_float = float(preco_kg)
                break
            except ValueError:
                print("⚠️ Preço inválido. Tente de novo.")

        cortes.append((corte.upper(), peso_float, preco_kg_float))

    total_peso = sum(p for _, p, _ in cortes)
    total_valor = sum(peso * preco for _, peso, preco in cortes)

    # Montar a nota
    linhas = [
        f"DATA: {data}",
        f"PESO TOTAL DO BOI: {peso_boi_float:.3f} kg\n",
        "    AV RACOES E FRIGORIFICO\n",
    ]

    for corte, peso, preco in cortes:
        valor_corte = peso * preco
        linhas.append(f"{corte.ljust(20, '.')} {peso:>6.3f} kg\n  R$ {valor_corte:>8.2f}")

    linhas.append("")
    linhas.append(f"TOTAL PESO".ljust(20, '.') + f" {total_peso:>6.3f} kg")
    linhas.append(f"TOTAL VALOR".ljust(20, '.') + f" R${total_valor:>8.2f}")
    linhas.append("\n\n")

    nota_texto = "\n".join(linhas)

    print("\nPrévia da nota:")
    print("-" * 40)
    print(nota_texto)
    print("-" * 40)

    confirma = input("Imprimir? (s/n): ").strip().lower()
    if confirma == 's':
        with open("/dev/usb/lp0", "w") as imp:
            imp.write("\x1B\x40")  # reset
            imp.write(nota_texto)
            imp.write("\x1B\x64\x02")  # avanço de papel (menos linhas)
        print("✅ Nota enviada para a impressora.")
    else:
        print("❌ Cancelado.")

if __name__ == "__main__":
    gerar_nota_peso_preco()
