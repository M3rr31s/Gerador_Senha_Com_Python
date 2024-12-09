#gerador de senhas usando python

class gerador_senha():

    def __init__(self):
        return

    def __coletar_dados(self):
               
        while True:
            try:
                self.tam_senha = int(input("Digite o tamanho da senha : "))
                break
            
            except ValueError:
                print("Valor incorreto, digite um valor do tipo número.")
                
        return
    
    def __tratar_dados(self):
        from string import ascii_letters, digits, punctuation
        import secrets

        lista = []
        i = 1
        
        conjuntos_string = (ascii_letters+digits+punctuation)
        
    
        while i <= self.tam_senha:
            x = secrets.choice(conjuntos_string)
            lista.append(x)
            i = i + 1 
        
        senha = "".join(lista)
        
        print(f'Sua nova senha é : {senha}')     
        
         
    def main(self):
        x = self.__coletar_dados()
        y = self.__tratar_dados()
        return
    
gerador_senha().main()