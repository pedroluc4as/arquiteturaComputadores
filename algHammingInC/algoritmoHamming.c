#include <stdio.h>
#include <stdlib.h>

int main ()
{
    int opcao, codificada, decodificada;
    printf("---ALGORITMO DE HAMMING---\n");
    printf("1. Codificar mensagem\n");
    printf("2. Decodificar mensagem\n");
    printf("0. Sair\n");
    printf("Escolha uma opcao e digite o numero: ");
    scanf("%d", &opcao);

    switch(opcao) {
        case 1:
            printf("Insira os bits da mensagem original (max 8 bits): ");
            scanf("%d ,&codificada");
            printf("\nCodificando bits inseridos...\n");
            // A logica para pedir os 8 bits e calcular a paridade vai aqui
            break;
        case 2:
            printf("Insira os bits da mensagem codificada (max 8 bits): ");
            scanf("%d ,&decodificada");
         
            printf("\nDecodificando os bits...\n");

            // A logica para receber os bits e decodificar vai aqui
            break;
        case 0:
            printf("\nEncerrando o programa. Deus abencoe!\n");
            break;
        default:
            printf("\nOpcao invalida!\n");
    }

    return 0;
}