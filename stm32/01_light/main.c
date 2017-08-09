#include "sys.h"
#include "delay.h"
#include "usart.h"

int main(void){
	Hal_init();
	Stm32_Clock_Init(360, 25, 2, 8);
	delay(216);

	RCC->AHB1ENR |= 1 << 1;

	GPIOB->MODER = 0x05;
	GPIOB->OSPEEDR = 0x0F;
	GPIOB->PUPDR = 0x05;

	while(1){
		GPIOB -> BSRR = 0x03;
		delay_ms(500);
		GPIOB -> BSRR = 0x00030000
		delay_ms(500);
	}

}