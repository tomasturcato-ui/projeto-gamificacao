print("=== BEM-VINDO AO QUIZ DE LÓGICA DE PROGRAMAÇÃO ===")
print("Responda com 'sim' ou 'não'.\n")

pergunta1 = input("1. A linguagem Python é interpretada? ").strip().lower()
pergunta2 = input("2. O operador == verifica igualdade em Python? ").strip().lower()

print("\n--- RESULTADO FINAL ---")

if pergunta1 == "sim" and pergunta2 == "sim":
    print("🎉 Excelente! Você acertou todas as questões de lógica básica.")

elif pergunta1 != "sim" and pergunta2 == "sim":
    print("💡 Quase lá! Você errou a primeira pergunta, mas dominou a segunda.")

elif pergunta1 == "sim" and pergunta2 != "sim":
    print("⚠️ Atenção! Você acertou a primeira, mas precisa revisar o conteúdo sobre operadores.")

else:
    print("📚 Não desanime! Vamos revisar o módulo de lógica para melhorar seu desempenho.")
