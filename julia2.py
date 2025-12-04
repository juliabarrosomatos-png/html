class Hotel:
    def _init_(self):
        self.quartos = {i: {'status': 'livre', 'hospede': None, 'valor': 150} 
                        for i in range(101, 111)}
    
    def disponiveis(self):
        print("\nQuartos livres:")
        for num, q in self.quartos.items():
            if q['status'] == 'livre':
                print(f"{num} - R${q['valor']}")
    
    def check_in(self):
        self.disponiveis()
        try:
            num = int(input("Quarto: "))
            if num not in self.quartos or self.quartos[num]['status'] != 'livre':
                print("Quarto inválido ou ocupado")
                return
            
            nome = input("Nome: ")
            self.quartos[num]['status'] = 'ocupado'
            self.quartos[num]['hospede'] = nome
            print(f"Check-in feito! Quarto {num}")
        except:
            print("Erro no check-in")
    
    def check_out(self):
        ocupados = [n for n, q in self.quartos.items() if q['status'] == 'ocupado']
        if not ocupados:
            print("Nenhum quarto ocupado")
            return
        
        print("Quartos ocupados:")
        for n in ocupados:
            print(f"{n} - {self.quartos[n]['hospede']}")
        
        try:
            num = int(input("Quarto para checkout: "))
            if num not in self.quartos or self.quartos[num]['status'] != 'ocupado':
                print("Quarto inválido ou já livre")
                return
            
            diarias = int(input("Diárias: "))
            total = diarias * self.quartos[num]['valor']
            
            print(f"\nRecibo - {self.quartos[num]['hospede']}")
            print(f"Quarto: {num}")
            print(f"Diárias: {diarias}")
            print(f"Total: R${total}")
            
            self.quartos[num]['status'] = 'livre'
            self.quartos[num]['hospede'] = None
        except:
            print("Erro no check-out")
    
    def hospedes(self):
        print("\nHóspedes atuais:")
        for num, q in self.quartos.items():
            if q['status'] == 'ocupado':
                print(f"Quarto {num}: {q['hospede']}")


def main():
    hotel = Hotel()
    
    while True:
        print("\n1.Ver quartos  2.Check-in  3.Check-out  4.Hóspedes  5.Sair")
        op = input("Opção: ")
        
        if op == '1':
            hotel.disponiveis()
        elif op == '2':
            hotel.check_in()
        elif op == '3':
            hotel.check_out()
        elif op == '4':
            hotel.hospedes()
        elif op == '5':
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


if __name__ == "_main_":
    main()  